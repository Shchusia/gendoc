"""
Settings for work lib
"""
# pylint: disable=invalid-name
import logging
from enum import Enum

from gen_doc.serializers import MarkdownSerializer

logging.basicConfig(encoding="utf-8", level=logging.INFO)  # type: ignore # noqa


class AllowedSaveModes(Enum):
    """
    mods for save documentations
    """

    # html = ".html"
    md = MarkdownSerializer


DEFAULT_SUFFIX = "_doc"
