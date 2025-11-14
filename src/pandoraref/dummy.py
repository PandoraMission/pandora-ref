"""Module for making dummy files. Use these as a way to set expectations for how files should be structured, if you have no other option."""

# Third-party
import astropy.units as u
import numpy as np
from astropy.io import fits
from astropy.time import Time
from astropy.wcs import WCS

from . import PACKAGEDIR
from .wcs import _read_distortion_file, create_sip, create_wcs

__all__ = ["create_dummy_reference_products"]


def create_visda_dummy_bad_pixel_map():
    """Creates a dummy file that is a placeholder for a bad pixel map on the VISDA."""
    quality = np.zeros((2048, 2048), dtype=np.uint16)
    for idx in range(16):
        quality[idx * 10 : (idx + 1) * 10, idx * 10 : (idx + 1) * 10] = 2**idx

    hdr0 = fits.Header(
        [
            ("TELESCOP", "NASA Pandora", "telescope"),
            ("CAMERAID", "PcoCam", "ID of camera used in acquisition"),
            ("INSTRMNT", "VISDA", "instrument"),
            (
                "CREATOR",
                "Pandora DPC Software",
                "Software that created this file",
            ),
            (
                "AUTHOR",
                "Christina Hedges",
                "Person or group that created this file",
            ),
            ("DATASRC", "DUMMY", ""),
            ("VERSION", "dummy", "creator software version"),
            ("DATE", Time.now().isot, "creation date"),
            (
                "COMMENT",
                "This file has been created as a place holder for a RDP",
            ),
        ]
    )

    hdr1 = fits.Header(
        [
            ("EXTNAME", "BAD_PIX", "name of extension"),
            ("0", "NO ISSUE", "bit definition"),
            ("1", "Placeholder", "bit definition"),
            ("2", "Placeholder", "bit definition"),
            ("3", "Placeholder", "bit definition"),
            ("4", "Placeholder", "bit definition"),
            ("5", "Placeholder", "bit definition"),
            ("6", "Placeholder", "bit definition"),
            ("7", "Placeholder", "bit definition"),
            ("8", "Placeholder", "bit definition"),
            ("9", "Placeholder", "bit definition"),
            ("10", "Placeholder", "bit definition"),
            ("11", "Placeholder", "bit definition"),
            ("12", "Placeholder", "bit definition"),
            ("13", "Placeholder", "bit definition"),
            ("14", "Placeholder", "bit definition"),
            ("15", "Placeholder", "bit definition"),
        ]
    )
    hdulist = fits.HDUList(
        [fits.PrimaryHDU(header=hdr0), fits.CompImageHDU(quality, header=hdr1)]
    )
    return hdulist


def create_nirda_dummy_bad_pixel_map():
    """Creates a dummy file that is a placeholder for a bad pixel map on the NIRDA."""
    quality = np.zeros((2048, 2048), dtype=np.uint16)
    for idx in range(16):
        quality[idx * 10 : (idx + 1) * 10, idx * 10 : (idx + 1) * 10] = 2**idx

    hdr0 = fits.Header(
        [
            ("TELESCOP", "NASA Pandora", "telescope"),
            ("CAMERAID", "H2rgCam", "ID of camera used in acquisition"),
            ("INSTRMNT", "NIRDA", "instrument"),
            (
                "CREATOR",
                "Pandora DPC Software",
                "Software that created this file",
            ),
            (
                "AUTHOR",
                "Christina Hedges",
                "Person or group that created this file",
            ),
            ("DATASRC", "DUMMY", ""),
            ("VERSION", "dummy", "creator software version"),
            ("DATE", Time.now().isot, "creation date"),
            (
                "COMMENT",
                "This file has been created as a place holder for a RDP",
            ),
        ]
    )

    hdr1 = fits.Header(
        [
            ("EXTNAME", "BAD_PIX", "name of extension"),
            ("0", "NO ISSUE", "bit definition"),
            ("1", "Placeholder", "bit definition"),
            ("2", "Placeholder", "bit definition"),
            ("3", "Placeholder", "bit definition"),
            ("4", "Placeholder", "bit definition"),
            ("5", "Placeholder", "bit definition"),
            ("6", "Placeholder", "bit definition"),
            ("7", "Placeholder", "bit definition"),
            ("8", "Placeholder", "bit definition"),
            ("9", "Placeholder", "bit definition"),
            ("10", "Placeholder", "bit definition"),
            ("11", "Placeholder", "bit definition"),
            ("12", "Placeholder", "bit definition"),
            ("13", "Placeholder", "bit definition"),
            ("14", "Placeholder", "bit definition"),
            ("15", "Placeholder", "bit definition"),
        ]
    )
    hdulist = fits.HDUList(
        [fits.PrimaryHDU(header=hdr0), fits.CompImageHDU(quality, header=hdr1)]
    )
    return hdulist


def create_visda_dummy_flat():
    """Creates a dummy file that is a placeholder for a flat on the VISDA."""
    flat = np.ones((2048, 2048), dtype=np.float32)

    hdr0 = fits.Header(
        [
            ("TELESCOP", "NASA Pandora", "telescope"),
            ("CAMERAID", "PcoCam", "ID of camera used in acquisition"),
            ("INSTRMNT", "VISDA", "instrument"),
            (
                "CREATOR",
                "Pandora DPC Software",
                "Software that created this file",
            ),
            (
                "AUTHOR",
                "Christina Hedges",
                "Person or group that created this file",
            ),
            ("DATASRC", "DUMMY", ""),
            ("VERSION", "dummy", "creator software version"),
            ("DATE", Time.now().isot, "creation date"),
            (
                "COMMENT",
                "This file has been created as a place holder for a RDP",
            ),
        ]
    )

    hdr1 = fits.Header(
        [
            ("EXTNAME", "FLAT", "name of extension"),
        ]
    )
    hdulist = fits.HDUList(
        [fits.PrimaryHDU(header=hdr0), fits.CompImageHDU(flat, header=hdr1)]
    )
    return hdulist


def create_nirda_dummy_flat():
    """Creates a dummy file that is a placeholder for a flat on the VISDA."""
    flat = np.ones((2048, 2048), dtype=np.float32)

    hdr0 = fits.Header(
        [
            ("TELESCOP", "NASA Pandora", "telescope"),
            ("CAMERAID", "H2rgCam", "ID of camera used in acquisition"),
            ("INSTRMNT", "NIRDA", "instrument"),
            (
                "CREATOR",
                "Pandora DPC Software",
                "Software that created this file",
            ),
            (
                "AUTHOR",
                "Christina Hedges",
                "Person or group that created this file",
            ),
            ("DATASRC", "DUMMY", ""),
            ("VERSION", "dummy", "creator software version"),
            ("DATE", Time.now().isot, "creation date"),
            (
                "COMMENT",
                "This file has been created as a place holder for a RDP",
            ),
        ]
    )

    hdr1 = fits.Header(
        [
            ("EXTNAME", "FLAT", "name of extension"),
        ]
    )
    hdulist = fits.HDUList(
        [fits.PrimaryHDU(header=hdr0), fits.CompImageHDU(flat, header=hdr1)]
    )
    return hdulist


def create_visda_dummy_bias():
    """Creates a dummy file that is a placeholder for a bias on the VISDA."""
    bias = np.ones((2048, 2048), dtype=np.int16) * 100

    hdr0 = fits.Header(
        [
            ("TELESCOP", "NASA Pandora", "telescope"),
            ("CAMERAID", "PcoCam", "ID of camera used in acquisition"),
            ("INSTRMNT", "VISDA", "instrument"),
            (
                "CREATOR",
                "Pandora DPC Software",
                "Software that created this file",
            ),
            (
                "AUTHOR",
                "Christina Hedges",
                "Person or group that created this file",
            ),
            ("DATASRC", "DUMMY", ""),
            ("VERSION", "dummy", "creator software version"),
            ("DATE", Time.now().isot, "creation date"),
            (
                "COMMENT",
                "This file has been created as a place holder for a RDP",
            ),
        ]
    )

    hdr1 = fits.Header(
        [
            ("EXTNAME", "BIAS", "name of extension"),
            ("UNIT", "DN", "unit of extension"),
        ]
    )
    hdulist = fits.HDUList(
        [fits.PrimaryHDU(header=hdr0), fits.CompImageHDU(bias, header=hdr1)]
    )
    return hdulist


def create_nirda_dummy_bias():
    """Creates a dummy file that is a placeholder for a bias on the VISDA."""
    bias = np.ones((2048, 2048), dtype=np.int16) * 6000

    hdr0 = fits.Header(
        [
            ("TELESCOP", "NASA Pandora", "telescope"),
            ("CAMERAID", "H2rgCam", "ID of camera used in acquisition"),
            ("INSTRMNT", "NIRDA", "instrument"),
            (
                "CREATOR",
                "Pandora DPC Software",
                "Software that created this file",
            ),
            (
                "AUTHOR",
                "Christina Hedges",
                "Person or group that created this file",
            ),
            ("DATASRC", "DUMMY", ""),
            ("VERSION", "dummy", "creator software version"),
            ("DATE", Time.now().isot, "creation date"),
            (
                "COMMENT",
                "This file has been created as a place holder for a RDP",
            ),
        ]
    )

    hdr1 = fits.Header(
        [
            ("EXTNAME", "BIAS", "name of extension"),
            ("UNIT", "DN", "unit of extension"),
        ]
    )
    hdulist = fits.HDUList(
        [fits.PrimaryHDU(header=hdr0), fits.CompImageHDU(bias, header=hdr1)]
    )
    return hdulist


def create_visda_dummy_dark():
    """Creates a dummy file that is a placeholder for a dark on the VISDA."""
    hdr0 = fits.Header(
        [
            ("TELESCOP", "NASA Pandora", "telescope"),
            ("CAMERAID", "PcoCam", "ID of camera used in acquisition"),
            ("INSTRMNT", "VISDA", "instrument"),
            (
                "CREATOR",
                "Pandora DPC Software",
                "Software that created this file",
            ),
            (
                "AUTHOR",
                "Christina Hedges",
                "Person or group that created this file",
            ),
            ("DATASRC", "DUMMY", ""),
            ("VERSION", "dummy", "creator software version"),
            ("DATE", Time.now().isot, "creation date"),
            ("DARK", 1, "dark rate in electron/second/pixel"),
            ("UNIT", "electron/second/pixel", "unit of dark rate"),
            (
                "COMMENT",
                "This file has been created as a place holder for a RDP",
            ),
        ]
    )
    hdulist = fits.HDUList([fits.PrimaryHDU(header=hdr0)])
    return hdulist


def create_nirda_dummy_dark():
    """Creates a dummy file that is a placeholder for a dark on the VISDA."""
    hdr0 = fits.Header(
        [
            ("TELESCOP", "NASA Pandora", "telescope"),
            ("CAMERAID", "H2rgCam", "ID of camera used in acquisition"),
            ("INSTRMNT", "NIRDA", "instrument"),
            (
                "CREATOR",
                "Pandora DPC Software",
                "Software that created this file",
            ),
            (
                "AUTHOR",
                "Christina Hedges",
                "Person or group that created this file",
            ),
            ("DATASRC", "DUMMY", ""),
            ("VERSION", "dummy", "creator software version"),
            ("DATE", Time.now().isot, "creation date"),
            ("DARK", 1, "dark rate in electron/second/pixel"),
            ("UNIT", "electron/second/pixel", "unit of dark rate"),
            (
                "COMMENT",
                "This file has been created as a place holder for a RDP",
            ),
        ]
    )

    hdulist = fits.HDUList([fits.PrimaryHDU(header=hdr0)])
    return hdulist


def create_visda_dummy_gain():
    """Creates a dummy file that is a placeholder for a dark on the VISDA."""
    hdr0 = fits.Header(
        [
            ("TELESCOP", "NASA Pandora", "telescope"),
            ("CAMERAID", "PcoCam", "ID of camera used in acquisition"),
            ("INSTRMNT", "VISDA", "instrument"),
            (
                "CREATOR",
                "Pandora DPC Software",
                "Software that created this file",
            ),
            (
                "AUTHOR",
                "Christina Hedges",
                "Person or group that created this file",
            ),
            ("DATASRC", "DUMMY", ""),
            ("VERSION", "dummy", "creator software version"),
            ("DATE", Time.now().isot, "creation date"),
            ("GAIN", 0.6, "gain setting in electron/ADU"),
            ("UNIT", "electron/DN", "unit of gain"),
            (
                "COMMENT",
                "This file has been created as a place holder for a RDP",
            ),
        ]
    )
    hdulist = fits.HDUList([fits.PrimaryHDU(header=hdr0)])
    return hdulist


def create_nirda_dummy_gain():
    """Creates a dummy file that is a placeholder for a dark on the VISDA."""
    hdr0 = fits.Header(
        [
            ("TELESCOP", "NASA Pandora", "telescope"),
            ("CAMERAID", "H2rgCam", "ID of camera used in acquisition"),
            ("INSTRMNT", "NIRDA", "instrument"),
            (
                "CREATOR",
                "Pandora DPC Software",
                "Software that created this file",
            ),
            (
                "AUTHOR",
                "Christina Hedges",
                "Person or group that created this file",
            ),
            ("DATASRC", "DUMMY", ""),
            ("VERSION", "dummy", "creator software version"),
            ("DATE", Time.now().isot, "creation date"),
            ("GAIN", 2.1, "gain setting in electron/ADU"),
            ("UNIT", "electron/DN", "unit of gain"),
            (
                "COMMENT",
                "This file has been created as a place holder for a RDP",
            ),
        ]
    )

    hdulist = fits.HDUList([fits.PrimaryHDU(header=hdr0)])
    return hdulist


def create_visda_dummy_read_noise():
    """Creates a dummy file that is a placeholder for a dark on the VISDA."""
    hdr0 = fits.Header(
        [
            ("TELESCOP", "NASA Pandora", "telescope"),
            ("CAMERAID", "PcoCam", "ID of camera used in acquisition"),
            ("INSTRMNT", "VISDA", "instrument"),
            (
                "CREATOR",
                "Pandora DPC Software",
                "Software that created this file",
            ),
            (
                "AUTHOR",
                "Christina Hedges",
                "Person or group that created this file",
            ),
            ("DATASRC", "DUMMY", ""),
            ("VERSION", "dummy", "creator software version"),
            ("DATE", Time.now().isot, "creation date"),
            ("READNS", 1.5, "read noise in electrons per pixel"),
            ("UNIT", "electron/pixel", "unit of read noise"),
            (
                "COMMENT",
                "This file has been created as a place holder for a RDP",
            ),
        ]
    )
    hdulist = fits.HDUList([fits.PrimaryHDU(header=hdr0)])
    return hdulist


def create_nirda_dummy_read_noise():
    """Creates a dummy file that is a placeholder for a dark on the VISDA."""
    hdr0 = fits.Header(
        [
            ("TELESCOP", "NASA Pandora", "telescope"),
            ("CAMERAID", "H2rgCam", "ID of camera used in acquisition"),
            ("INSTRMNT", "NIRDA", "instrument"),
            (
                "CREATOR",
                "Pandora DPC Software",
                "Software that created this file",
            ),
            (
                "AUTHOR",
                "Christina Hedges",
                "Person or group that created this file",
            ),
            ("DATASRC", "DUMMY", ""),
            ("VERSION", "dummy", "creator software version"),
            ("DATE", Time.now().isot, "creation date"),
            ("READNS", 18 / np.sqrt(2), "read noise in electrons per pixel"),
            ("UNIT", "electron/pixel", "unit of read noise"),
            (
                "COMMENT",
                "This file has been created as a place holder for a RDP",
            ),
        ]
    )

    hdulist = fits.HDUList([fits.PrimaryHDU(header=hdr0)])
    return hdulist


def create_visda_dummy_non_linearity():
    """Creates a dummy file that is a placeholder for a non linearity on the VISDA."""
    nonlin_ADU = np.linspace(0, 60000, dtype=np.float32)
    nonlin_electrons = np.linspace(0, 60000, dtype=np.float32)

    hdr0 = fits.Header(
        [
            ("TELESCOP", "NASA Pandora", "telescope"),
            ("CAMERAID", "PcoCam", "ID of camera used in acquisition"),
            ("INSTRMNT", "VISDA", "instrument"),
            (
                "CREATOR",
                "Pandora DPC Software",
                "Software that created this file",
            ),
            (
                "AUTHOR",
                "Christina Hedges",
                "Person or group that created this file",
            ),
            ("DATASRC", "DUMMY", ""),
            ("VERSION", "dummy", "creator software version"),
            ("DATE", Time.now().isot, "creation date"),
            (
                "COMMENT",
                "This file has been created as a place holder for a RDP",
            ),
        ]
    )

    hdr1 = fits.Header(
        [
            ("EXTNAME", "NON LINEARITY", "name of extension"),
        ]
    )
    tab = fits.TableHDU.from_columns(
        [
            fits.Column(name="ADU", format="E", array=nonlin_ADU),
            fits.Column(name="eletrons", format="E", array=nonlin_electrons),
        ],
        header=hdr1,
    )

    hdulist = fits.HDUList([fits.PrimaryHDU(header=hdr0), tab])
    return hdulist


def create_nirda_dummy_non_linearity():
    """Creates a dummy file that is a placeholder for a non linearity on the NIRDA."""
    nonlin_ADU = np.linspace(0, 60000, dtype=np.float32)
    nonlin_electrons = np.linspace(0, 60000, dtype=np.float32)

    hdr0 = fits.Header(
        [
            ("TELESCOP", "NASA Pandora", "telescope"),
            ("CAMERAID", "H2rgCam", "ID of camera used in acquisition"),
            ("INSTRMNT", "NIRDA", "instrument"),
            (
                "CREATOR",
                "Pandora DPC Software",
                "Software that created this file",
            ),
            (
                "AUTHOR",
                "Christina Hedges",
                "Person or group that created this file",
            ),
            ("DATASRC", "DUMMY", ""),
            ("VERSION", "dummy", "creator software version"),
            ("DATE", Time.now().isot, "creation date"),
            (
                "COMMENT",
                "This file has been created as a place holder for a RDP",
            ),
        ]
    )

    hdr1 = fits.Header(
        [
            ("EXTNAME", "NON LINEARITY", "name of extension"),
        ]
    )
    tab = fits.TableHDU.from_columns(
        [
            fits.Column(name="ADU", format="E", array=nonlin_ADU),
            fits.Column(name="eletrons", format="E", array=nonlin_electrons),
        ],
        header=hdr1,
    )

    hdulist = fits.HDUList([fits.PrimaryHDU(header=hdr0), tab])
    return hdulist


def create_visda_v0_1_0_wcs():
    hdr0 = fits.Header(
        [
            ("TELESCOP", "NASA Pandora", "telescope"),
            ("CAMERAID", "PcoCam", "ID of camera used in acquisition"),
            ("INSTRMNT", "VISDA", "instrument"),
            (
                "CREATOR",
                "Pandora DPC Software",
                "Software that created this file",
            ),
            (
                "AUTHOR",
                "Christina Hedges",
                "Person or group that created this file",
            ),
            ("DATASRC", "SIMULATION", ""),
            ("VERSION", "v0.1.0", "creator software version"),
            ("DATE", Time.now().isot, "creation date"),
        ]
    )

    hdulist = create_wcs(
        target_ra=0,
        target_dec=0,
        theta=0,
        naxis1=2048,
        naxis2=2048,
        crpix1=1024,
        crpix2=1024,
        pixel_scale=0.78 * u.arcsecond / u.pixel,
    ).to_fits(relax=True)
    hdulist[0].header.extend(hdr0)
    return hdulist


def create_nirda_v0_1_0_wcs():
    hdr0 = fits.Header(
        [
            ("TELESCOP", "NASA Pandora", "telescope"),
            ("CAMERAID", "H2rgCam", "ID of camera used in acquisition"),
            ("INSTRMNT", "NIRDA", "instrument"),
            (
                "CREATOR",
                "Pandora DPC Software",
                "Software that created this file",
            ),
            (
                "AUTHOR",
                "Christina Hedges",
                "Person or group that created this file",
            ),
            ("DATASRC", "SIMULATION", ""),
            ("VERSION", "v0.1.0", "creator software version"),
            ("DATE", Time.now().isot, "creation date"),
        ]
    )
    hdulist = create_wcs(
        target_ra=0,
        target_dec=0,
        theta=0,
        naxis1=2048,
        naxis2=2048,
        crpix1=2008,
        crpix2=1024,
        pixel_scale=1.19 * u.arcsecond / u.pixel,
    ).to_fits(relax=True)
    hdulist[0].header.extend(hdr0)
    return hdulist


def create_visda_v0_1_0_sip():
    X, Y, Xp, Yp = _read_distortion_file(
        pixel_size=6.5 * u.micron / u.pixel,
        distortion_file=f"{PACKAGEDIR}/data/external/fov_distortion.csv",
    )

    sip = create_sip(X, Y, Xp, Yp, crpix1=1024, crpix2=1024, order=3)
    wcs = WCS()
    wcs.wcs.ctype = ["RA---TAN-SIP", "DEC--TAN-SIP"]
    hdr0 = wcs.to_fits(relax=True)[0].header
    wcs.sip = sip
    hdulist = wcs.to_fits(relax=True)
    # pop out bad headers
    _ = [hdulist[0].header.pop(c) for c in list(hdr0.keys())[2:]]

    hdr0 = fits.Header(
        [
            ("TELESCOP", "NASA Pandora", "telescope"),
            ("CAMERAID", "PcoCam", "ID of camera used in acquisition"),
            ("INSTRMNT", "VISDA", "instrument"),
            (
                "CREATOR",
                "Pandora DPC Software",
                "Software that created this file",
            ),
            (
                "AUTHOR",
                "Christina Hedges",
                "Person or group that created this file",
            ),
            ("DATASRC", "SIMULATION", ""),
            ("VERSION", "v0.1.0", "creator software version"),
            ("CRPIX1", 1024, "reference pixel in column"),
            ("CRPIX2", 1024, "reference pixel in row"),
            ("DATE", Time.now().isot, "creation date"),
        ]
    )
    # add new headers
    hdulist[0].header.extend(hdr0)
    return hdulist


def create_nirda_dummy_qe():
    wavelength = np.linspace(0.5, 3, 1000) * u.micron
    wavelength = np.atleast_1d(wavelength)
    sw_coeffs = np.array([0.65830, -0.05668, 0.25580, -0.08350])
    sw_exponential = 100.0
    sw_wavecut_red = 1.69  # changed from 2.38 for Pandora
    sw_wavecut_blue = 0.85  # new for Pandora
    with np.errstate(invalid="ignore", over="ignore"):
        sw_qe = (
            sw_coeffs[0]
            + sw_coeffs[1] * wavelength.to(u.micron).value
            + sw_coeffs[2] * wavelength.to(u.micron).value ** 2
            + sw_coeffs[3] * wavelength.to(u.micron).value ** 3
        )

        sw_qe = np.where(
            wavelength.to(u.micron).value > sw_wavecut_red,
            sw_qe
            * np.exp(
                (sw_wavecut_red - wavelength.to(u.micron).value)
                * sw_exponential
            ),
            sw_qe,
        )

        sw_qe = np.where(
            wavelength.to(u.micron).value < sw_wavecut_blue,
            sw_qe
            * np.exp(
                -(sw_wavecut_blue - wavelength.to(u.micron).value)
                * (sw_exponential / 1.5)
            ),
            sw_qe,
        )
    sw_qe[sw_qe < 1e-5] = 0
    hdr0 = fits.Header(
        [
            ("TELESCOP", "NASA Pandora", "telescope"),
            ("CAMERAID", "H2rgCam", "ID of camera used in acquisition"),
            ("INSTRMNT", "NIRDA", "instrument"),
            (
                "CREATOR",
                "Pandora DPC Software",
                "Software that created this file",
            ),
            (
                "AUTHOR",
                "Christina Hedges",
                "Person or group that created this file",
            ),
            ("DATASRC", "THEORETICAL", ""),
            ("VERSION", "v0.1.0", "creator software version"),
            ("DATE", Time.now().isot, "creation date"),
        ]
    )

    hdr1 = fits.Header(
        [
            ("EXTNAME", "QUANTUM EFFICIENCY", "name of extension"),
        ]
    )
    hdulist = fits.HDUList(
        [
            fits.PrimaryHDU(header=hdr0),
            fits.TableHDU.from_columns(
                [
                    fits.Column(
                        name="Wavelength",
                        array=wavelength.value,
                        format="E",
                        unit="micron",
                    ),
                    fits.Column(
                        name="QE",
                        array=sw_qe,
                        unit="electron / photon",
                        format="E",
                    ),
                ],
                header=hdr1,
            ),
        ]
    )
    return hdulist


def create_nirda_v0_1_0_sip():
    X, Y, Xp, Yp = _read_distortion_file(
        pixel_size=18 * u.micron / u.pixel,
        distortion_file=f"{PACKAGEDIR}/data/external/fov_distortion.csv",
    )

    sip = create_sip(X, Y, Xp, Yp, crpix1=2008, crpix2=1024, order=3)
    wcs = WCS()
    wcs.wcs.ctype = ["RA---TAN-SIP", "DEC--TAN-SIP"]
    hdr0 = wcs.to_fits(relax=True)[0].header
    wcs.sip = sip
    hdulist = wcs.to_fits(relax=True)
    # pop out bad headers
    _ = [hdulist[0].header.pop(c) for c in list(hdr0.keys())[2:]]

    hdr0 = fits.Header(
        [
            ("TELESCOP", "NASA Pandora", "telescope"),
            ("CAMERAID", "H2rgCam", "ID of camera used in acquisition"),
            ("INSTRMNT", "NIRDA", "instrument"),
            (
                "CREATOR",
                "Pandora DPC Software",
                "Software that created this file",
            ),
            (
                "AUTHOR",
                "Christina Hedges",
                "Person or group that created this file",
            ),
            ("DATASRC", "SIMULATION", ""),
            ("VERSION", "v0.1.0", "creator software version"),
            ("CRPIX1", 2008, "reference pixel in column"),
            ("CRPIX2", 1024, "reference pixel in row"),
            ("DATE", Time.now().isot, "creation date"),
        ]
    )
    # add new headers
    hdulist[0].header.extend(hdr0)
    return hdulist


def create_dummy_reference_products(overwrite=True):
    """Populate this package with dummy reference files."""

    # VISDA
    hdulist = create_visda_dummy_flat()
    hdulist.writeto(f"{PACKAGEDIR}/data/visda/flat.fits", overwrite=overwrite)
    hdulist = create_visda_dummy_bias()
    hdulist.writeto(f"{PACKAGEDIR}/data/visda/bias.fits", overwrite=overwrite)
    hdulist = create_visda_dummy_dark()
    hdulist.writeto(f"{PACKAGEDIR}/data/visda/dark.fits", overwrite=overwrite)
    hdulist = create_visda_dummy_gain()
    hdulist.writeto(f"{PACKAGEDIR}/data/visda/gain.fits", overwrite=overwrite)
    hdulist = create_visda_dummy_read_noise()
    hdulist.writeto(
        f"{PACKAGEDIR}/data/visda/readnoise.fits", overwrite=overwrite
    )
    hdulist = create_visda_dummy_bad_pixel_map()
    hdulist.writeto(
        f"{PACKAGEDIR}/data/visda/badpix.fits", overwrite=overwrite
    )
    hdulist = create_visda_dummy_non_linearity()
    hdulist.writeto(
        f"{PACKAGEDIR}/data/visda/nonlin.fits", overwrite=overwrite
    )
    hdulist = create_visda_v0_1_0_sip()
    hdulist.writeto(f"{PACKAGEDIR}/data/visda/sip.fits", overwrite=overwrite)
    hdulist = create_visda_v0_1_0_wcs()
    hdulist.writeto(f"{PACKAGEDIR}/data/visda/wcs.fits", overwrite=overwrite)

    # NIRDA
    hdulist = create_nirda_dummy_flat()
    hdulist.writeto(f"{PACKAGEDIR}/data/nirda/flat.fits", overwrite=overwrite)
    hdulist = create_nirda_dummy_bias()
    hdulist.writeto(f"{PACKAGEDIR}/data/nirda/bias.fits", overwrite=overwrite)
    hdulist = create_nirda_dummy_dark()
    hdulist.writeto(f"{PACKAGEDIR}/data/nirda/dark.fits", overwrite=overwrite)
    hdulist = create_nirda_dummy_gain()
    hdulist.writeto(f"{PACKAGEDIR}/data/nirda/gain.fits", overwrite=overwrite)
    hdulist = create_nirda_dummy_read_noise()
    hdulist.writeto(
        f"{PACKAGEDIR}/data/nirda/readnoise.fits", overwrite=overwrite
    )
    hdulist = create_nirda_dummy_bad_pixel_map()
    hdulist.writeto(
        f"{PACKAGEDIR}/data/nirda/badpix.fits", overwrite=overwrite
    )
    hdulist = create_nirda_dummy_non_linearity()
    hdulist.writeto(
        f"{PACKAGEDIR}/data/nirda/nonlin.fits", overwrite=overwrite
    )
    hdulist = create_nirda_v0_1_0_sip()
    hdulist.writeto(f"{PACKAGEDIR}/data/nirda/sip.fits", overwrite=overwrite)
    hdulist = create_nirda_v0_1_0_wcs()
    hdulist.writeto(f"{PACKAGEDIR}/data/nirda/wcs.fits", overwrite=overwrite)
    hdulist = create_nirda_dummy_qe()
    hdulist.writeto(f"{PACKAGEDIR}/data/nirda/qe.fits", overwrite=overwrite)
