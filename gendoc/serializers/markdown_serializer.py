"""
Markdown serializer
"""
import os
from typing import Any, Dict, List, Optional

from gendoc.models import (
    Assign,
    Class,
    Entity,
    EntityOfCode,
    EnumTypeVariables,
    Function,
    Module,
)
from gendoc.models.module import Argument, ParsedDocString
from gendoc.serializers.serializer import Serializer


class MarkdownSerializer(Serializer):
    """
    Module convert parsed to pretty markdown format
    """

    suffix_file = ".MD"

    def serialize(self, module: Module) -> List[str]:
        return self.module_to_markdown_string(module)

    def module_to_markdown_string(self, module: Module) -> List[str]:
        module_markdown = list()  # type:List[str]
        module_markdown.extend(self.convert_module_data(module))
        for entity in module.list_entities:
            module_markdown.extend(self.convert_entity_of_code(entity))

        return module_markdown

    def convert_module_data(self, module: Module) -> List[str]:
        """
        Convert base info of module
        :param module: module to convert
        :type module: Module
        :return: list of markdown
        """
        self._logger.debug("Started convert module base data")
        module_data_markdown = list()  # type:List[str]
        module_data_markdown.append(f"# Module `{module.path_to_file.name}`")
        module_data_markdown.append(
            f"""```text
{module.module_doc_string}
```
"""
        )
        module_data_markdown.append(f"> Path: `{module.path_to_file}`")
        self._logger.debug("Finished convert module base data")
        return module_data_markdown

    def convert_entity_of_code(self, entity_of_code: EntityOfCode) -> List[str]:
        """

        :param entity_of_code:
        :return:
        """
        if isinstance(entity_of_code, Assign):
            return self.convert_assign(entity_of_code)
        elif isinstance(entity_of_code, Class):
            return self.convert_class(entity_of_code)
        elif isinstance(entity_of_code, Function):
            return self.convert_function(entity_of_code)
        else:
            self._logger.warning("Unknown type entity_of_code: %s", entity_of_code)
        return list()

    def convert_assign(self, entity_assign: Assign) -> List[str]:
        name = self.convert_entity(entity_assign.name)
        value = self.convert_entity(entity_assign.value)
        annotation = self.convert_entity(entity_assign.annotation)
        row_annotation = ""
        if annotation:
            row_annotation = f": {annotation}"
        if name[0] == "(" and name[-1] == ")":
            name = name[1:-1]
        return [f"`{name}`{row_annotation} = {value}"]

    def convert_class(self, entity_class: Class) -> List[str]:
        class_markdown = list()  # type: List[str]

        class_markdown.append(f"## Class `{entity_class.class_name}`")
        if entity_class.class_doc_string:
            class_markdown.append(
                f"""```text
{entity_class.class_doc_string}
```
"""
            )
        if entity_class.class_decorators:
            class_markdown.append("### Decorator(s)")
            for decorators in entity_class.class_decorators:
                class_markdown.append(f"+ {self.convert_entity(decorators)}")
        if entity_class.class_bases:
            class_markdown.append("### Basses(s)")
            for base in entity_class.class_bases:
                class_markdown.append(f"+ {self.convert_entity(base)}")
        if entity_class.class_entities:
            class_markdown.append("### SubElement(s)")
            for ent in entity_class.class_entities:
                class_markdown.append(self.convert_sub_code(ent))
        return class_markdown

    def convert_function(self, entity_function: Function) -> List[str]:
        def convert_parse_docs(
            parse_docs: Optional[ParsedDocString],
        ) -> Dict[str, Any]:
            if not parse_docs:
                return dict(
                    description="",
                    example="",
                    returns={"doc": "", "type": ""},
                    args=dict(),
                    raises=dict(),
                )
            dict_converted = {
                "description": parse_docs.description,
                "example": parse_docs.example,
                "returns": {
                    "doc": parse_docs.returns.param_description,
                    "type": parse_docs.returns.param_type,
                },
                "args": {
                    arg_d.param_name: {
                        "doc": arg_d.param_description,
                        "type": arg_d.param_type,
                    }
                    for arg_d in parse_docs.args
                },
                "raises": [
                    {"doc": raise_d.param_description, "type": raise_d.param_type}
                    for raise_d in parse_docs.raises
                ],
            }
            return dict_converted

        def get_arg_str(arg_name: Argument, _converted_doc_string) -> str:
            tmp_annotations = self.convert_entity(arg_name.annotation)
            if not tmp_annotations:
                tmp_annotations = (
                    _converted_doc_string["args"]
                    .get(arg_name.arg, dict())
                    .get("type", "")
                )
            if tmp_annotations:
                tmp_annotations = ": " + tmp_annotations
            doc_string = (
                _converted_doc_string["args"].get(arg_name.arg, dict()).get("doc", "")
            )
            if not doc_string:
                doc_string = "empty doc string"
            arg_row = f"`{arg_name.arg}`{tmp_annotations} - {doc_string}"
            return arg_row

        def convert_args(args: List[Argument], _converted_doc_string):
            args_markdown = list()
            for arg in args:
                arg_row = get_arg_str(arg, _converted_doc_string)
                args_markdown.append(f"+ {arg_row}")
            return args_markdown

        function_markdown = list()  # type: List[str]
        converted_doc_string = convert_parse_docs(
            entity_function.function_parsed_docstring
        )
        async_text = ""
        if entity_function.function_is_async:
            async_text = "`async`"
        function_markdown.append(
            f"## Function {async_text} `{entity_function.function_name}`"
        )
        if converted_doc_string.get("description"):
            function_markdown.append(
                f"""```text
{converted_doc_string["description"]}
```
        """
            )
        if entity_function.function_decorators:
            function_markdown.append("### Decorator(s)")
            for decorators in entity_function.function_decorators:
                function_markdown.append(f"+ {self.convert_entity(decorators)}")
        if any(
            [
                entity_function.function_args.args,
                entity_function.function_args.posonlyargs,
                entity_function.function_args.kwonlyargs,
                entity_function.function_args.vararg,
                entity_function.function_args.kwarg,
            ]
        ):
            function_markdown.append("### Argument(s)")
            function_markdown.extend(
                convert_args(
                    entity_function.function_args.posonlyargs, converted_doc_string
                )
            )
            function_markdown.extend(
                convert_args(entity_function.function_args.args, converted_doc_string)
            )
            function_markdown.extend(
                convert_args(
                    entity_function.function_args.kwonlyargs, converted_doc_string
                )
            )
            if entity_function.function_args.vararg:
                vararg = get_arg_str(
                    entity_function.function_args.vararg, converted_doc_string
                )
                function_markdown.append(f"+ *{vararg}")
            if entity_function.function_args.kwarg:
                kwarg = get_arg_str(
                    entity_function.function_args.kwarg, converted_doc_string
                )
                function_markdown.append(f"+ **{kwarg}")

        if converted_doc_string["raises"]:
            function_markdown.append("### Raise(s)")
            for row_raise in converted_doc_string["raises"]:
                function_markdown.append(
                    f"+ `{row_raise['type']}` - {row_raise['doc']}"
                )

        if converted_doc_string["returns"].get("doc"):
            function_markdown.append("### Return")
            function_markdown.append(
                f"""```text
{converted_doc_string["returns"]["doc"]}
```
                    """
            )
        if entity_function.function_returns:
            function_markdown.append(
                f"#### Declared returns: "
                f"`{self.convert_entity(entity_function.function_returns)}`"
            )
        else:
            if converted_doc_string["returns"].get("type"):
                function_markdown.append(
                    f"#### Declared returns: "
                    f"`{converted_doc_string['returns']['type']}`"
                )
        if converted_doc_string["example"]:
            function_markdown.append("### Example ")
            function_markdown.append(
                f"""```{self._language}
{converted_doc_string["example"]}
```
"""
            )
        if entity_function.function_entities:
            function_markdown.append("### SubElement(s)")
            for ent in entity_function.function_entities:
                function_markdown.append(self.convert_sub_code(ent))
        return function_markdown

    def convert_sub_code(self, entity: EntityOfCode) -> str:
        tmp_list_entity = self.convert_entity_of_code(entity)
        tmp_list = [
            f" > {row.strip()}"
            for row in "\n".join(tmp_list_entity).expandtabs().splitlines()
        ]
        return "\n".join(tmp_list)

    def convert_entity(self, entity: Optional[Entity]) -> Optional[str]:
        if not entity:
            return None
        if entity.e_type == EnumTypeVariables.NONE:
            return None
        elif entity.e_type in [
            EnumTypeVariables.BOOL,
            EnumTypeVariables.NUM,
            EnumTypeVariables.NAME,
        ]:
            return str(entity.e_value[0])
        elif entity.e_type in EnumTypeVariables.STR:
            return f'"{entity.e_value[0]}"'
        elif entity.e_type in [
            EnumTypeVariables.TUPLE,
            EnumTypeVariables.LIST,
            EnumTypeVariables.SET,
        ]:
            res = [self.convert_entity(val) for val in entity.e_value]
            if entity.e_type == EnumTypeVariables.TUPLE:
                return f"({', '.join(res)})"
            if entity.e_type == EnumTypeVariables.LIST:
                return f"[{', '.join(res)}]"
            if entity.e_type == EnumTypeVariables.SET:
                return f"{{{', '.join(res)}}}"
        elif entity.e_type == EnumTypeVariables.SLICE:
            lower = self.convert_entity(entity.e_value[0]) if entity.e_value[0] else ""
            upper = self.convert_entity(entity.e_value[1]) if entity.e_value[1] else ""
            step = self.convert_entity(entity.e_value[2]) if entity.e_value[2] else ""
            return f"[{lower}:{upper}:{step}]"
        elif entity.e_type == EnumTypeVariables.DICT:
            res = [
                f"{self.convert_entity(key)}: {self.convert_entity(value)}"
                for key, value in entity.e_value
            ]
            return f"""{{
            {f',{os.linesep}'.join(res)}
            }}"""
        elif entity.e_type == EnumTypeVariables.BIN_OP:
            left = self.convert_entity(entity.e_value[0])
            right = self.convert_entity(entity.e_value[2])
            return f"{left} {entity.e_value[1]} {right}"
        elif entity.e_type == EnumTypeVariables.UNARY_OP:
            return f"{entity.e_value[0]} {self.convert_entity(entity.e_value[1])}"
        elif entity.e_type == EnumTypeVariables.UNPARSE:
            return f"{entity.e_value[0]}"
        else:
            self._logger.warning("Unknown entity to convert - %s.", entity)
        return "unknown"
