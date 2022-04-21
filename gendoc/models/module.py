"""
Model for module
"""
from __future__ import annotations

from pathlib import Path
from typing import Any, List, Union

from pydantic import BaseModel, Field

from .variables import EnumTypeVariables


class EntityOfCode(BaseModel):
    pass


class Module(BaseModel):
    path_to_file: Path = Field(description="Path to file from root folder")
    module_doc_string: str = Field(description="Doc string for module")
    list_entities: List[EntityOfCode] = Field(None, description="")


class Decorators(EntityOfCode):
    pass


class Function(EntityOfCode):
    pass


class Entity(EntityOfCode):
    e_type: EnumTypeVariables = Field(None, description="")
    e_value: List[Union[Entity, Any]] = Field(None, description="")


class Assign(EntityOfCode):
    name: Entity = Field(None, description="")
    value: Entity = Field(None, description="")
    type_comment: Any = Field(None, description="")
    annotation: Any = Field(None, description="")
    simple: Any = Field(None, description="")


class Variable:
    name: List[Entity] = Field(None, description="")
    value: List[Entity] = Field(None, description="")


class Class(EntityOfCode):
    class_name: str = Field(None, description="")
    class_decorators: List[str] = Field(None, description="")
    class_bases: List[str] = Field(None, description="")
    class_variables: List[EntityOfCode] = Field(None, description="")
    class_doc_string: str = Field(None, description="Doc string")
    class_entities: List[EntityOfCode] = Field(None, description="")
