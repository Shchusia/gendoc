"""
base class for serializers
"""
from abc import ABC, abstractmethod
from logging import Logger, getLogger
from typing import List, Optional

from gendoc.models import Module


class Serializer(ABC):
    def __init__(
        self, language: Optional[str] = "python", logger: Optional[Logger] = None
    ):
        self._logger = logger or getLogger(__name__)
        self._language = language

    @abstractmethod
    def serialize(self, module: Module) -> List[str]:
        """

        :param module:
        :return:
        """
        raise NotImplementedError

    @property
    def suffix_file(self) -> str:
        raise NotImplementedError
