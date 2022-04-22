"""
Model for module
"""
from __future__ import annotations

from pathlib import Path
from typing import Any, List, Optional, Union

from pydantic import BaseModel, Field

from .variables import EnumTypeVariables


class EntityOfCode(BaseModel):
    pass


class Entity(EntityOfCode):
    e_type: EnumTypeVariables = Field(None, description="")
    e_value: List[Union[Entity, Any]] = Field(None, description="")


class Module(BaseModel):
    path_to_file: Path = Field(description="Path to file from root folder")
    module_doc_string: Optional[str] = Field(None, description="Doc string for module")
    list_entities: List[EntityOfCode] = Field(None, description="")


class Argument(EntityOfCode):
    arg: str
    annotation: Entity
    type_comment: Any


class Arguments(EntityOfCode):
    args: List[Argument] = Field(None, description="")
    defaults: List[Entity] = Field(None, description="")
    kw_defaults: List[Entity] = Field(None, description="")
    kwarg: Optional[Argument] = Field(None, description="")  # **kwarg
    vararg: Optional[Argument] = Field(None, description="")  # *args
    posonlyargs: List[Argument] = Field(None, description="")
    kwonlyargs: List[Argument] = Field(None, description="")


class Parameter(BaseModel):
    param_name: str = Field(None, description="")
    param_type: str = Field(None, description="")
    param_description: str = Field(None, description="")


class ParsedDocString(BaseModel):
    description: str = Field(None, description="")
    args: List[Parameter] = Field(None, description="")
    raises: List[Parameter] = Field(None, description="")
    returns: Parameter = Field(None, description="")
    example: str = Field(None, description="")


class Function(EntityOfCode):
    function_name: str = Field(None, description="")
    function_doc_string: str = Field(None, description="")
    function_args: Arguments = Field(None, description="")
    function_decorators: List[Entity] = Field(None, description="")
    function_returns: Entity = Field(None, description="")
    function_type_comment: Any = Field(None, description="")
    function_is_async: bool = Field(False, description="")
    function_entities: List[EntityOfCode] = Field(None, description="")
    function_parsed_docstring: Optional[ParsedDocString] = Field(None, description="")


class Assign(EntityOfCode):
    name: Entity = Field(None, description="")
    value: Entity = Field(None, description="")
    type_comment: Any = Field(None, description="")
    annotation: Entity = Field(None, description="")
    simple: Any = Field(None, description="")


class Variable:
    name: List[Entity] = Field(None, description="")
    value: List[Entity] = Field(None, description="")


class Class(EntityOfCode):
    class_name: str = Field(None, description="Class name")
    class_doc_string: str = Field(None, description="Class doc string")
    class_decorators: List[Entity] = Field(None, description="")
    class_bases: List[Entity] = Field(None, description="")
    class_keywords: List[Assign] = Field(None, description="")
    class_entities: List[EntityOfCode] = Field(None, description="")
