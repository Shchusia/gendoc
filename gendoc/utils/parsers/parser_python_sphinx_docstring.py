"""
Module with python sphinx doc_string
"""
import os
import re
from typing import Dict, Optional, Tuple

from gendoc.models import Parameter, ParsedDocString

GENERAL_STOPPERS = r"(?:(?=:param)|(?=:return)|(?=:raises)|(?=:type)|(?=:rtype)|(?=:example)|(?=\.\. code-block::)|\Z)"  # noqa

DESCRIPTION_REGEX = re.compile(
    f"(?P<description_method>[\*\w\s]+){GENERAL_STOPPERS}", re.S  # noqa
)

PARAM_REGEX = re.compile(
    f":param (?P<param>[\*\w\s]+): (?P<param_doc>.*?){GENERAL_STOPPERS}", re.S  # noqa
)
TYPE_REGEX = re.compile(
    f":type (?P<param>[\*\w\s]+): (?P<type>.*?){GENERAL_STOPPERS}", re.S  # noqa
)
RAISES_REGEX = re.compile(
    f":raises (?P<error_type>[\*\w\s]+): (?P<error_type_doc>.*?){GENERAL_STOPPERS}",  # noqa
    re.S,
)
RETURNS_REGEX = re.compile(f":return:(?P<return_doc>.*?){GENERAL_STOPPERS}", re.S)
RETURN_TYPE_REGEX = re.compile(f":rtype: (?P<rtype>.*?){GENERAL_STOPPERS}", re.S)
EXAMPLE_REGEX = re.compile(
    f"\.\. code-block:: (?P<language>[\*\w\s]+) (?P<example>.*?){GENERAL_STOPPERS}",  # noqa
    re.S,
)
EXAMPLE_REGEX_2 = re.compile(f":example:(?P<example>.*?){GENERAL_STOPPERS}", re.S)


def strip_rows(doc_string: str):
    lines = doc_string.expandtabs().splitlines()
    data = [line.strip() for line in lines]
    data = list(filter(lambda x: x, data))
    return f"{os.linesep}".join(data)


def parse_docstring(doc_string: Optional[str] = None) -> Optional[ParsedDocString]:
    """
    Function parse doc string to standard object
    ! sphinx doc string style
    :param doc_string:
    :type doc_string: str
    :return: parsed object
    :rtype:Optional[ParsedDocString]
    """

    def parse_params_type(
        _params: Dict[str, str], _types: Dict[str, str]
    ) -> Tuple[Dict[str, str], Dict[str, str]]:
        to_del = list()
        new = dict()
        for param, doc in _params.items():
            tmp = param.split()
            if len(tmp) > 1:
                to_del.append(param)
                new[tmp[-1]] = doc
                _types[tmp[-1]] = tmp[0]

        for td in to_del:
            del _params[td]
        _params.update(new)

        return _params, _types

    if not doc_string:
        return None
    params = {param: strip_rows(doc) for param, doc, in PARAM_REGEX.findall(doc_string)}
    types = {
        param: strip_rows(_type) for param, _type, in TYPE_REGEX.findall(doc_string)
    }
    params, types = parse_params_type(params, types)
    parameters = [
        Parameter(
            param_name=param,
            param_type=types.get(param, None),
            param_description=strip_rows(doc),
        )
        for param, doc in params.items()
    ]
    raises = [
        Parameter(param_type=error, param_description=strip_rows(doc))
        for error, doc in RAISES_REGEX.findall(doc_string)
    ]
    returns_match = RETURNS_REGEX.search(doc_string)
    returns = ""
    if returns_match:
        returns = strip_rows(returns_match.group("return_doc"))
    returns_type_match = RETURN_TYPE_REGEX.search(doc_string)
    return_type = None
    if returns_type_match:
        return_type = strip_rows(returns_type_match.group("rtype"))

    match_ex = EXAMPLE_REGEX.search(doc_string)
    example = ""
    if match_ex:
        example = strip_rows(match_ex.group("example"))
    else:
        match_ex = EXAMPLE_REGEX_2.search(doc_string)
        if match_ex:
            example = strip_rows(match_ex.group("example"))
    description = ""
    match_description = DESCRIPTION_REGEX.search(doc_string)
    if match_description:
        description = strip_rows(match_description.group("description_method"))
    parsed_doc_string = ParsedDocString(
        description=description,
        example=example,
        returns=Parameter(param_type=return_type, param_description=returns),
        raises=raises,
        args=parameters,
    )
    return parsed_doc_string


if __name__ == "__main__":
    doc_str = """Exapmle doc
            long string
        :param val1: value with
         long description
         really long
        :type val1: str
        :param str val2: other variable
        :return: some return text
        :rtype: str
        :raises RunTimeError: if error in time execution
        :example:
        >>> from pathlib import Path
        >>> from model import Model
        >>> MODEL_PATH = Path('model')
        >>> mdl = Model(model_path=MODEL_PATH)
        >>> mdl.predict(42)
        result - 42
        """
    print(parse_docstring(doc_str))
