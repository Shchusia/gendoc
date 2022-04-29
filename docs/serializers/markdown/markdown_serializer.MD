# Module `markdown_serializer.py`
```text
Markdown serializer
```

> Path: `gen_doc\serializers\markdown\markdown_serializer.py`
## Class `MarkdownSerializer`
```text
Module convert parsed to pretty markdown format
```

### Basses(s)
+ GenDocSerializer
### SubElement(s)
 > `short_name` = "md"
 > `suffix_file` = ".MD"
 > ## Function  `serialize_general_info`
 > ```text
 > Serialize general info
 > ```
 > 
 > #### Declared returns: `List[str]`
 > ## Function  `serialize_module`
 > ### Argument(s)
 > + `module`: Module - empty doc string
 > + *`args` - empty doc string
 > + **`kwargs` - empty doc string
 > #### Declared returns: `List[str]`
 > ## Function  `module_to_markdown_string`
 > ```text
 > Serializer Module to markdown
 > ```
 > 
 > ### Argument(s)
 > + `module`: Module - empty doc string
 > ### Return
 > ```text
 > serialized module to list[str]
 > ```
 > 
 > #### Declared returns: `List[str]`
 > ## Function  `convert_module_data`
 > ```text
 > Convert base info of module
 > ```
 > 
 > ### Argument(s)
 > + `module`: Module - module to convert
 > ### Return
 > ```text
 > list of markdown
 > ```
 > 
 > #### Declared returns: `List[str]`
 > ## Function  `convert_entity_of_code`
 > ### Argument(s)
 > + `entity_of_code`: EntityOfCode - entity of code
 > ### Return
 > ```text
 > serialized entity
 > ```
 > 
 > #### Declared returns: `List[str]`
 > ## Function  `convert_assign`
 > ```text
 > Convert assign
 > ```
 > 
 > ### Argument(s)
 > + `entity_assign`: Assign - Assign object
 > ### Return
 > ```text
 > Serialized Assign
 > ```
 > 
 > #### Declared returns: `List[str]`
 > ## Function  `convert_class`
 > ```text
 > Method serialize class
 > ```
 > 
 > ### Argument(s)
 > + `entity_class`: Class - entity class
 > ### Return
 > ```text
 > serialized class
 > ```
 > 
 > #### Declared returns: `List[str]`
 > ## Function  `convert_function`
 > ```text
 > Method to convert Function
 > ```
 > 
 > ### Argument(s)
 > + `entity_function`: Function - entity function
 > ### Return
 > ```text
 > serialized function
 > ```
 > 
 > #### Declared returns: `List[str]`
 > ### SubElement(s)
 > > ## Function  `convert_parse_docs`
 > > ### Argument(s)
 > > + `parse_docs`: Optional[ParsedDocString] - empty doc string
 > > #### Declared returns: `Dict[str, Any]`
 > > ## Function  `get_arg_str`
 > > ### Argument(s)
 > > + `arg_name`: Argument - empty doc string
 > > + `_converted_doc_string` - empty doc string
 > > #### Declared returns: `str`
 > > ## Function  `convert_args`
 > > ### Argument(s)
 > > + `args`: List[Argument] - empty doc string
 > > + `_converted_doc_string` - empty doc string
 > > #### Declared returns: `None`
 > ## Function  `convert_sub_code`
 > ### Argument(s)
 > + `entity`: EntityOfCode - empty doc string
 > #### Declared returns: `str`
 > ## Function  `convert_entity`
 > ```text
 > Convert entities
 > ```
 > 
 > ### Argument(s)
 > + `entity`: Optional[Entity] - entity
 > ### Return
 > ```text
 > Optional[str] base str
 > ```
 > 
 > #### Declared returns: `Optional[str]`