"""Utility function to add two numbers."""

from typing import Union

Number = Union[int, float, complex]


def add_numbers(first: Number, second: Number) -> Number:
    """Return the sum of ``first`` and ``second``.

    Args:
        first: The first number to add.
        second: The second number to add.

    Returns:
        The arithmetic sum of the two numbers.
    """

    return first + second
