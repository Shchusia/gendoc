"""
First example_file
"""
# pylint: disable=unused-argument, unnecessary-pass, invalid-name
import re
from abc import ABC, abstractmethod
from typing import Callable, Dict, List

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

assert val_1 > 0, "test"

REGEX = re.compile(r"hello world")


def decorator_factory(arg1: bool, arg2: int, arg3: float) -> Callable:
    """
    Decorator with args
    :param arg1:
    :param arg2:
    :param arg3:
    :return:
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
    async function
    :return:
    """
    pass


def function_without_doc_string(
    arg1,
    *args,
):
    pass


def function_posonlyargs(arg_1, /, arg_2, arg_3):
    pass


def function_kwonlyargs(arg_1, *, arg_2, arg_3):
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
    pass


class ExampleClass(ABC, metaclass=First):  # type: ignore
    """
    ExampleClass
    """

    _value: str = "example"
    _value_2 = 2

    @property
    def value(self):
        """
        property value
        :return:
        """
        return self._value

    @value.setter
    def value(self, value=1) -> None:
        """
        setter
        :param value:
        :return:
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
