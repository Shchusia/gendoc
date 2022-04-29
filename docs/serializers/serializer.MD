# Module `serializer.py`
```text
Module with base class for the serializers
```

> Path: `gen_doc\serializers\serializer.py`
## Class `GenDocSerializer`
```text
Base class for the serializers
```

### Basses(s)
+ ABC
### SubElement(s)
 > ## Function  `__init__`
 > ### Argument(s)
 > + `path_to_save`: Optional[Path] - empty doc string
 > + `root_folder`: Optional[Path] - empty doc string
 > + `logger`: Optional[Logger] - empty doc string
 > + `language`: Optional[str] - empty doc string
 > + `extract_with_same_hierarchy`: Optional[bool] - empty doc string
 > + `overwrite_if_file_exists`: Optional[bool] - empty doc string
 > + `file_to_save`: Optional[Union[str, Path]] - empty doc string
 > + `general_info`: Optional[GeneralInfo] - empty doc string
 > #### Declared returns: `None`
 > ## Function  `suffix_file`
 > ```text
 > File type for which this serializer is intended
 > ```
 > 
 > ### Decorator(s)
 > + property
 > ### Return
 > ```text
 > ".type"
 > ```
 > 
 > #### Declared returns: `str`
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
 > >>> short_name = "md"
 > ```
 > ## Function  `serialize_module`
 > ```text
 > Main method for serialize module
 > method to implement in child classes
 > ```
 > 
 > ### Decorator(s)
 > + abstractmethod
 > ### Argument(s)
 > + `module`: Module - object of module
 > + *`args`None - Optional arguments
 > + **`kwargs`None - Optional keyword arguments
 > ### Return
 > ```text
 > serialized module to list of string
 > ```
 > 
 > #### Declared returns: `List[str]`
 > ## Function  `serialize_general_info`
 > ```text
 > Method serialize general info
 > ```
 > 
 > ### Decorator(s)
 > + abstractmethod
 > #### Declared returns: `List[str]`
 > ## Function  `serialize`
 > ```text
 > Serialize parsed modules
 > ```
 > 
 > ### Argument(s)
 > + `modules`: List[Module] - list parsed modules
 > ### Return
 > ```text
 > nothing
 > ```
 > 
 > #### Declared returns: `None`
 > ## Function  `_save_documentation_file`
 > ```text
 > Method to save data to a file
 > ```
 > 
 > ### Argument(s)
 > + `path_to_save`: Path - path to file
 > + `data_to_save`: List[str] - empty doc string
 > ### Return
 > ```text
 > nothing
 > ```
 > 
 > #### Declared returns: `None`