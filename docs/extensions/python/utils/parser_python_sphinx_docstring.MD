# Module `parser_python_sphinx_docstring.py`
```text
Module with python Sphinx docstrings parser
```

> Path: `gen_doc\extensions\python\utils\parser_python_sphinx_docstring.py`
`GENERAL_STOPPERS` = "(?:(?=:param)|(?=:return)|(?=:raises)|(?=:type)|(?=:rtype)|(?=:example)|(?=\.\. code-block::)|\Z)"
`DESCRIPTION_REGEX` = re.compile(f'(?P<description_method>[\\*\\w\\s]+){GENERAL_STOPPERS}', re.S)
`PARAM_REGEX` = re.compile(f':param (?P<param>[\\*\\w\\s]+): (?P<param_doc>.*?){GENERAL_STOPPERS}', re.S)
`TYPE_REGEX` = re.compile(f':type (?P<param>[\\*\\w\\s]+): (?P<type>.*?){GENERAL_STOPPERS}', re.S)
`RAISES_REGEX` = re.compile(f':raises (?P<error_type>[\\*\\w\\s]+): (?P<error_type_doc>.*?){GENERAL_STOPPERS}', re.S)
`RETURNS_REGEX` = re.compile(f':return:(?P<return_doc>.*?){GENERAL_STOPPERS}', re.S)
`RETURN_TYPE_REGEX` = re.compile(f':rtype: (?P<rtype>.*?){GENERAL_STOPPERS}', re.S)
`EXAMPLE_REGEX` = re.compile(f'\\.\\. code-block:: (?P<language>[\\*\\w\\s]+)(?P<example>.*?){GENERAL_STOPPERS}', re.S)
`EXAMPLE_REGEX_2` = re.compile(f':example:(?P<example>.*?){GENERAL_STOPPERS}', re.S)
## Function  `strip_rows`
### Argument(s)
+ `doc_string`: str - empty doc string
#### Declared returns: `None`
## Function  `parse_docstring`
```text
sphinx doc string style
```
        
### Argument(s)
+ `doc_string`: Optional[str] - received function doc string
### Return
```text
parsed object
```
                    
#### Declared returns: `Optional[ParsedDocString]`
### SubElement(s)
 > ## Function  `parse_params_type`
 > ### Argument(s)
 > + `_params`: Dict[str, str] - empty doc string
 > + `_types`: Dict[str, str] - empty doc string
 > #### Declared returns: `Tuple[Dict[str, str], Dict[str, str]]`