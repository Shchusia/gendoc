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

from .models import GeneralInfo, Module
from .serializers.serializer import Serializer
from .settings import DEFAULT_SUFFIX, AllowedSaveModes


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
        file_to_save: Optional[Union[str, Path]] = None,
        save_mode: Optional[str] = "md",
        title: Optional[str] = None,
        repository_main_url: Optional[str] = None,
        author: Optional[str] = None,
        author_contacts: Optional[List[str]] = None,
        release: Optional[str] = None,
        additional_files_to_ignore: Optional[List[str]] = None,
        additional_folders_to_ignore: Optional[List[str]] = None,
    ):
        """
        Init config loader
        :param logger:
        :param path_to_root_folder: path to the directory for which
         documentation should be compiled
        :param extract_with_same_hierarchy: if False extract all to one file
         if True create file for every file'
        :param overwrite_if_file_exists: for overwriting if file exist
        :param path_to_save: path to the directory where to save docs
        :param file_to_save: name_file to save
        :param save_mode: save mode
        :param title: title for header
        :param repository_main_url: url of the repository where this project
         is located
        :param author: author of the documented project
        :param author_contacts: contacts author
        :param release: release project
        :param additional_files_to_ignore: additional files that should not
         be included in the documentation
        :param additional_folders_to_ignore: additional directories not
         included in documentation
        """

        self._logger = logger or getLogger(__name__)
        if not path_to_root_folder:
            path_to_root_folder = "./"
        if isinstance(path_to_root_folder, str):
            path_to_root_folder = Path(path_to_root_folder)

        self._root_folder = path_to_root_folder
        try:
            self._serializer = AllowedSaveModes[save_mode].value(
                self.language, self._logger
            )  # type: Serializer
        except KeyError:
            self._logger.warning(
                "Not allowed `save_mode` - %s. " "Allowed modes: %s",
                save_mode,
                [i.name for i in AllowedSaveModes],
            )
            return
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
            self._file_to_save = Path(
                self._root_folder.absolute().name
                + DEFAULT_SUFFIX
                + self._serializer.suffix_file
            )
        else:
            self._file_to_save = Path(file_to_save)
            if self._file_to_save.suffix != self._serializer.suffix_file:
                self._file_to_save = Path(
                    self._file_to_save.name + self._serializer.suffix_file
                )
        if not path_to_save:
            self._path_to_save = self._root_folder.absolute().parent / Path(
                self._root_folder.absolute().name + DEFAULT_SUFFIX
            )
            self._path_to_save.mkdir(exist_ok=True, parents=True)
        else:
            self._path_to_save = Path(path_to_save)
            self._path_to_save.mkdir(parents=True, exist_ok=True)
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
    def language(self) -> str:
        """
        Property for which language
        :return: str language
        :rtype: str
        :example:
        >>> language = "python"
        """
        raise NotImplementedError

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
    def build_documentation_file(self, path_to_file: Path) -> Module:
        """Method to overwriting in sub class for concrete ProgramLanguage
        :param Path path_to_file: file for which build documentation
        :return: list[str] docs
        """
        raise NotImplementedError

    def build_documentation(self):
        """
        Main function in build documentation
        """
        list_parsed_modules = list()  # type: List[Module]
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
            if not self._is_correct_folder_to_process(
                str(folder_path), _current_folders_to_ignore
            ):
                continue
            for file in list_files:
                if file in _current_files_to_ignore:
                    continue
                file_path = Path(file)
                if file_path.suffix not in self.types_of_file_to_process:
                    continue
                list_parsed_modules.append(
                    self.build_documentation_file(path_to_file=folder_path / file_path)
                )
        if self._extract_with_same_hierarchy:
            for module in list_parsed_modules:
                relative_path_to_module = str(module.path_to_file.absolute())[
                    len(str(self._root_folder.absolute())) :
                ]
                val = self._path_to_save
                tmp_path = Path(str(val) + relative_path_to_module)
                path_to_tmp_root = tmp_path.parent
                path_to_tmp_root.mkdir(exist_ok=True, parents=True)
                path_to_save = path_to_tmp_root / Path(
                    module.path_to_file.stem + self._serializer.suffix_file
                )
                self._save_documentation_file(
                    path_to_save, self._serializer.serialize(module)
                )
        else:
            one_documentation = [
                row
                for module in list_parsed_modules
                for row in self._serializer.serialize(module)
            ]
            self._save_documentation_file(
                self._path_to_save / self._file_to_save, one_documentation
            )

    @staticmethod
    def _is_correct_folder_to_process(
        folder: str, folders_to_ignore: List[str]
    ) -> bool:
        """
        method checks whether the specified directory
         should be processed
        :param str folder: current folder to process
        :param List[str] folders_to_ignore: folders in exclusion
        :return: true if need to process
        """
        for ig_folder in folders_to_ignore:
            if ig_folder == folder[: len(ig_folder)]:
                return False
        return True

    def _save_documentation_file(
        self, path_to_save: Path, data_to_save: List[str]
    ) -> None:
        """
        Method save data to file
        :param Path path_to_save: path to file
        :param List[str] data_to_save: data to save
        """

        if not data_to_save:
            self._logger.warning("Not data to save.")
            return
        if os.path.isfile(path_to_save):
            if not self._overwrite_if_file_exists:
                self._logger.warning(
                    "File with same name was exist. "
                    "Path to save: %s. "
                    "Change path to save or option "
                    "`overwrite_if_file_exists` set as True",
                    path_to_save,
                )
        path_to_save.parent.mkdir(exist_ok=True, parents=True)
        with open(path_to_save, "w", encoding="utf-8") as file:
            file.write(f"{os.linesep}".join(data_to_save))
