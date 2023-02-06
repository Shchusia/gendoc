# Module `folder_general_information.py`
```text
General info of the repository
```

> Path: `gen_doc/models/folder_general_information.py`
## Class `GeneralInfo`
```text
Model with general information about the repository
```

### Basses(s)
+ BaseModel
### SubElement(s)
 > `title`: Optional[str] = Field(None, description='Title project')
 > `description`: Optional[str] = Field(None, description='Description project')
 > `author`: Optional[str] = Field(None, description='Name author')
 > `author_contacts`: Optional[List[str]] = Field(None, description='Contacts author')
 > `release`: Optional[str] = Field(None, description='Version release')
 > `repository_main_url`: Optional[str] = Field(None, description='Url to repository')