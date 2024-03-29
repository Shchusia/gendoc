# Module `commands.py`
```text
commands to build documentation
```

> Path: `gen_doc/commands.py`
## Function  `entry_point`
### Decorator(s)
+ click.group(help='Utility for generating project documentation from docstrings', cls=GroupWithCommandOptions, context_settings=dict(ignore_unknown_options=True))
+ click.option('-v', '--version', 'version', is_flag=True, required=False, default=False, help='Get library version', type=bool)
+ click.option('-i', '--init', 'init_var', is_flag=True, required=False, default=False, help='Init gen_doc config with default parameters', type=bool)
+ click.option('-b', '--build', 'build_var', is_flag=True, required=False, default=False, help='Build documentation by config', type=bool)
+ click.pass_context
### Argument(s)
+ `ctx` - empty doc string
+ `version` - empty doc string
+ `init_var` - empty doc string
+ `build_var` - empty doc string
## Function  `init`
### Decorator(s)
+ entry_point.command('init', help='To init config file in order to generate documentation.', context_settings=dict(ignore_unknown_options=True))
+ click.option('-f', '--file-config', 'file_config', show_default=True, required=False, default='gen_doc.yaml', help='Config file name', type=str)
+ click.option('-o', '--overwrite', 'overwrite', is_flag=True, required=False, default=False, help='To overwrite, in case file already exists', type=bool)
### Argument(s)
+ `file_config`: str - empty doc string
+ `overwrite`: bool - empty doc string
+ *`args` - empty doc string
+ **`kwargs` - empty doc string
## Function  `build`
### Decorator(s)
+ entry_point.command('build', help='Build documentation', context_settings=dict(ignore_unknown_options=True))
+ click.argument('language', required=False, default='py', type=click.Choice([i.name for i in GenDocParsers]))
+ click.option('-sm', '--save-mode', 'save_mode', required=False, default='md', help='Save mode', type=click.Choice([i.name for i in GenDocSerializers]))
+ click.option('-hi', '--hierarchically', 'hierarchically', is_flag=True, required=False, default=True, help='Extract with the same hierarchy', type=bool)
+ click.option('-o', '--overwrite', 'overwrite', is_flag=True, required=False, default=True, help='To overwrite, in case file already exists', type=bool)
+ click.option('-p2r', '--path-to-root', 'path_to_root', required=False, default=None, help='Path to the directory for which documentation should be compiled', type=str)
+ click.option('-p2s', '--path-to-save', 'path_to_save', required=False, default=None, help='Path to the directory where the documentation should be saved', type=str)
+ click.option('-f2s', '--file-to-save', 'file_to_save', required=False, default=None, help='Path to the directory where the documentation should be saved', type=str)
+ click.option('-c', '--config', 'config', is_flag=True, required=False, default=False, help='Use config for build documentation.', type=bool)
+ click.option('-f', '--file-config', 'file_config', show_default=True, required=False, default='gen_doc.yaml', help='Config file name', type=str)
### Argument(s)
+ `language` - empty doc string
+ `save_mode` - empty doc string
+ `path_to_root` - empty doc string
+ `config` - empty doc string
+ `hierarchically` - empty doc string
+ `overwrite` - empty doc string
+ `path_to_save` - empty doc string
+ `file_to_save` - empty doc string
+ `file_config` - empty doc string
+ *`args` - empty doc string
+ **`kwargs` - empty doc string