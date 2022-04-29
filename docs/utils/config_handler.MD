# Module `config_handler.py`
```text
Module with functions work with  config
```

> Path: `gen_doc\utils\config_handler.py`
## Function  `normalize_name_config`
```text
Help function to normalize and rename the file
```
        
### Argument(s)
+ `file_name_to_save`: str - name file
### Return
```text
path to file
```
                    
#### Declared returns: `Path`
## Function  `load_config`
```text
Method to parse the config file
```
        
### Argument(s)
+ `file_name_to_save`: str - path to file config
### Return
```text
config if exists
```
                    
#### Declared returns: `Optional[Dict[str, Any]]`
## Function  `copy_config`
```text
Method to copy config template
```
        
### Argument(s)
+ `file_name_to_save`: str - name config
+ `overwrite`: bool - is overwriting config if exist
### Return
```text
is correct
```
                    
#### Declared returns: `bool`