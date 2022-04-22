import logging
from pathlib import Path
from shutil import copyfile
from typing import Any, Dict, Optional

import yaml  # type: ignore  # noqa


def normalize_name_config(file_name_to_save: str) -> Path:
    """
    Help function for normalizing and convert file name
    :param str file_name_to_save: name file
    :return: path to file
    """
    path_to_save = Path(file_name_to_save)
    if path_to_save.suffix != ".yaml":
        path_to_save = Path(path_to_save.name + ".yaml")
    return path_to_save


def load_config(file_name_to_save: str) -> Optional[Dict[str, Any]]:
    """
    method parse config file
    :param str file_name_to_save:
    :return: config if exists
    """
    path_to_config_file = normalize_name_config(file_name_to_save)
    if not path_to_config_file.is_file():
        return None
    try:
        with open(normalize_name_config(file_name_to_save), "r") as file:
            config = yaml.safe_load(file)
        return config
    except Exception as exc:
        logging.warning("Error in time load config. Error: %s", str(exc), exc_info=True)
    return dict()


def copy_config(file_name_to_save: str, overwrite: bool) -> bool:
    """
    Method to copy config template
    :param str file_name_to_save: name config
    :param bool overwrite: is overwriting config if exist
    :return: is correct
    """
    config_path = (
        Path(__file__).absolute().parent.parent / Path("src") / Path("template.yaml")
    )
    path_to_config_file = normalize_name_config(file_name_to_save)
    if path_to_config_file.is_file():
        if not overwrite:
            print("Such file already exists. To replace use the command '-o'")
            return False
    copyfile(config_path, path_to_config_file)
    return True
