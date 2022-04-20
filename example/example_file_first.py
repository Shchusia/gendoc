"""
First example_file
"""
# pylint: disable=unused-argument, unnecessary-pass
from abc import ABC, abstractmethod
from typing import Callable, Dict, List

CONST_VAL_FIRST = "first_test_const_value"
CONST_VAL_SECOND = {"value": 1}
CONST_VAL_THREAD = [
    ("value", 1),
    ("value2", 2),
]

CONST_LAMBDA_FUNCTION = lambda x: x ** 2  # noqa


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


class ExampleClass(ABC):
    """
    ExampleClass
    """

    _value: str = "example"

    @property
    def value(self):
        """
        property value
        :return:
        """
        return self._value

    @value.setter
    def value(self, value) -> None:
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

    async def run(self, arg) -> int:
        """
        async function
        :param arg:
        :return:
        """
        pass
