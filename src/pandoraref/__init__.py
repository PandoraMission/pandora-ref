# Standard library
import logging  # noqa: E402
import os  # noqa

# Third-party
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
from .ref import *  # noqa
