"""
Main module with class for working with catalog
"""
# pylint: disable=too-many-arguments
import os
from abc import ABC, abstractmethod
from collections import Iterable
from distutils.util import strtobool
from logging import Logger, getLogger
from pathlib import Path
from typing import List, Optional, Tuple, Union

from .models import GeneralInfo
from .settings import DEFAULT_SUFFIX  # noqa


class DocGenerator(ABC):
    """
    Class for generating project documentation
    """

    def __init__(
        self,
        logger: Optional[Logger] = None,
        path_to_root_folder: Optional[Union[Path, str]] = None,
        extract_with_same_hierarchy: Optional[bool] = True,
        overwrite_if_file_exists: Optional[bool] = False,
        path_to_save: Optional[Path] = None,
        file_to_save: Optional[str] = None,
        save_mode: Optional[str] = "md",
        title: Optional[str] = None,
        repository_main_url: Optional[str] = None,
        author: Optional[str] = None,
        author_contacts: Optional[List[str]] = None,
        release: Optional[str] = None,
        additional_files_to_ignore: Optional[List[str]] = None,
        additional_folders_to_ignore: Optional[List[str]] = None,
    ):

        self._logger = logger or getLogger(__name__)
        if not path_to_root_folder:
            path_to_root_folder = "./"
        if isinstance(path_to_root_folder, str):
            path_to_root_folder = Path(path_to_root_folder)

        self._root_folder = path_to_root_folder
        self._save_mode = save_mode
        self._extract_with_same_hierarchy = strtobool(str(extract_with_same_hierarchy))
        self._overwrite_if_file_exists = strtobool(str(overwrite_if_file_exists))
        self.general_info = GeneralInfo(
            title=title,
            author=author,
            author_contacts=author_contacts,
            release=release,
            repository_main_url=repository_main_url,
        )

        if not file_to_save:
            self._file_to_save = self._root_folder.absolute().name + DEFAULT_SUFFIX
        if not path_to_save:
            self._path_to_save = self._root_folder.absolute() / Path(
                self._root_folder.absolute().name + DEFAULT_SUFFIX
            )
            self._path_to_save.mkdir(exist_ok=True, parents=True)
        if not additional_files_to_ignore or not isinstance(
            additional_files_to_ignore, Iterable
        ):
            additional_files_to_ignore = list()  # type: List[str] # type: ignore # noqa
        if not additional_folders_to_ignore or not isinstance(
            additional_folders_to_ignore, Iterable
        ):
            additional_folders_to_ignore = (
                list()
            )  # type: List[str] # type: ignore # noqa

        self._additional_folders_to_ignore = additional_folders_to_ignore
        self._additional_files_to_ignore = additional_files_to_ignore

        self._logger.debug("Path to folder: %s", self._root_folder)

    @property
    def short_name(self) -> str:
        """
        Property for short name in commands
        :return: str short name
        :rtype: str
        :example:
        >>> short_name = "py"  # for python
        """
        raise NotImplementedError

    @property
    def types_of_file_to_process(self) -> List[str]:
        """
        Property for concrete language
        type of documents for which to create documentation
        :return: is list of string types to build docs
        :rtype: List[str]
        :example:
        >>> types_of_file_to_process = ['.py']  # for python
        """
        raise NotImplementedError

    @property
    def files_to_ignore(self):
        """
        Which files names will not be considered
        :return: list of files that should not be processed
        :rtype: List[str]
        :example:
        >>> files_to_ignore = ['setup.py'] # for python
        """
        raise NotImplementedError

    @property
    def folders_to_ignore(self):
        """Which folder names will not be considered
        :return: list of folders that should not be processed
        :rtype: List[str]
        :example:
        >>> folders_to_ignore = ['__pycache__'] # for python
        """
        raise NotImplementedError

    @abstractmethod
    def build_documentation_file(self, path_to_file: Path, deep: int = 1) -> List[str]:
        """Method to overwriting in sub class for concrete ProgramLanguage
        :param Path path_to_file: file for which build documentation
        :param int optional int deep: at what nesting level is the file
        :return: list[str] docs
        """
        raise NotImplementedError

    def build_documentation(self) -> None:
        """
        Main function in build documentation
        :return: Path to doc file or root documentation folder
        :rtype: Path
        """

        # list_documentation_data = list()  # type: List[Any]
        list_folders_with_files_to_parse = [
            (Path(dir_path), file_names)
            for (dir_path, dir_names, file_names) in os.walk(self._root_folder)
            if file_names
        ]  # type: List[Tuple[Path, List[str]]]
        self._logger.debug(list_folders_with_files_to_parse)
        _current_files_to_ignore = [
            *self.files_to_ignore,
            *self._additional_files_to_ignore,
        ]
        _current_folders_to_ignore = [
            *self.folders_to_ignore,
            *self._additional_folders_to_ignore,
        ]
        for folder_path, list_files in list_folders_with_files_to_parse:
            if not self._extract_with_same_hierarchy:
                deep = len(
                    str(folder_path)[len(str(self._root_folder)) :].split(os.sep)
                )
            else:
                deep = 1
            if folder_path.name in _current_folders_to_ignore:
                continue
            for file in list_files:
                if file in _current_files_to_ignore:
                    continue
                file_path = Path(file)
                if file_path.suffix not in self.types_of_file_to_process:
                    continue
                self.build_documentation_file(
                    path_to_file=folder_path / file_path, deep=deep
                )
