"""
Settings for work lib
"""
# pylint: disable=invalid-name
import logging
from enum import Enum

logging.basicConfig(encoding="utf-8", level=logging.DEBUG)  # type: ignore # noqa


class AllowedSaveModes(Enum):
    """
    mods for save documentations
    """

    html = ".html"
    md = ".md"


DEFAULT_SUFFIX = "_doc"


if __name__ == "__main__":
    print(AllowedSaveModes[".md"].value)
