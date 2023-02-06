# Module `python_parser.py`
```text
Module with parser for python files
Sphinx docstrings
```

> Path: `gen_doc/extensions/python/python_parser.py`
`ARGUMENTS_TO_IGNORE` = ["self"]
## Class `GenDocPythonParser`
```text
Class to retrieve information about the python module
```

### Basses(s)
+ GenDocParser
### SubElement(s)
 > `language` = "python"
 > `short_name` = "py"
 > `types_of_file_to_process` = [".py"]
 > `folders_to_ignore` = ["__pycache__", ".git", "venv", "build", "dist", ".mypy_cache", ".idea"]
 > `files_to_ignore` = ["setup.py"]
 > ## Function  `_parse_body`
 > ```text
 > Method to parse object body for parse child
 > ```
 > 
 > ### Argument(s)
 > + `obj`: Union[ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef] - obj to process
 > + `is_inner`: bool - empty doc string
 > ### Return
 > ```text
 > parsed body
 > ```
 > 
 > #### Declared returns: `List[EntityOfCode]`
 > ## Function  `_parse_obj`
 > ```text
 > Method to define the handler object
 > the method contains all the objects for analysis
 > ```
 > 
 > ### Argument(s)
 > + `obj`: stmt - object to process if exist handler
 > + `is_inner`: bool - empty doc string
 > ### Return
 > ```text
 > type, info
 > ```
 > 
 > #### Declared returns: `Optional[EntityOfCode]`
 > ## Function  `_parse_value`
 > ```text
 > Method to parse expression
 > ```
 > 
 > ### Argument(s)
 > + `obj`: ast.expr - obj to parse
 > ### Return
 > ```text
 > parsed entity
 > ```
 > 
 > #### Declared returns: `Entity`
 > ## Function  `_parse_assign`
 > ```text
 > Parsing assigner
 > ```
 > 
 > ### Argument(s)
 > + `obj`: Union[ast.Assign, ast.AnnAssign] - object for Parsing Assigner
 > ### Return
 > ```text
 > parsed all assigned
 > ```
 > 
 > #### Declared returns: `Assign`
 > ## Function  `_parse_class`
 > ```text
 > Method to parse a class
 > ```
 > 
 > ### Argument(s)
 > + `obj`: ast.ClassDef - current class to parse info from
 > ### Return
 > ```text
 > processed class
 > ```
 > 
 > #### Declared returns: `Class`
 > ## Function  `_parse_decorators`
 > ```text
 > Method to get decorators of a class or a function
 > ```
 > 
 > ### Argument(s)
 > + `obj`: Union[ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef] - current object to parse info from
 > ### Return
 > ```text
 > list of decorators
 > ```
 > 
 > #### Declared returns: `List[Entity]`
 > ## Function  `_parse_basses`
 > ```text
 > Method to parse bases for the current class
 > ```
 > 
 > ### Argument(s)
 > + `obj`: ast.ClassDef - current class to parse info from
 > ### Return
 > ```text
 > list of bases classes
 > ```
 > 
 > #### Declared returns: `List[Entity]`
 > ## Function  `_parse_keywords`
 > ```text
 > Parse of keywords
 > ```
 > 
 > ### Argument(s)
 > + `obj`: ast.ClassDef - current class to parse info from
 > ### Return
 > ```text
 > list parsed keywords
 > ```
 > 
 > #### Declared returns: `List[Assign]`
 > ## Function  `_parse_function`
 > ```text
 > Method to parse functions
 > ```
 > 
 > ### Argument(s)
 > + `obj`: Union[ast.FunctionDef, ast.AsyncFunctionDef] - current function to parse info from
 > ### Return
 > ```text
 > parsed function object
 > ```
 > 
 > #### Declared returns: `Function`
 > ## Function  `_parse_arguments`
 > ```text
 > Method to parse arguments functions
 > ```
 > 
 > ### Argument(s)
 > + `obj`: ast.arguments - current function to parse info from
 > ### Return
 > ```text
 > parsed arguments of function
 > ```
 > 
 > #### Declared returns: `Arguments`
 > ## Function  `_parse_file`
 > ```text
 > Main processing method
 > Reads the file and starts the parsing process
 > ```
 > 
 > ### Argument(s)
 > + `path_to_file`: Path - path to the file to be processed
 > ### Return
 > ```text
 > module with extracted information from the input file
 > ```
 > 
 > #### Declared returns: `Module`
 > ## Function  `parse_file`
 > ```text
 > Method for parsing python modules
 > ```
 > 
 > ### Argument(s)
 > + `path_to_file`: Path - path to current file to parse info from
 > ### Return
 > ```text
 > parsed module
 > ```
 > 
 > #### Declared returns: `Module`