import inspect
from typing import Dict

import gendoc.extensions as extensions
from gendoc import DocGenerator


def get_extensions() -> Dict[str, DocGenerator]:
    """
    Method build dict existed extensions for doc generator
    :return: dict[short_name: doc_generator
    """
    _val = dict()  # type: Dict[str, DocGenerator]
    for _, clazz in inspect.getmembers(extensions, inspect.isclass):
        if _val.get(clazz.short_name):
            raise ValueError("not unique command")
        _val[clazz.short_name] = clazz
    return _val
