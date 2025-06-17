"""Tools to make SIP and WCS files"""

# Third-party
import astropy.units as u
import numpy as np
import numpy.typing as npt
import pandas as pd
from astropy.io import fits
from astropy.wcs import WCS, Sip


def create_sip(
    X: npt.NDArray,
    Y: npt.NDArray,
    Xp: npt.NDArray,
    Yp: npt.NDArray,
    crpix1: float,
    crpix2: float,
    order: int = 3,
) -> Sip:
    """Helper function to make a Sip object from arrays of input pixel positions and focal plane positions.

    See https://fits.gsfc.nasa.gov/registry/sip/SIP_distortion_v1_0.pdf for more information

    The inputs must be a completely "square" grid of pixels
    "X" and "Y", and a corresponding set of distorted pixel positions
    "Xp" and "Yp". These should be centered on CRPIX1 and CRPIX2.

    Parameters:
    -----------
    X : np.ndarray
        X (column) pixel positions in undistorted frame, centered around CRPIX1
    Y : np.ndarray
        Y (row) pixel positions in undistorted frame, centered around CRPIX2
    Xp : np.ndarray
        X (column) pixel positions in distorted frame, centered around CRPIX1
    Yp : np.ndarray
        Y (row) pixel positions in distorted frame, centered around CRPIX2
    crpix1: float
        CRPIX1 value
    crpix2: float
        CRPIX2 value
    order: int
        Polynomial order for the distortion model

    Returns:
    --------
    sip: astropy.wcs.Sip
        astropy SIP object
    """

    M = np.vstack(
        [
            X.ravel() ** idx * Y.ravel() ** jdx
            for idx in range(order + 1)
            for jdx in range(order + 1)
        ]
    ).T

    coeffs = [
        np.linalg.solve(M.T.dot(M), M.T.dot(-(X - Xp).ravel())).reshape(
            (order + 1, order + 1)
        ),
        np.linalg.solve(M.T.dot(M), M.T.dot(-(Y - Yp).ravel())).reshape(
            (order + 1, order + 1)
        ),
    ]
    coeffsP = [
        np.linalg.solve(M.T.dot(M), M.T.dot((X - Xp).ravel())).reshape(
            (order + 1, order + 1)
        ),
        np.linalg.solve(M.T.dot(M), M.T.dot((Y - Yp).ravel())).reshape(
            (order + 1, order + 1)
        ),
    ]

    # Build a SIP object
    sip = Sip(
        coeffs[0],
        coeffs[1],
        coeffsP[0],
        coeffsP[1],
        (crpix1, crpix2),
    )

    # Check that the new correction distorts correctly

    # True pixel positions
    pix = np.vstack([X.ravel(), Y.ravel()]).T + np.asarray([crpix1, crpix2])
    if not np.all(
        np.hypot(
            *(np.vstack([Xp.ravel(), Yp.ravel()]) - sip.pix2foc(pix, 1).T)
        )
        < 0.1
    ):
        raise ValueError("WCS SIP does not produce expected pixel distortion")
    # Check that the new correction goes back to original coordinates correctly
    if not np.all(
        np.hypot(*(pix.T - sip.foc2pix(sip.pix2foc(pix, 1), 1).T)) < 0.1
    ):
        raise ValueError("WCS SIP does not invert precisely")
    return sip


def create_wcs(
    detector,
    target_ra: u.Quantity,
    target_dec: u.Quantity,
    theta: u.Quantity = 0 * u.deg,
    crpix1: int = None,
    crpix2: int = None,
    xreflect: bool = True,
    yreflect: bool = False,
) -> WCS.wcs:
    """Get the World Coordinate System for a detector

    Parameters:
    -----------
    detector : pandorasim.Detector
        The detector to build the WCS for
    target_ra: astropy.units.Quantity
        The target RA in degrees
    target_dec: astropy.units.Quantity
        The target Dec in degrees
    theta: astropy.units.Quantity
        The observatory angle in degrees
    crpix1: int
        Reference pixel in column
    crpix2: int
        Reference pixel in row
    xreflect: bool
        Whether to reflect in the x (column) direction
    yreflect: bool
        Whether to reflect in the y (column) direction
    """
    if isinstance(target_ra, (np.ndarray, float, int)):
        target_ra = u.Quantity(target_ra, "deg")
    if isinstance(target_dec, (np.ndarray, float, int)):
        target_dec = u.Quantity(target_dec, "deg")
    if isinstance(theta, (np.ndarray, float, int)):
        theta = u.Quantity(theta, "deg")
    hdu = fits.PrimaryHDU()
    hdu.header["CTYPE1"] = "RA---TAN"
    hdu.header["CTYPE2"] = "DEC--TAN"
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
    hdu.header["CRPIX1"] = (
        detector.naxis1.value // 2 if crpix1 is None else crpix1
    )
    hdu.header["CRPIX2"] = (
        detector.naxis2.value // 2 if crpix2 is None else crpix2
    )

    hdu.header["NAXIS1"] = detector.naxis1.value
    hdu.header["NAXIS2"] = detector.naxis2.value
    hdu.header["CDELT1"] = detector.pixel_scale.to(u.deg / u.pixel).value * (
        -1
    ) ** (int(xreflect))
    hdu.header["CDELT2"] = detector.pixel_scale.to(u.deg / u.pixel).value * (
        -1
    ) ** (int(yreflect))

    wcs = WCS(hdu.header, relax=True)
    return wcs


def _read_distortion_file(detector, distortion_file: str):
    """Helper function to read a distortion file from LLNL

    This file must be a CSV file that contains a completely "square" grid of pixels
    "Parax X" and "Parax Y", and a corresponding set of distorted pixel positions
    "Real X" and "Real Y". These should be centered CRPIX1 and CRPIX2.

    Parameters:
    -----------
    distortion_file: str
        File path to a distortion CSV file.

    Returns:
    --------
    X : np.ndarray
        X pixel positions in undistorted frame, centered around CRPIX1
    Y : np.ndarray
        Y pixel positions in undistorted frame, centered around CRPIX2
    Xp : np.ndarray
        X pixel positions in distorted frame, centered around CRPIX1
    Yp : np.ndarray
        Y pixel positions in distorted frame, centered around CRPIX2
    """
    df = pd.read_csv(distortion_file)
    # Square grid of pixels (TRUTH)
    X = (
        (u.Quantity(np.asarray(df["Parax X"]), "mm") / detector.pixel_size)
        .to(u.pix)
        .value
    )
    Y = (
        (u.Quantity(np.asarray(df["Parax Y"]), "mm") / detector.pixel_size)
        .to(u.pix)
        .value
    )
    # Distorted pixel positions (DISTORTED)
    Xp = (
        (u.Quantity(np.asarray(df["Real X"]), "mm") / detector.pixel_size)
        .to(u.pix)
        .value
    )
    Yp = (
        (u.Quantity(np.asarray(df["Real Y"]), "mm") / detector.pixel_size)
        .to(u.pix)
        .value
    )
    return X, Y, Xp, Yp
