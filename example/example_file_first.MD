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
 > #### Declared returns: `None`
 > ### SubElement(s)
 > > ## Function  `wrapper`
 > > ### Argument(s)
 > > + *`args` - empty doc string
 > > + **`kwargs` - empty doc string
 > > #### Declared returns: `None`
## Function `async` `async_function_with_doc_string`
```text
async function
```
        
### Raise(s)
+ `RunTimeError` - error in run
#### Declared returns: `None`
### Example 
```python
>>> import time
>>> time.sleep(2)
```

## Function  `function_without_doc_string`
### Argument(s)
+ `arg1` - empty doc string
+ *`args` - empty doc string
#### Declared returns: `None`
## Function  `function_posonlyargs`
### Argument(s)
+ `arg_1` - empty doc string
+ `arg_2` - empty doc string
+ `arg_3` - empty doc string
#### Declared returns: `None`
## Function  `function_kwonlyargs`
### Argument(s)
+ `arg_1` - empty doc string
+ `arg_2` - empty doc string
+ `arg_3` - empty doc string
#### Declared returns: `None`
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
## Class `ExampleClass`
```text
ExampleClass
```

### Basses(s)
+ ABC
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
 > ### Argument(s)
 > + `self` - empty doc string
 > #### Declared returns: `None`
 > ## Function  `value`
 > ```text
 > setter
 > ```
 > 
 > ### Decorator(s)
 > + value.setter
 > ### Argument(s)
 > + `self` - empty doc string
 > + `value` - empty doc string
 > #### Declared returns: `None`
 > ## Function  `test_func`
 > ```text
 > class test function
 > ```
 > 
 > ### Decorator(s)
 > + abstractmethod
 > ### Argument(s)
 > + `self` - empty doc string
 > #### Declared returns: `None`
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
 > + `self` - empty doc string
 > + `arg`: int - empty doc string
 > #### Declared returns: `int`