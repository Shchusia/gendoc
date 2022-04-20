"""
Module with doc generator for sphinx doc strings
"""
from pathlib import Path
from typing import List

from ..doc_generator import DocGenerator


class PythonDocGenerator(DocGenerator):
    """
    Class for retrieving information about python module
    """

    short_name = "py"
    types_of_file_to_process = [".py"]
    folders_to_ignore = ["__pycache__", ".git", "venv", "build", "dist"]
    files_to_ignore = ["setup.py"]

    def build_documentation_file(self, path_to_file: Path, deep: int = 1) -> List[str]:
        """Method to overwriting in sub class for concrete ProgramLanguage
        :param Path path_to_file: file for which build documentation
        :param int optional int deep: at what nesting level is the file
        :return: list[str] docs
        """
        raise NotImplementedError
