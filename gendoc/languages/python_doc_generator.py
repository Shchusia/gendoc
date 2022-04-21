"""
Module with doc generator for sphinx doc strings
"""
import ast
from ast import stmt
from pathlib import Path
from typing import List, Optional, Union

from ..doc_generator import DocGenerator
from ..models import (
    Assign,
    Class,
    Entity,
    EntityOfCode,
    EnumTypeVariables,
    Module,
    Operations,
)


class PythonDocGenerator(DocGenerator):
    """
    Class for retrieving information about python module
    """

    short_name = "py"
    types_of_file_to_process = [".py"]
    folders_to_ignore = [
        "__pycache__",
        ".git",
        "venv",
        "build",
        "dist",
        ".mypy_cache",
        ".idea",
    ]
    files_to_ignore = ["setup.py"]

    def _parse_body(
        self,
        obj: Union[ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef],
    ) -> List[EntityOfCode]:
        """
        Method parse object body for parse child
        :param obj: obj to process
        :type obj: Union[ast.Module, ast.ClassDef, ast.FunctionDef,
         ast.AsyncFunctionDef]
        :return: parsed body
        :rtype: List[EntityOfCode]
        """
        list_entities = list()  # type: List[EntityOfCode]
        for obj in obj.body:  # type: ignore
            parsed_obj = self._parse_obj(obj)  # type: ignore
            if parsed_obj:
                list_entities.append(parsed_obj)
        return list_entities

    def _parse_obj(self, obj: stmt) -> Optional[EntityOfCode]:
        """
        Method for defining the handler object
        the method contains all objects for analysis
        :param obj: object to process if exist handler
        :type obj: stmt
        :return: type, info
        :rtype:
        """

        if isinstance(obj, (ast.Expr, ast.Import, ast.ImportFrom)):
            return None
        elif isinstance(obj, (ast.Assign, ast.AnnAssign)):
            return self._parse_assign(obj)
        elif isinstance(obj, ast.ClassDef):
            return self._parse_class(obj)
        elif isinstance(obj, (ast.FunctionDef, ast.AsyncFunctionDef)):
            pass
        elif isinstance(obj, ast.Assert):
            pass
        else:
            self._logger.warn("can't parse %s", obj)
        return None

    def _parse_value(self, obj: ast.expr) -> Entity:
        if obj is None:
            return Entity(e_type=EnumTypeVariables.NONE, e_value=[None])
        elif obj in [True, False]:
            return Entity(e_type=EnumTypeVariables.BOOL, e_value=[obj])
        elif isinstance(obj, ast.Name):
            return Entity(e_type=EnumTypeVariables.NAME, e_value=[obj.id])
        elif isinstance(obj, ast.Num):
            return Entity(e_type=EnumTypeVariables.NUM, e_value=[obj.n])
        elif isinstance(obj, ast.Str):
            return Entity(e_type=EnumTypeVariables.STR, e_value=[obj.s])
        elif isinstance(obj, ast.NameConstant):
            return self._parse_value(obj.value)
        elif isinstance(obj, ast.Constant):
            return self._parse_value(obj.value)
        elif isinstance(obj, ast.Tuple):
            return Entity(
                e_type=EnumTypeVariables.TUPLE,
                e_value=[self._parse_value(val) for val in obj.elts],
            )
        elif isinstance(obj, ast.List):
            return Entity(
                e_type=EnumTypeVariables.LIST,
                e_value=[self._parse_value(val) for val in obj.elts],
            )
        elif isinstance(obj, ast.Set):
            return Entity(
                e_type=EnumTypeVariables.SET,
                e_value=[self._parse_value(val) for val in obj.elts],
            )
        elif isinstance(obj, ast.Slice):
            lower = self._parse_value(obj.lower) if obj.lower else ""
            upper = self._parse_value(obj.upper) if obj.upper else ""
            step = self._parse_value(obj.step) if obj.step else ""
            return Entity(e_type=EnumTypeVariables.SLICE, e_value=[lower, upper, step])
        elif isinstance(obj, ast.Dict):
            return Entity(
                e_type=EnumTypeVariables.DICT,
                e_value=[
                    (self._parse_value(key), self._parse_value(value))
                    for key, value in zip(obj.keys, obj.values)
                ],
            )
        elif isinstance(obj, ast.BinOp):
            return Entity(
                e_type=EnumTypeVariables.BIN_OP,
                e_value=[
                    self._parse_value(obj.right),
                    Operations[obj.op.__class__.__name__].value,
                    self._parse_value(obj.left),
                ],
            )
        elif isinstance(obj, ast.UnaryOp):
            return Entity(
                e_type=EnumTypeVariables.UNARY_OP,
                e_value=[
                    Operations[obj.op.__class__.__name__].value,
                    self._parse_value(obj.operand),
                ],
            )

        else:
            self._logger.warn("Not processed: %s", obj)
            return Entity(e_type=EnumTypeVariables.UNPARSE, e_value=[ast.unparse(obj)])

    def _parse_assign(self, obj: Union[ast.Assign, ast.AnnAssign]) -> Assign:
        """
        Parse assign
        :param obj: obj for parse Assign
        :type: Union[ast.Assign, ast.AnnAssign]
        :param is_ann: is annotated
        :type: bool
        :return: parsed all assigned
        :rtype: Assign
        """
        assign = Assign(value=self._parse_value(obj.value))
        if isinstance(obj, ast.AnnAssign):
            assign.name = self._parse_value(obj.target)
            assign.annotation = self._parse_value(obj.annotation)
            assign.simple = obj.simple
        else:
            assign.name = self._parse_value(obj.targets[0])
            assign.type_comment = obj.type_comment
        return assign

    def _parse_class(self, obj: ast.ClassDef) -> Class:
        """
        Method parse class
        :param obj: current class to parse info
        :type obj: ast.ClassDef
        :return: processed class
        :rtype: Class
        """
        clazz = Class(class_name=obj.name)
        try:
            class_doc_string = ast.get_docstring(obj)
        except Exception as exc:
            class_doc_string = ""
            self._logger.debug(
                "Class `%s` don't have class doc string. Err: %s",
                clazz.class_name,
                str(exc),
            )
        clazz.class_doc_string = class_doc_string
        clazz.class_decorators = self._parse_decorators(obj)
        clazz.class_bases = self._parse_basses(obj)
        clazz.class_entities = self._parse_body(obj)
        clazz.class_keywords = self._parse_keywords(obj)
        return clazz

    def _parse_decorators(
        self, obj: Union[ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef]
    ) -> List[Entity]:
        """
        Method get decorators of class or function
        :param obj: obj to parse
        :rtype obj: Union[ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef]
        :return:
        """
        return [self._parse_value(decorator) for decorator in obj.decorator_list]

    def _parse_basses(self, obj: ast.ClassDef) -> List[Entity]:
        """
        Method parse bases class for current
        :param obj:
        :type: ast.ClassDef
        :return: list of bases classes
        :rtype: List[Entity]
        """
        return [self._parse_value(base) for base in obj.bases]

    def _parse_keywords(self, obj: ast.ClassDef) -> List[Assign]:
        """

        :param obj:
        :return:
        """
        return [
            Assign(
                name=Entity(e_type=EnumTypeVariables.NAME, e_value=[key_word.arg]),
                value=self._parse_value(key_word.value),
            )
            for key_word in obj.keywords
        ]

    def _parse_file(self, path_to_file: Path) -> Module:
        """
        Main processing method
        Reads the file and starts the parsing process
        :param path_to_file: path to the file to be processed
        :type: Path
        :return: with extracted information from file
        :rtype:
        """
        file_to_parse = open(path_to_file, "r", encoding="utf-8").read()
        tree = ast.parse(file_to_parse)
        try:
            module_doc_string = ast.get_docstring(tree)
        except Exception:
            module_doc_string = ""
            self._logger.debug("File `%s` don't have module doc string", path_to_file)
        module = Module(path_to_file=path_to_file, module_doc_string=module_doc_string)
        module.list_entities = self._parse_body(tree)
        return module

    def build_documentation_file(
        self, path_to_file: Path, deep: int = 1
    ) -> Optional[Module]:
        """Method to overwriting in sub class for concrete ProgramLanguage
        :param Path path_to_file: file for which build documentation
        :type path_to_file: Path
        :param deep: at what nesting level is the file
        :type deep: Path
        :return: docs
        :rtype: List[str]
        """
        self._logger.debug("Started process file: %s", path_to_file)

        self._parse_file(path_to_file)

        self._logger.debug("Finished process file: %s", path_to_file)
        return None
