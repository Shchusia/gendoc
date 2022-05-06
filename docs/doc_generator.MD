# Module `doc_generator.py`
```text
Main module with the class that works with the catalog
```

> Path: `gen_doc\doc_generator.py`
## Class `DocGenerator`
```text
Class for generating project documentation
```

### SubElement(s)
 > ## Function  `__init__`
 > ```text
 > Init config loader
 > ```
 > 
 > ### Argument(s)
 > + `logger`: Optional[Logger] - Logger
 > + `path_to_root_folder`: Optional[Union[Path, str]] - Path to the directory for which the
 > documentation should be compiled
 > + `extract_with_same_hierarchy`: Optional[bool] - If False extract all into one file
 > if True create file for each file'
 > + `overwrite_if_file_exists`: Optional[bool] - To overwrite if the file exists
 > + `path_to_save`: Optional[Path] - Path to the directory where the documentation
 > should be saved
 > + `file_to_save`: Optional[Union[str, Path]] - name_file to save
 > + `save_mode`: Optional[str] - Save mode
 > + `parse_mode`: Optional[str] - empty doc string
 > + `title`: Optional[str] - Title for the header
 > + `description`: Optional[str] - Description project
 > + `repository_main_url`: Optional[str] - URL of the repository where this project
 > is located
 > + `author`: Optional[str] - Author of the documented project
 > + `author_contacts`: Optional[List[str]] - Author contacts
 > + `release`: Optional[str] - Release project
 > + `additional_files_to_ignore`: Optional[List[str]] - Additional files that should not
 > be included in the documentation
 > + `additional_folders_to_ignore`: Optional[List[str]] - Additional directories that should
 > not be included in the documentation
 > ## Function  `generate`
 > ```text
 > Function to run process generate documentation
 > ```
 > 
 > ### Return
 > ```text
 > nothing
 > ```
 > 