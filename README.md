## ``gen_doc`` - library for generating documentation

### Installation

```commandline
pip install gen_doc
```

### What for?
+ aggregates all `.py` files to one (or same hierarchy folder) `.md` files
+ collects all classes and methods with information about them

### How to use:

+ install the library
+ open the terminal in the folder with the project for which you want to create documentation
+ run the command `gen_doc init`
+ make changes to the config file
+ run the command `gen_doc build -c`

### Details

#### General
```text
Usage: gen_doc [OPTIONS] COMMAND [ARGS]...

  Utility for generating project documentation from docstrings

Options:
  --help  Show this message and exit.

Commands:
  build  Build documentation
  init   To init config file in order to generate documentation.
```
#### Init
```text
Usage: gen_doc init [OPTIONS]

  To init config file in order to generate documentation.

Options:
  -f, --file-config TEXT  Config file name  [default: gen_doc.yaml]
  -o, --overwrite         For overwriting if the file exists
  --help                  Show this message and exit.

```
#### Build
```text
Usage: gen_doc build [OPTIONS] [[py]]

  Build documentation

Options:
  -sm, --save-mode [md]      Save mode
  -hi, --hierarchically      Extract with the same hierarchy
  -o, --overwrite            For overwriting if the file exists
  -p2r, --path-to-root TEXT  Path to the directory for which documentation
                             should be compiled
  -p2s, --path-to-save TEXT  Path to the directory where the documentation
                             should be saved
  -f2s, --file-to-save TEXT  Path to the directory where the documentation
                             should be saved
  -c, --config               Use config for build documentation.
  -f, --file-config TEXT     Config file name  [default: gen_doc.yaml]
  --help                     Show this message and exit.
```