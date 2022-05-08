"""
First example_file
"""
# pylint: disable=unused-argument, unnecessary-pass, invalid-name
import re
from abc import ABC, abstractmethod
from typing import Callable, Dict, List, Tuple

BASE_VALUE = 1  # type: int
CONST_VAL_FIRST: str = "first_test_const_value"
CONST_VAL_SECOND = {"value": 1}
CONST_VAL_THREAD = [
    ("value", 1),
    ("value2", 2),
]

val_1, val_2 = 1, 2
val_3, val_4 = CONST_VAL_THREAD
val_5 = val_1 + val_2

tmp_list = [*range(4)]
tmp_slice = tmp_list[val_2:val_5]

CONST_LAMBDA_FUNCTION = lambda x: x ** 2  # noqa

REGEX = re.compile(r"hello world")


def decorator_factory(arg1: bool, arg2: int = 1, arg3: float = 1) -> Callable:
    """
    Decorator with args
    :param arg1: argument 1
    :param arg2: argument 2
    :param arg3: argument 3
    :return: callable
    .. code-block:: python
    >>> import time
    >>> time.sleep(2)
    """

    def decorator(function):
        def wrapper(*args, **kwargs):
            if arg1:
                result = function(arg2, *args, **kwargs)
            else:
                result = function(arg3, *args, **kwargs)
            return result

        return wrapper

    return decorator


async def async_function_with_doc_string():
    """
    function doc string with sphinx style
    with long description

    :param value1: description to value1
    :type value1: str
    :param List[str] value2: description to value2
    :attr value3: description to value3
    :type value3: Dict[str, str]
    :attr List[Tuple[str, str]] value4: description to value3
    :return: what return function
    :rtype: type returned value
    :yield: if yield function
    :ytype: for yield value
    :note: note string
    with some information
    :todo: todo1
    :todo: todo2
    with description
    :example:
    >>> import this
    >>> # and other imports

    """
    pass


def function_without_doc_string(
    arg1,
    *args,
):
    pass


def function_google_docstring(val1: int, val2: List[Tuple[str, str]]) -> Dict[str, str]:
    """
    function doc string with google style
        with long description

    Args:
        val1 (int): description
        val2 (List[Tuple[str,str]]): Long description
    Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions
            that are relevant to the interface.
    Returns:
        Dict[str, str]: A dict value description
    Todo:
        * For module TODOs
        * You have to also use
          ``sphinx.ext.todo`` extension
    .. _Google Python Style Guide:
        http://google.github.io/styleguide/pyguide.html
    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/
    Note:
        Do not include the `self` parameter in the ``Args`` section.
    Example:
        Examples should be written in doctest format, and should illustrate how
        to use the function.
        >>> print([i for i in example_generator(4)])
        [0, 1, 2, 3]
    """


def function_posonlyargs(arg_1, /, arg_2, arg_3):
    pass


def function_kwonlyargs(arg_1, *, arg_2, arg_3):
    """

    :param arg_1:
    :param arg_2:
    :param arg_3:
    :return:
    :example:
    """
    pass


# function_posonlyargs(1, 2, arg_2=3)


@decorator_factory(True, 2, arg3=3)
def test_func(arg, *args, **kwargs) -> List[Dict]:
    """
    Test function with decorator with parameters
    :param arg:
    :param args:
    :param kwargs:
    :return:
    :example:
    >>> test_func(123)
    None
    """
    pass


class First(ABC):
    """
    example class
    """


class Second:
    """
    Class with google doc style
    Attributes:
        attribute_1 (int): description attribute_1
        attribute_2 (List[int]): description attribute_2
    Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions
            that are relevant to the interface.
    Note:
        Do not include the `self` parameter in the ``Args`` section.
    Example:
        Examples should be written in doctest format, and should illustrate how
        to use the function.
        >>> sec_class = Second()
        >>> sec_class.attribute_1
        1
    """

    def __init__(self):
        self.attribute_1 = 1
        self.attribute_2 = list()

    pass


class ExampleClass(ABC, metaclass=First):  # type: ignore
    """
    ExampleClass
    """

    _value: str = "example"
    _value_2 = 2

    @property
    def value(self) -> str:
        """
        property value
        :return: value
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str = "new_str") -> None:
        """
        setter
        :param value:
        """
        self._value = value

    @abstractmethod
    def test_func(self):
        """
        class test function
        :return:
        """
        raise NotImplementedError

    @staticmethod
    def test_static(value: int, arg_1: Dict, arg_2: List[Dict]) -> Dict[str, str]:
        """
        test staticmethod
        :return:
        """
        pass

    async def run(self, arg: int = 1) -> int:
        """
        async function
        :param arg:
        :return:
        """
        pass
