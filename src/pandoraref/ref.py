# Standard library
import warnings
from functools import lru_cache

# Third-party
import astropy.units as u
import numpy as np
import pandas as pd
from astropy.constants import c, h

# import pandorasat as ps
from astropy.io import fits
from astropy.wcs import WCS

from . import PACKAGEDIR

__all__ = ["NIRDAReference", "VISDAReference"]


class RefMixins:
    """Mixins common to each detector."""

    @property
    def flat_file(self):
        return f"{PACKAGEDIR}/data/{self.name.lower()}/flat.fits"

    @property
    def bias_file(self):
        return f"{PACKAGEDIR}/data/{self.name.lower()}/bias.fits"

    @property
    def dark_file(self):
        return f"{PACKAGEDIR}/data/{self.name.lower()}/dark.fits"

    @property
    def gain_file(self):
        return f"{PACKAGEDIR}/data/{self.name.lower()}/gain.fits"

    @property
    def readnoise_file(self):
        return f"{PACKAGEDIR}/data/{self.name.lower()}/readnoise.fits"

    @property
    def bad_pixel_file(self):
        return f"{PACKAGEDIR}/data/{self.name.lower()}/badpix.fits"

    @property
    def nonlin_file(self):
        return f"{PACKAGEDIR}/data/{self.name.lower()}/nonlin.fits"

    @property
    def sip_file(self):
        return f"{PACKAGEDIR}/data/{self.name.lower()}/sip.fits"

    @property
    def wcs_file(self):
        return f"{PACKAGEDIR}/data/{self.name.lower()}/wcs.fits"

    @property
    def qe_file(self):
        return f"{PACKAGEDIR}/data/{self.name.lower()}/qe.fits"

    @property
    def throughput_file(self):
        return f"{PACKAGEDIR}/data/{self.name.lower()}/throughput.fits"

    def get_wcs(
        self,
        target_ra: u.Quantity = 0 * u.deg,
        target_dec: u.Quantity = 0 * u.deg,
        theta: u.Quantity = 0 * u.deg,
        distortion=True,
    ):
        """Get the World Coordinate System for a detector as an astropy.wcs.WCS object, given pointing parameters.
        This method only updates the CRVAL and PC parameters, the rest of the WCS is set by reference products
        within this package.

        Parameters:
        -----------
        target_ra: astropy.units.Quantity
            The target RA in degrees
        target_dec: astropy.units.Quantity
            The target Dec in degrees
        theta: astropy.units.Quantity
            The observatory angle in degrees

        Returns:
        --------
        wcs: astropy.wcs.WCS
            World Coordinate System object
        """

        hdu = fits.open(self.wcs_file)[0]
        matrix = np.asarray(
            [
                [np.cos(theta).value, -np.sin(theta).value],
                [np.sin(theta).value, np.cos(theta).value],
            ]
        )
        hdu.header["CRVAL1"] = target_ra.value
        hdu.header["CRVAL2"] = target_dec.value
        for idx in range(2):
            for jdx in range(2):
                hdu.header[f"PC{idx + 1}_{jdx + 1}"] = matrix[idx, jdx]

        if distortion:
            sip_hdr = fits.open(self.sip_file)[0].header
            cards = [
                card
                for card in sip_hdr.cards
                if (
                    card[0].startswith("A_")
                    | card[0].startswith("B_")
                    | card[0].startswith("AP_")
                    | card[0].startswith("BP_")
                )
            ]
            hdu.header.extend(cards)
            hdu.header["CTYPE1"] = "RA---TAN-SIP"
            hdu.header["CTYPE2"] = "DEC--TAN-SIP"

        with warnings.catch_warnings():
            # The warning here is because this is a WCS with no data associated
            warnings.simplefilter("ignore")
            wcs = WCS(hdu.header)

        return wcs

    def get_sip(self):
        """Retrieve the SIP file as an astropy.wcs.SIP object"""
        hdr = fits.open(self.sip_file)[0].header
        hdr["CTYPE1"] = "RA---TAN-SIP"
        hdr["CTYPE2"] = "DEC--TAN-SIP"
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            sip = WCS(hdr).sip
        return sip

    @lru_cache()
    def _get_throughput_data(self):
        """This helper function ensures that we only have to do the IO of this file once"""
        with fits.open(self.throughput_file) as hdulist:
            wav_grid, throughput = (
                u.Quantity(
                    hdulist[1].data["wavelength"], hdulist[1].header["TUNIT1"]
                ),
                u.Quantity(hdulist[1].data["throughput"]),
            )
        return wav_grid, throughput

    def get_throughput(self, wavelength):
        """
        Get the throughput of the detector.

        Parameters
        ----------
        wavelength : npt.NDArray
            Wavelength in microns as an `astropy.Quantity`

        Returns
        -------
        throughput : npt.NDArray
            Array of the throughput of the detector
        """
        wav_grid, throughput = self._get_throughput_data()
        return u.Quantity(
            np.interp(
                u.Quantity(wavelength, u.micron).value,
                wav_grid.to(u.micron).value,
                throughput.value,
            )
        )

    @lru_cache()
    def _get_qe_data(self):
        """This helper function ensures that we only have to do the IO of this file once"""
        with fits.open(self.qe_file) as hdulist:
            wav_grid, qe = (
                u.Quantity(
                    hdulist[1].data["wavelength"], hdulist[1].header["TUNIT1"]
                ),
                u.Quantity(hdulist[1].data["qe"]),
            )
        return wav_grid, qe

    def get_qe(self, wavelength):
        """
        Get the quantum efficiency of the detector.

        Parameters
        ----------
        wavelength : npt.NDArray
            Wavelength in microns as an `astropy.Quantity`

        Returns
        -------
        qe : npt.NDArray
            Array of the quantum efficiency of the detector
        """
        wav_grid, qe = self._get_qe_data()
        return u.Quantity(
            np.interp(
                u.Quantity(wavelength, u.micron).value,
                wav_grid.to(u.micron).value,
                qe.value,
            )
        )

    def get_sensitivity(self, wavelength):
        """
        Get the sensitivity of the detector.
        This is currently calculated from the throughput and QE.
        In future this is likely to be replaced by an RDP of the empirical sensitivity.

        Parameters
        ----------
        wavelength : npt.NDArray
            Wavelength in microns as an `astropy.Quantity`

        Returns
        -------
        sensitivity : npt.NDArray
            Array of the sensitivity of the detector
        """

        A_primary = np.pi * ((43.5 * u.cm).to(u.m) / 2) ** 2
        A_secondary = np.pi * ((86 * u.mm).to(u.m) / 2) ** 2
        mirror_diameter = ((A_primary - A_secondary) / np.pi) ** 0.5

        def photon_energy(wavelength):
            """Converts photon wavelength to energy."""
            return ((h * c) / wavelength) * 1 / u.photon

        sed = 1 * u.erg / u.s / u.cm**2 / u.angstrom
        E = photon_energy(wavelength)
        telescope_area = np.pi * (mirror_diameter / 2) ** 2
        photon_flux_density = (
            telescope_area * sed * self.get_throughput(wavelength) / E
        ).to(u.photon / u.second / u.angstrom) * self.get_qe(wavelength)
        sensitivity = photon_flux_density / sed
        return sensitivity

    @lru_cache()
    def _get_vega_data(self):
        """This helper function ensures that we only have to do the IO of this file once"""
        df = pd.read_csv(
            f"{PACKAGEDIR}/data/external/vega.csv",
            header=None,
        )
        wavelength, spectrum = df.values.T
        wavelength *= u.angstrom
        spectrum *= u.erg / u.cm**2 / u.s / u.angstrom
        return wavelength, spectrum

    def get_zeropoint(self):
        """Returns the Vega magnitude system zeropoint of the detector."""
        wavelength, spectrum = self._get_vega_data()
        sens = self.get_sensitivity(wavelength)
        zeropoint = np.trapz(spectrum * sens, wavelength) / np.trapz(
            sens, wavelength
        )
        return zeropoint


class NIRDAReference(RefMixins):
    """Class for returning paths to the NIRDA reference data files.

    This class can only load objects or give file paths to objects that exist in the package. It can not make new objects.
    """

    @property
    def name(self):
        return "NIRDA"

    def __repr__(self):
        return "NIRDAReference Object"

    @property
    def pixel_position_file(self):
        return f"{PACKAGEDIR}/data/{self.name.lower()}/pixel_position.fits"

    @lru_cache()
    def _get_pixel_position_data(self):
        """This helper function ensures that we only have to do the IO of this file once"""
        with fits.open(self.pixel_position_file) as hdulist:
            wav_grid, pixel_position = (
                u.Quantity(
                    hdulist[1].data["wavelength"], hdulist[1].header["TUNIT1"]
                ),
                u.Quantity(
                    hdulist[1].data["pixel"],
                    hdulist[1].header["TUNIT2"],
                ),
            )
        return wav_grid, pixel_position

    def get_pixel_position(self, wavelength):
        """
        Get the pixel position on the detector given a wavelength.

        Parameters
        ----------
        wavelength : npt.NDArray
            Wavelength in microns as an `astropy.Quantity`

        Returns
        -------
        qe : npt.NDArray
            Array of the pixel positions
        """
        wav_grid, pixel_position = self._get_pixel_position_data()
        return u.Quantity(
            np.interp(
                u.Quantity(wavelength, u.micron).value,
                wav_grid.to(u.micron).value,
                pixel_position.value,
            )
            * u.pixel
        )

    def get_wavelength_position(self, pixel):
        """
        Get the wavelength of a pixel position on the detector.

        Parameters
        ----------
        pixel : npt.NDArray, u.Quantity
            Pixel as as an `astropy.Quantity`

        Returns
        -------
        qe : npt.NDArray, u.Quantity
            Array of the wavelength of the pixel position
        """
        wav_grid, pixel_position = self._get_pixel_position_data()
        return u.Quantity(
            np.interp(
                u.Quantity(pixel, u.pixel).value,
                pixel_position.value,
                wav_grid.value,
            )
            * wav_grid.unit
        )


class VISDAReference(RefMixins):
    """Class for returning paths to the VISDA reference data files.

    This class can only load objects or give file paths to objects that exist in the package. It can not make new objects.
    """

    @property
    def name(self):
        return "VISDA"

    def __repr__(self):
        return "VISDAReference Object"
