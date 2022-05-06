# Module `base_parser.py`
```text
Module with base class for parsers
```

> Path: `gen_doc\extensions\python\utils\base_parser.py`
## Class `PythonDocStringParser`
```text
Base class for all parsers
```

### Basses(s)
+ ABC
### SubElement(s)
 > ## Function  `example`
 > ```text
 > Example of a string with all available and correctly spelled attributes
 > ```
 > 
 > ### Decorator(s)
 > + property
 > ### Return
 > ```text
 > example str
 > ```
 > 
 > #### Declared returns: `str`
 > ## Function  `parse`
 > ```text
 > Method to parse a Python doc string
 > ```
 > 
 > ### Decorator(s)
 > + staticmethod
 > + abstractmethod
 > ### Argument(s)
 > + `doc_string`: Optional[str] - extracted doc string
 > ### Return
 > ```text
 > parsed object
 > ```
 > 
 > #### Declared returns: `Optional[ParsedDocString]`