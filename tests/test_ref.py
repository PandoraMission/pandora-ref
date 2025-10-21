# Standard library
import inspect
import os

# Third-party
import astropy.units as u
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS, Sip

# First-party/Local
from pandoraref import NIRDAReference, VISDAReference


def test_path_objects():
    """Test we can get all the path back and they all point to fits files"""
    for name, Ref in zip(["NIRDA", "VISDA"], [NIRDAReference, VISDAReference]):
        keys = [
            name
            for name, value in inspect.getmembers(Ref)
            if not name.startswith("__") and not inspect.isroutine(value)
        ]
        obj = Ref()
        for key in keys:
            if key.endswith("_file"):
                assert os.path.isfile(getattr(obj, key))
                if getattr(obj, key).endswith(".fits"):
                    with fits.open(getattr(obj, key)) as hdulist:
                        assert hdulist[0].header["VERSION"] != ""
                        assert hdulist[0].header["INSTRMNT"] == name
    return


def test_get_wcs():
    """Test the wcs getting"""
    for name, Ref in zip(["NIRDA", "VISDA"], [NIRDAReference, VISDAReference]):
        obj = Ref()
        wcs = obj.get_wcs()
        assert isinstance(wcs, WCS)


def test_get_sip():
    """Test the wcs getting"""
    for name, Ref in zip(["NIRDA", "VISDA"], [NIRDAReference, VISDAReference]):
        obj = Ref()
        sip = obj.get_sip()
        assert isinstance(sip, Sip)


def test_get_sensitivity():
    """Test the wcs getting"""
    for name, Ref in zip(["NIRDA", "VISDA"], [NIRDAReference, VISDAReference]):
        obj = Ref()
        wavelength = np.arange(0.1, 3) * u.micron
        sens = obj.get_sensitivity(wavelength)
        assert isinstance(sens, u.Quantity)
        assert len(sens) == len(wavelength)
        wavelength = np.arange(100, 3000) * u.nm
        sens = obj.get_sensitivity(wavelength)

    assert (
        NIRDAReference().get_sensitivity(1.5 * u.micron)
        > 6e14 * u.cm**2 * u.electron / u.erg
    )


def test_get_pixel_position():
    """Test the wcs getting"""
    obj = NIRDAReference()
    wavelength = np.arange(0.1, 3) * u.micron
    pixel = obj.get_pixel_position(wavelength)
    assert isinstance(pixel, u.Quantity)
    assert len(pixel) == len(wavelength)


def test_get_spectrum_normalization():
    """Test the wcs getting"""
    obj = NIRDAReference()
    wavelength = np.arange(0.1, 3) * u.micron
    sens = obj.get_spectrum_normalization_per_wavelength(wavelength)
    assert isinstance(sens, u.Quantity)
    assert len(sens) == len(wavelength)
    assert sens.unit.is_equivalent("cm2 electron / erg")

    pixel = np.arange(-200, 200) * u.pixel
    sens = obj.get_spectrum_normalization_per_pixel(pixel)
    assert isinstance(sens, u.Quantity)
    assert len(sens) == len(pixel)
    assert sens.unit.is_equivalent("cm2 Angstrom electron / (erg pix)")


def test_vega():
    obj = NIRDAReference()
    w, s = obj._get_vega_data()
    assert isinstance(w, u.Quantity)
    assert isinstance(s, u.Quantity)
