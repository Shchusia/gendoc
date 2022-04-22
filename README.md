## ``gen_doc`` - library for generating documentation

### Installation

```commandline
pip install gen_doc
```

### What for?
+ aggregates all `.py` files to one (or same hierarchy folder) `.md` files
+ collects all classes and methods with information about them

### Details

```text
Usage: gen_doc [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  build  Build documentation
  init   To init config file for generating documentation.
```

```text
Usage: gen_doc init [OPTIONS]

  To init config file for generating documentation.

Options:
  -f, --file-config TEXT  Config file name  [default: gen_doc.yaml]
  -o, --overwrite         for overwriting if file exist
  --help                  Show this message and exit.
```

```text
Usage: gen_doc build [OPTIONS] [[py]]

  Build documentation

Options:
  -sm, --save-mode [md]      Save mode
  -hi, --hierarchically      Extract with same hierarchy
  -o, --overwrite            For overwriting if file exist
  -p2r, --path-to-root TEXT  Path to the directory for which documentation
                             should be compiled
  -p2s, --path-to-save TEXT  Path to the directory where to save docs
  -f2s, --file-to-save TEXT  Path to the directory where to save docs
  -c, --config               Config file name
  -f, --file-config TEXT     Config file name  [default: gen_doc.yaml]
  --help                     Show this message and exit.

```