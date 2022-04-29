# Module `module.py`
```text
Models for module
```

> Path: `gen_doc\models\module.py`
## Class `EntityOfCode`
### Basses(s)
+ BaseModel
## Class `Entity`
### Basses(s)
+ EntityOfCode
### SubElement(s)
 > `e_type`: EnumTypeVariables = Field(None, description='Type of entity')
 > `e_value`: List[Union[Entity, Any]] = Field(None, description='Value of entity')
## Class `Module`
### Basses(s)
+ BaseModel
### SubElement(s)
 > `path_to_file`: Path = Field(description='Path to file from root folder')
 > `module_doc_string`: Optional[str] = Field(None, description='Doc string for module')
 > `list_entities`: List[EntityOfCode] = Field(None, description='Parsed entities')
## Class `Argument`
### Basses(s)
+ EntityOfCode
### SubElement(s)
 > `arg`: str = Field(description='Title argument')
 > `annotation`: Entity = Field(None, description='Parsed annotation to argument')
 > `type_comment`: Any = Field(None, description='Optional info about the argument')
## Class `Arguments`
### Basses(s)
+ EntityOfCode
### SubElement(s)
 > `args`: List[Argument] = Field(None, description='Parsed arguments')
 > `defaults`: List[Entity] = Field(None, description='Parsed default values of arguments')
 > `kw_defaults`: List[Entity] = Field(None, description='Parsed default values of kwarguments')
 > `kwarg`: Optional[Argument] = Field(None, description='Parsed **kwarg')
 > `vararg`: Optional[Argument] = Field(None, description='Parsed *args')
 > `posonlyargs`: List[Argument] = Field(None, description='Parsed position-only arguments')
 > `kwonlyargs`: List[Argument] = Field(None, description='Parsed keyword-only arguments')
## Class `Parameter`
### Basses(s)
+ BaseModel
### SubElement(s)
 > `param_name`: str = Field(None, description='Parsed parameter name')
 > `param_type`: str = Field(None, description='Parsed parameter type')
 > `param_description`: str = Field(None, description='Parsed parameter description')
## Class `ParsedDocString`
### Basses(s)
+ BaseModel
### SubElement(s)
 > `description`: str = Field(None, description='Parsed function description')
 > `args`: List[Parameter] = Field(None, description='Parsed arguments')
 > `raises`: List[Parameter] = Field(None, description='Parsed raises of function')
 > `returns`: Parameter = Field(None, description='Parsed return values of function')
 > `example`: str = Field(None, description='Parsed example')
## Class `Function`
### Basses(s)
+ EntityOfCode
### SubElement(s)
 > `function_name`: str = Field(None, description='Function name')
 > `function_doc_string`: str = Field(None, description='Function doc string')
 > `function_args`: Arguments = Field(None, description='Function arguments')
 > `function_decorators`: List[Entity] = Field(None, description='Function decorators')
 > `function_returns`: Entity = Field(None, description='What does the function return')
 > `function_type_comment`: Any = Field(None, description='Function type comment')
 > `function_is_async`: bool = Field(False, description='Is async function')
 > `function_entities`: List[EntityOfCode] = Field(None, description='Sub entities current function')
 > `function_parsed_docstring`: Optional[ParsedDocString] = Field(None, description='Docstring object resolved to object')
## Class `Assign`
### Basses(s)
+ EntityOfCode
### SubElement(s)
 > `name`: Entity = Field(None, description='Name variable')
 > `value`: Entity = Field(None, description='Value variable')
 > `annotation`: Entity = Field(None, description='Type annotation variable')
 > `type_comment`: Any = Field(None, description='Optional argument')
 > `simple`: Any = Field(None, description='Optional argument')
## Class `Class`
### Basses(s)
+ EntityOfCode
### SubElement(s)
 > `class_name`: str = Field(None, description='Class name')
 > `class_doc_string`: str = Field(None, description='Class doc string')
 > `class_decorators`: List[Entity] = Field(None, description='Class decorators')
 > `class_bases`: List[Entity] = Field(None, description='Class bases')
 > `class_keywords`: List[Assign] = Field(None, description='Class keywords')
 > `class_entities`: List[EntityOfCode] = Field(None, description='Sub entities current class')