"""
Main module with class for working with catalog
"""
# pylint: disable=too-many-arguments
from collections import Iterable
from distutils.util import strtobool
from logging import Logger, getLogger
from pathlib import Path
from typing import List, Optional, Union

from gen_doc.models import Module

from .extensions import GenDocParser, GenDocParsers
from .models import GeneralInfo
from .serializers import GenDocSerializer, GenDocSerializers
from .settings import DEFAULT_SUFFIX


class DocGenerator:
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
        parse_mode: Optional[str] = "py",
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
        :param parse_mode: parse_mode
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
            _ = GenDocParsers[parse_mode]
            self._parse_mode = parse_mode
        except KeyError:
            self._logger.warning(
                "Not allowed `parse_mode` - %s. " "Allowed modes: %s",
                save_mode,
                [i.name for i in GenDocParsers],
            )
            return

        try:
            _ = GenDocSerializers[save_mode]
            self._save_mode = save_mode
        except KeyError:
            self._logger.warning(
                "Not allowed `save_mode` - %s. " "Allowed modes: %s",
                save_mode,
                [i.name for i in GenDocSerializers],
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
        self._file_to_save = file_to_save
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

    def generate(self):
        """
        Function to run process generate documentation
        """
        parser = GenDocParsers[self._parse_mode].value(
            logger=self._logger,
            path_to_root_folder=self._root_folder,
            additional_files_to_ignore=self._additional_files_to_ignore,
            additional_folders_to_ignore=self._additional_folders_to_ignore,
        )  # type: GenDocParser
        list_modules = parser.parse()  # type: List[Module]
        serializer = GenDocSerializers[self._save_mode].value(
            path_to_save=self._path_to_save,
            root_folder=self._root_folder,
            file_to_save=self._file_to_save,
            logger=self._logger,
            language=parser.language,
            extract_with_same_hierarchy=self._extract_with_same_hierarchy,
            overwrite_if_file_exists=self._overwrite_if_file_exists,
            general_info=self.general_info,
        )  # type: GenDocSerializer
        serializer.serialize(modules=list_modules)
