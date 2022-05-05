"""

"""

from abc import ABC, abstractmethod
from typing import Optional

from gen_doc.models import ParsedDocString


class PythonDocStringParser(ABC):
    """
    Base class for all parsers
    """

    @property
    def example(self) -> str:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def parse(doc_string: Optional[str]) -> Optional[ParsedDocString]:
        """
        Method to parse a Python doc string
        :param doc_string: extracted doc string
        :type doc_string: Optional[str]
        :return: parsed object
        :rtype: Optional[ParsedDocString]
        """
        raise NotImplementedError
