"""
Setup GenDoc
"""
import os
import pathlib
import re
from typing import Optional

from setuptools import setup

LIB_NAME = "gen_doc"
HERE = pathlib.Path(__file__).parent


def get_version() -> Optional[str]:
    """
      Method for getting the version of the library from the init file
    :requirements: version must be specified separately
        :good: __version__ = '0.0.1'
        :bad: __version__, __any_variable__ = '0.0.1', 'any_value'
    :return: version lib
    """

    txt = (HERE / LIB_NAME / "__init__.py").read_text("utf-8")
    txt = txt.replace("'", '"')
    try:
        version = re.findall(r'^__version__ = "([^"]+)"\r?$', txt, re.M)[0]
        return version
    except IndexError:
        raise RuntimeError("Unable to determine version.")


def get_packages():
    """
    Method get packages for apply into lib
    """
    ignore = ["__pycache__"]

    list_sub_folders_with_paths = [
        x[0].replace(os.sep, ".")
        for x in os.walk(LIB_NAME)
        if x[0].split(os.sep)[-1] not in ignore
    ]
    return list_sub_folders_with_paths


setup(
    name=LIB_NAME,
    version=get_version(),
    description="Module for build documentation",
    author="Denis Shchutkiy",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author_email="denisshchutskyi@gmail.com",
    url="https://github.com/Shchusia/gendoc",
    packages=get_packages(),
    keywords=["pip", LIB_NAME],
    python_requires=">=3.7",
    entry_points={"console_scripts": ["gen_doc=gen_doc.commands:entry_point"]},
    package_data={
        f"{LIB_NAME}.src": [
            "*.yaml",
        ]
    },
    install_requires=[
        "click==8.1.2",
        "pydantic==1.9.0",
        "PyYAML==6.0",
    ],
)
