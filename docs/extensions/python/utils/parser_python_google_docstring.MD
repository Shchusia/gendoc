# Module `parser_python_google_docstring.py`
```text
Module with python Google docstrings parser
```

> Path: `gen_doc\extensions\python\utils\parser_python_google_docstring.py`
`GENERAL_STOPPERS` = "(?:(?=Args:)|(?=Arguments?:)|(?=Returns?:)|(?=Raises?:)|(?=Attributes?:)|(?=Examples?:)|(?=Todo?:)|(?=Notes?:)|(?=Yields?:)|(?=\.\. \_)|\Z)"
`DESCRIPTION_REGEX` = re.compile(f'(?P<description>.*?){GENERAL_STOPPERS}', re.S)
`ARGS_REGEX` = re.compile(f'(Args|Arguments?):?\\s (?P<args_doc>.*?){GENERAL_STOPPERS}', re.S)
`RETURNS_REGEX` = re.compile(f'Returns?:?\\s (?P<returns_doc>.*?){GENERAL_STOPPERS}', re.S)
`YIELDS_REGEX` = re.compile(f'Yields?:?\\s (?P<yields_doc>.*?){GENERAL_STOPPERS}', re.S)
`RAISES_REGEX` = re.compile(f'Raises?:?\\s (?P<raises_doc>.*?){GENERAL_STOPPERS}', re.S)
`ATTRIBUTES_REGEX` = re.compile(f'Attributes?:?\\s (?P<attribute_doc>.*?){GENERAL_STOPPERS}', re.S)
`EXAMPLE_REGEX` = re.compile(f'Examples?:?\\s (?P<example_doc>.*?){GENERAL_STOPPERS}', re.S)
`NOTE_REGEX` = re.compile(f'Notes?:?\\s (?P<note_doc>.*?){GENERAL_STOPPERS}', re.S)
`TODO_REGEX` = re.compile(f'Todos?:?\\s (?P<todo_doc>.*?){GENERAL_STOPPERS}', re.S)
`OPTIONAL_ARGS_REGEX` = re.compile(f'\\.\\. \\_(?P<optional_name>[\\*\\w\\s]+):?\\s (?P<optional_doc>.*?){GENERAL_STOPPERS}', re.S)
`STOPPERS_ATTR_ARG` = "(?:(?=[\r\n?|\n]{1,}[ \t\d\w\(\)\]\[\,]+:)|\Z)"
`RETURN_YIELD_PARSERS_REGEX` = re.compile(f'(?P<type>[\\s\\d\\w\\(\\)\\]\\[\\,]+): (?P<return_doc>.*?){STOPPERS_ATTR_ARG}', re.S)
`STOPPERS_TODOS` = "(?:(?=\*)|\Z)"
`TODOS_PARSER_REGEX` = re.compile(f'\\* (?P<to_do>.*?){STOPPERS_TODOS}', re.S)
`PARAM_REGEX` = re.compile(f'\\s(?P<param>[\\s\\d\\w\\(\\)\\]\\[\\,]+): (?P<param_doc>.*?){STOPPERS_ATTR_ARG}', re.S)
`PARSE_PARAM_TYPE` = re.compile(f'(?P<param>[\\*\\w\\s]+)[\\s]*\\((?P<type>.*?)\\)', re.S)
## Class `GoogleDocStringPyParser`
```text
Google doc string parser
```

### Basses(s)
+ PythonDocStringParser
### SubElement(s)
 > `example` = "
 > Example google doc string
 > 
 > Description of function
 > 
 > Arguments:
 > value1 (int): description to value1
 > value2 (Dict[str, str]): description to value2
 > long description
 > value2 desc
 > value3: description value3
 > Attributes:
 > value4 (int): description to value4
 > value5: description to value5
 > Raises:
 > AttributeError: The ``Raises`` section is a list of all exceptions
 > that are relevant to the interface.
 > Returns:
 > type_returned_value: a description of return
 > Todos:
 > * For module TODOs
 > * ToDo
 > long
 > .. _Google Python Style Guide optional parameters:
 > http://google.github.io/styleguide/pyguide.html
 > .. _PEP 484:
 > https://www.python.org/dev/peps/pep-0484/
 > Yields:
 > int: yield value with type
 > Note:
 > Do not include the `self` parameter in the ``Args`` section.
 > Example:
 > Examples should be written in doctest format, and should illustrate how
 > to use the function.
 > >>> print([i for i in example_generator(4)])
 > [0, 1, 2, 3]
 > "
 > ## Function  `parse`
 > ```text
 > Function to parse doc string to a standard object
 > ! google doc string style
 > ```
 > 
 > ### Decorator(s)
 > + staticmethod
 > ### Argument(s)
 > + `doc_string`: Optional[str] - received function doc string
 > ### Return
 > ```text
 > parsed object
 > ```
 > 
 > #### Declared returns: `Optional[ParsedDocString]`
 > ### SubElement(s)
 > > ## Function  `parse_params_type`
 > > ### Argument(s)
 > > + `param_type_part`: str - empty doc string
 > > #### Declared returns: `Tuple[str, Optional[str]]`
 > > ## Function  `parse_attributes_args`
 > > ### Argument(s)
 > > + `block_doc_string`: str - empty doc string
 > > #### Declared returns: `List[Parameter]`
 > > ## Function  `parse_return_yield_doc`
 > > ### Argument(s)
 > > + `parsed_doc` - empty doc string
 > > #### Declared returns: `Parameter`