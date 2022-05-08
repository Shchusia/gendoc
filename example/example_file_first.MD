# Module `example_file_first.py`
```text
First example_file
```

> Path: `example\example_file_first.py`
`BASE_VALUE` = 1
`CONST_VAL_FIRST`: str = "first_test_const_value"
`CONST_VAL_SECOND` = {
            "value": 1
            }
`CONST_VAL_THREAD` = [("value", 1), ("value2", 2)]
`val_1, val_2` = (1, 2)
`val_3, val_4` = CONST_VAL_THREAD
`val_5` = val_2 + val_1
`tmp_list` = [*range(4)]
`tmp_slice` = tmp_list[val_2:val_5]
`CONST_LAMBDA_FUNCTION` = lambda x: x ** 2
`REGEX` = re.compile('hello world')
## Function  `decorator_factory`
```text
Decorator with args
```
        
### Argument(s)
+ `arg1`: bool - argument 1
+ `arg2`: int - argument 2
+ `arg3`: float - argument 3
### Return
```text
callable
```
                    
#### Declared returns: `Callable`
### Example 
```python
>>> import time
>>> time.sleep(2)
```

### SubElement(s)
 > ## Function  `decorator`
 > ### Argument(s)
 > + `function` - empty doc string
 > ### SubElement(s)
 > > ## Function  `wrapper`
 > > ### Argument(s)
 > > + *`args` - empty doc string
 > > + **`kwargs` - empty doc string
## Function `async` `async_function_with_doc_string`
```text
function doc string with sphinx style
with long description
```
        
### Return
```text
what return function
```
                    
#### Declared returns: `type returned value`
### Yield
```text
if yield function
```

#### Declared yields: `for yield value`
### Example 
```python
>>> import this
>>> # and other imports
```

### Note 
```
note string
with some information
```

### ToDo(s) 
+ todo1
+ todo2
with description
## Function  `function_without_doc_string`
### Argument(s)
+ `arg1` - empty doc string
+ *`args` - empty doc string
## Function  `function_google_docstring`
```text
function doc string with google style
with long description
```
        
### Argument(s)
+ `val1`: int - empty doc string
+ `val2`: List[Tuple[str, str]] - empty doc string
### Raise(s)
+ `AttributeError` - The ``Raises`` section is a list of all exceptions
that are relevant to the interface.
### Return
```text
A dict value description
```
                    
#### Declared returns: `Dict[str, str]`
### Extra Parameter(s) 
+ `Google Python Style Guide` - http://google.github.io/styleguide/pyguide.html 
+ `PEP 484` - https://www.python.org/dev/peps/pep-0484/ 
### Example 
```python
Examples should be written in doctest format, and should illustrate how
to use the function.
>>> print([i for i in example_generator(4)])
[0, 1, 2, 3]
```

### Note 
```
Do not include the `self` parameter in the ``Args`` section.
```

### ToDo(s) 
+ For module TODOs
+ You have to also use
``sphinx.ext.todo`` extension
## Function  `function_posonlyargs`
### Argument(s)
+ `arg_1` - empty doc string
+ `arg_2` - empty doc string
+ `arg_3` - empty doc string
## Function  `function_kwonlyargs`
### Argument(s)
+ `arg_1` - empty doc string
+ `arg_2` - empty doc string
+ `arg_3` - empty doc string
## Function  `test_func`
```text
Test function with decorator with parameters
```
        
### Decorator(s)
+ decorator_factory(True, 2, arg3=3)
### Argument(s)
+ `arg` - empty doc string
+ *`args` - empty doc string
+ **`kwargs` - empty doc string
#### Declared returns: `List[Dict]`
### Example 
```python
>>> test_func(123)
None
```

## Class `First`
```text
example class
```

### Basses(s)
+ ABC
## Class `Second`
```text
Class with google doc style
```

### Attributes(s)
+ attribute_1`:int - 
+ description attribute_1
    attribute_2`:List[int] - description attribute_2
### Example 
```python
Examples should be written in doctest format, and should illustrate how
to use the function.
>>> sec_class = Second()
>>> sec_class.attribute_1
1
```

### Note 
```text
Do not include the `self` parameter in the ``Args`` section.
```

### SubElement(s)
 > ## Function  `__init__`
## Class `ExampleClass`
```text
ExampleClass
```

### Basses(s)
+ ABC
### Keywords(s)
+ `metaclass` = First
### SubElement(s)
 > `_value`: str = "example"
 > `_value_2` = 2
 > ## Function  `value`
 > ```text
 > property value
 > ```
 > 
 > ### Decorator(s)
 > + property
 > ### Return
 > ```text
 > value
 > ```
 > 
 > #### Declared returns: `str`
 > ## Function  `value`
 > ```text
 > setter
 > ```
 > 
 > ### Decorator(s)
 > + value.setter
 > ### Argument(s)
 > + `value`: str - empty doc string
 > ## Function  `test_func`
 > ```text
 > class test function
 > ```
 > 
 > ### Decorator(s)
 > + abstractmethod
 > ## Function  `test_static`
 > ```text
 > test staticmethod
 > ```
 > 
 > ### Decorator(s)
 > + staticmethod
 > ### Argument(s)
 > + `value`: int - empty doc string
 > + `arg_1`: Dict - empty doc string
 > + `arg_2`: List[Dict] - empty doc string
 > #### Declared returns: `Dict[str, str]`
 > ## Function `async` `run`
 > ```text
 > async function
 > ```
 > 
 > ### Argument(s)
 > + `arg`: int - empty doc string
 > #### Declared returns: `int`