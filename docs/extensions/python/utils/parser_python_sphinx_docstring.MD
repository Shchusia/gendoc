# Module `parser_python_sphinx_docstring.py`
```text
Module with python Sphinx docstrings parser
```

> Path: `gen_doc\extensions\python\utils\parser_python_sphinx_docstring.py`
`GENERAL_STOPPERS` = "(?:(?=:param)|(?=:attr)|(?=:return)|(?=:yield)|(?=:note)|(?=:raises)|(?=:type)|(?=:rtype)|(?=:ytype)|(?=:todo)|(?=:example)|(?=\.\. code-block::)|\Z)"
`DESCRIPTION_REGEX` = re.compile(f'(?P<description_method>.*?){GENERAL_STOPPERS}', re.S)
`PARAM_REGEX` = re.compile(f':param (?P<param>[\\*\\w\\s\\[\\]\\,]+): (?P<param_doc>.*?){GENERAL_STOPPERS}', re.S)
`ATTR_REGEX` = re.compile(f':attr (?P<attr>[\\*\\w\\s\\[\\]\\,]+): (?P<attr_doc>.*?){GENERAL_STOPPERS}', re.S)
`TYPE_REGEX` = re.compile(f':type (?P<param>[\\*\\w\\s]+): (?P<type>.*?){GENERAL_STOPPERS}', re.S)
`RAISES_REGEX` = re.compile(f':raises (?P<error_type>[\\*\\w\\s]+): (?P<error_type_doc>.*?){GENERAL_STOPPERS}', re.S)
`NOTE_REGEX` = re.compile(f':note:(?P<note_doc>.*?){GENERAL_STOPPERS}', re.S)
`TODO_REGEX` = re.compile(f':todo:(?P<todo_doc>.*?){GENERAL_STOPPERS}', re.S)
`RETURNS_REGEX` = re.compile(f':return:(?P<return_doc>.*?){GENERAL_STOPPERS}', re.S)
`YIELD_REGEX` = re.compile(f':yield:(?P<yield_doc>.*?){GENERAL_STOPPERS}', re.S)
`RETURN_TYPE_REGEX` = re.compile(f':rtype: (?P<rtype>.*?){GENERAL_STOPPERS}', re.S)
`YIELD_TYPE_REGEX` = re.compile(f':ytype: (?P<ytype>.*?){GENERAL_STOPPERS}', re.S)
`EXAMPLE_REGEX` = re.compile(f'\\.\\. code-block:: (?P<language>[\\*\\w\\s]+)(?P<example>.*?){GENERAL_STOPPERS}', re.S)
`EXAMPLE_REGEX_2` = re.compile(f':example:(?P<example>.*?){GENERAL_STOPPERS}', re.S)
## Class `SphinxDocStringPyParser`
```text
Sphinx doc string parser
```

### Basses(s)
+ PythonDocStringParser
### SubElement(s)
 > `example` = "
 > Object doc string
 > with long description
 > 
 > :param value1: description to value1
 > :type value1: str
 > :param List[str] value2: description to value2
 > long description value2
 > :attr value3: description to value3
 > :type value3: Dict[str, str]
 > :attr List[Tuple[str, str]] value4: description to value3
 > :return: what return function
 > :rtype: type returned value
 > :yield: if yield function
 > :ytype: for yield value
 > :note: note string
 > with some information
 > :todo: todo1
 > :todo: todo2
 > with description
 > :example:
 > >>> import this
 > >>> # and other imports
 > "
 > ## Function  `parse`
 > ```text
 > Function to parse doc string to a standard object
 > ! sphinx doc string style
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
 > > + `_params`: Dict[str, str] - empty doc string
 > > + `_types`: Dict[str, str] - empty doc string
 > > #### Declared returns: `Tuple[Dict[str, str], Dict[str, str]]`
 > > ## Function  `convert_params_attrs`
 > > ### Argument(s)
 > > + `_vals`: Dict[str, str] - empty doc string
 > > + `_types`: Dict[str, str] - empty doc string
 > > #### Declared returns: `List[Parameter]`