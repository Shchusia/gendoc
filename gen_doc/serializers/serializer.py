"""
base class for serializers
"""
from abc import ABC, abstractmethod
from logging import Logger, getLogger
from typing import List, Optional

from gen_doc.models import Module


class Serializer(ABC):
    """
    Base class for serializers
    """

    def __init__(
        self, language: Optional[str] = "python", logger: Optional[Logger] = None
    ):
        self._logger = logger or getLogger(__name__)
        self._language = language

    @abstractmethod
    def serialize(self, module: Module) -> List[str]:
        """
        Main function to serialize module
        :param Module module: parsed module to convert
        :return: list of markups string
        """
        raise NotImplementedError

    @property
    def suffix_file(self) -> str:
        """
        File type for which this serializer is intended
        :return: ".type"
        """
        raise NotImplementedError
