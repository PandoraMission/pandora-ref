# Standard library
import inspect  # noqa
import logging  # noqa: E402
import os  # noqa

# Third-party
import numpy as np  # noqa
import pandas as pd  # noqa
from astropy.io import fits  # noqa
from astropy.time import Time  # noqa
from rich.console import Console  # noqa: E402
from rich.logging import RichHandler  # noqa: E402

PACKAGEDIR = os.path.abspath(os.path.dirname(__file__))
TESTDIR = "/".join(PACKAGEDIR.split("/")[:-2]) + "/tests/"

# Standard library
from importlib.metadata import PackageNotFoundError, version  # noqa


def get_version():
    try:
        return version("pandoraref")
    except PackageNotFoundError:
        return "unknown"


__version__ = get_version()


# Custom Logger with Rich
class PandoraLogger(logging.Logger):
    def __init__(self, name, level=logging.INFO):
        super().__init__(name, level)
        console = Console()
        self.handler = RichHandler(
            show_time=False, show_level=False, show_path=False, console=console
        )
        self.handler.setFormatter(
            logging.Formatter(
                "%(asctime)s %(levelname)s: %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )
        )
        self.addHandler(self.handler)


def get_logger(name="pandoraref"):
    """Configure and return a logger with RichHandler."""
    return PandoraLogger(name)


logger = get_logger("pandoraref")

from .dummy import create_dummy_reference_products  # noqa
from .ref import NIRDAReference, VISDAReference  # noqa


def get_file_info():
    """Get a table of file info"""

    def human_size(size):
        for unit in ["B", "KB", "MB", "GB", "TB"]:
            if size < 1024:
                return f"{size:.2f} {unit}"
            size /= 1024

    dfs = []
    for name, Ref in zip(["NIRDA", "VISDA"], [NIRDAReference, VISDAReference]):
        keys = np.sort(
            [
                name
                for name, value in inspect.getmembers(Ref)
                if not name.startswith("__") and not inspect.isroutine(value)
            ]
        )
        obj = Ref()
        for key in keys:
            if key.endswith("_file"):
                fname = getattr(obj, key)
                if not os.path.isfile(getattr(obj, key)):
                    raise ValueError
                with fits.open(getattr(obj, key)) as hdulist:
                    hdr = hdulist[0].header
                    version = hdr["VERSION"] if "VERSION" in hdr else "-"
                    src = hdr["DATASRC"] if "DATASRC" in hdr else "-"
                    creator = hdr["CREATOR"] if "CREATOR" in hdr else "-"
                    author = hdr["AUTHOR"] if "AUTHOR" in hdr else "-"
                    date = (
                        Time(hdr["DATE"]).isot[:10] if "DATE" in hdr else "-"
                    )
                    size = human_size(os.path.getsize(fname))
                    instrument = hdr["INSTRMNT"] if "INSTRMNT" in hdr else "-"
                dfs.append(
                    pd.DataFrame(
                        np.vstack(
                            [
                                instrument,
                                key,
                                version,
                                src,
                                creator,
                                author,
                                date,
                                size,
                            ]
                        ).T,
                        columns=[
                            "Instrument",
                            "File Name",
                            "File Version",
                            "File Source",
                            "File Creator",
                            "File Author",
                            "File Date",
                            "File Size",
                        ],
                    )
                )
    df = pd.concat(dfs).reset_index(drop=True)
    return df
