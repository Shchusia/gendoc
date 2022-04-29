# Module `parser.py`
```text
Module with base file parser
```

> Path: `gen_doc\extensions\parser.py`
## Class `GenDocParser`
```text
Base class for parsers
```

### Basses(s)
+ ABC
### SubElement(s)
 > ## Function  `__init__`
 > ### Argument(s)
 > + `logger`: Optional[Logger] - empty doc string
 > + `path_to_root_folder`: Optional[Union[Path, str]] - empty doc string
 > + `additional_files_to_ignore`: Optional[List[str]] - empty doc string
 > + `additional_folders_to_ignore`: Optional[List[str]] - empty doc string
 > #### Declared returns: `None`
 > ## Function  `language`
 > ```text
 > Property for which language
 > ```
 > 
 > ### Decorator(s)
 > + property
 > ### Return
 > ```text
 > str language
 > ```
 > 
 > #### Declared returns: `str`
 > ### Example
 > ```python
 > >>> language = "python"
 > ```
 > ## Function  `short_name`
 > ```text
 > Property for short name in commands
 > ```
 > 
 > ### Decorator(s)
 > + property
 > ### Return
 > ```text
 > str short name
 > ```
 > 
 > #### Declared returns: `str`
 > ### Example
 > ```python
 > >>> short_name = "py"  # for python
 > ```
 > ## Function  `types_of_file_to_process`
 > ```text
 > Property for concrete language
 > type of documents for which to create documentation
 > ```
 > 
 > ### Decorator(s)
 > + property
 > ### Return
 > ```text
 > is list of string types to build docs
 > ```
 > 
 > #### Declared returns: `List[str]`
 > ### Example
 > ```python
 > >>> types_of_file_to_process = ['.py']  # for python
 > ```
 > ## Function  `files_to_ignore`
 > ```text
 > Which files names will not be considered
 > ```
 > 
 > ### Decorator(s)
 > + property
 > ### Return
 > ```text
 > list of files that should not be processed
 > ```
 > 
 > #### Declared returns: `None`
 > ### Example
 > ```python
 > >>> files_to_ignore = ['setup.py'] # for python
 > ```
 > ## Function  `folders_to_ignore`
 > ```text
 > Which folder names will not be considered
 > ```
 > 
 > ### Decorator(s)
 > + property
 > ### Return
 > ```text
 > list of folders that should not be processed
 > ```
 > 
 > #### Declared returns: `None`
 > ### Example
 > ```python
 > >>> folders_to_ignore = ['__pycache__'] # for python
 > ```
 > ## Function  `parse_file`
 > ### Decorator(s)
 > + abstractmethod
 > ### Argument(s)
 > + `path_to_file`: Path - empty doc string
 > #### Declared returns: `None`
 > ## Function  `parse`
 > ```text
 > Method parses all nested files and folders if
 > they are not in the exclusion
 > ```
 > 
 > ### Return
 > ```text
 > list of parsed modules
 > ```
 > 
 > #### Declared returns: `List[Module]`
 > ## Function  `_is_correct_folder_to_process`
 > ```text
 > Method to check if the specified directory
 > should be processed
 > ```
 > 
 > ### Decorator(s)
 > + staticmethod
 > ### Argument(s)
 > + `folder`: str - current folder to process
 > + `folders_to_ignore`: List[str] - folders in exclusion
 > ### Return
 > ```text
 > true if folder needs to be processed
 > ```
 > 
 > #### Declared returns: `bool`