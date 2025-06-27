"""Module for making dummy files. Use these as a way to set expectations for how files should be structured, if you have no other option."""

# Third-party
import numpy as np
import pandorasat as ps
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
            ("CREATOR", "Pandora DPC", "creator of this product"),
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
            ("CREATOR", "Pandora DPC", "creator of this product"),
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
            ("CREATOR", "Pandora DPC", "creator of this product"),
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
            ("CREATOR", "Pandora DPC", "creator of this product"),
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
    bias = np.ones((2048, 2048), dtype=np.int16)

    hdr0 = fits.Header(
        [
            ("TELESCOP", "NASA Pandora", "telescope"),
            ("CAMERAID", "PcoCam", "ID of camera used in acquisition"),
            ("INSTRMNT", "VISDA", "instrument"),
            ("CREATOR", "Pandora DPC", "creator of this product"),
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
        ]
    )
    hdulist = fits.HDUList(
        [fits.PrimaryHDU(header=hdr0), fits.CompImageHDU(bias, header=hdr1)]
    )
    return hdulist


def create_nirda_dummy_bias():
    """Creates a dummy file that is a placeholder for a bias on the VISDA."""
    bias = np.ones((2048, 2048), dtype=np.int16)

    hdr0 = fits.Header(
        [
            ("TELESCOP", "NASA Pandora", "telescope"),
            ("CAMERAID", "H2rgCam", "ID of camera used in acquisition"),
            ("INSTRMNT", "NIRDA", "instrument"),
            ("CREATOR", "Pandora DPC", "creator of this product"),
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
        ]
    )
    hdulist = fits.HDUList(
        [fits.PrimaryHDU(header=hdr0), fits.CompImageHDU(bias, header=hdr1)]
    )
    return hdulist


def create_visda_dummy_dark():
    """Creates a dummy file that is a placeholder for a dark on the VISDA."""
    dark = np.zeros((2048, 2048), dtype=np.int16)

    hdr0 = fits.Header(
        [
            ("TELESCOP", "NASA Pandora", "telescope"),
            ("CAMERAID", "PcoCam", "ID of camera used in acquisition"),
            ("INSTRMNT", "VISDA", "instrument"),
            ("CREATOR", "Pandora DPC", "creator of this product"),
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
            ("EXTNAME", "dark", "name of extension"),
        ]
    )
    hdulist = fits.HDUList(
        [fits.PrimaryHDU(header=hdr0), fits.CompImageHDU(dark, header=hdr1)]
    )
    return hdulist


def create_nirda_dummy_dark():
    """Creates a dummy file that is a placeholder for a dark on the VISDA."""
    dark = np.zeros((2048, 2048), dtype=np.int16)

    hdr0 = fits.Header(
        [
            ("TELESCOP", "NASA Pandora", "telescope"),
            ("CAMERAID", "H2rgCam", "ID of camera used in acquisition"),
            ("INSTRMNT", "NIRDA", "instrument"),
            ("CREATOR", "Pandora DPC", "creator of this product"),
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
            ("EXTNAME", "DARK", "name of extension"),
        ]
    )
    hdulist = fits.HDUList(
        [fits.PrimaryHDU(header=hdr0), fits.CompImageHDU(dark, header=hdr1)]
    )
    return hdulist


def create_visda_dummy_gain():
    """Creates a dummy file that is a placeholder for a dark on the VISDA."""
    hdr0 = fits.Header(
        [
            ("TELESCOP", "NASA Pandora", "telescope"),
            ("CAMERAID", "PcoCam", "ID of camera used in acquisition"),
            ("INSTRMNT", "VISDA", "instrument"),
            ("CREATOR", "Pandora DPC", "creator of this product"),
            ("VERSION", "dummy", "creator software version"),
            ("DATE", Time.now().isot, "creation date"),
            ("GAIN", 1, "gain setting in electron/ADU"),
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
            ("CREATOR", "Pandora DPC", "creator of this product"),
            ("VERSION", "dummy", "creator software version"),
            ("DATE", Time.now().isot, "creation date"),
            ("GAIN", 1, "gain setting in electron/ADU"),
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
            ("CREATOR", "Pandora DPC", "creator of this product"),
            ("VERSION", "dummy", "creator software version"),
            ("DATE", Time.now().isot, "creation date"),
            ("READNS", 0, "read noise in electrons"),
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
            ("CREATOR", "Pandora DPC", "creator of this product"),
            ("VERSION", "dummy", "creator software version"),
            ("DATE", Time.now().isot, "creation date"),
            ("READNS", 0, "read noise in electrons"),
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
            ("CREATOR", "Pandora DPC", "creator of this product"),
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
            ("CREATOR", "Pandora DPC", "creator of this product"),
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
    detector = ps.VisibleDetector()

    hdr0 = fits.Header(
        [
            ("TELESCOP", "NASA Pandora", "telescope"),
            ("CAMERAID", "PcoCam", "ID of camera used in acquisition"),
            ("INSTRMNT", "VISDA", "instrument"),
            ("CREATOR", "Pandora DPC", "creator of this product"),
            ("VERSION", "v.0.1.0", "creator software version"),
            ("DATE", Time.now().isot, "creation date"),
        ]
    )

    hdulist = create_wcs(detector, 0, 0, 0, crpix1=1024, crpix2=1024).to_fits(
        relax=True
    )
    hdulist[0].header.extend(hdr0)
    return hdulist


def create_nirda_v0_1_0_wcs():
    detector = ps.NIRDetector()

    hdr0 = fits.Header(
        [
            ("TELESCOP", "NASA Pandora", "telescope"),
            ("CAMERAID", "H2rgCam", "ID of camera used in acquisition"),
            ("INSTRMNT", "NIRDA", "instrument"),
            ("CREATOR", "Pandora DPC", "creator of this product"),
            ("VERSION", "dummy", "creator software version"),
            ("DATE", Time.now().isot, "creation date"),
        ]
    )
    hdulist = create_wcs(detector, 0, 0, 0, crpix1=1024, crpix2=1024).to_fits(
        relax=True
    )
    hdulist[0].header.extend(hdr0)
    return hdulist


def create_visda_v0_1_0_sip():
    detector = ps.VisibleDetector()
    X, Y, Xp, Yp = _read_distortion_file(
        detector,
        f"{PACKAGEDIR}/data/external/fov_distortion.csv",
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
            ("CREATOR", "Pandora DPC", "creator of this product"),
            ("VERSION", "v0.1.0", "creator software version"),
            ("CRPIX1", 1024, "reference pixel in column"),
            ("CRPIX2", 1024, "reference pixel in row"),
            ("DATE", Time.now().isot, "creation date"),
        ]
    )
    # add new headers
    hdulist[0].header.extend(hdr0)
    return hdulist


def create_nirda_v0_1_0_sip():
    detector = ps.NIRDetector()
    X, Y, Xp, Yp = _read_distortion_file(
        detector,
        f"{PACKAGEDIR}/data/external/fov_distortion.csv",
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
            ("CAMERAID", "H2rgCam", "ID of camera used in acquisition"),
            ("INSTRMNT", "NIRDA", "instrument"),
            ("CREATOR", "Pandora DPC", "creator of this product"),
            ("VERSION", "v0.1.0", "creator software version"),
            ("CRPIX1", 1024, "reference pixel in column"),
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
