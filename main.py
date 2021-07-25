# from mypy_extensions import TypedDict


# class Z(TypedDict):
#     a: int
#     b: str


# z = Z(a=5, b="hi")
# print("yo")

from typing import Any, Iterable, NamedTuple, Tuple, TypeVar, TypedDict

T = TypeVar("T")


class X(TypedDict):
    a: int
    b: str


def zoop(cols) -> X:
    return (5,)


x = zoop(["b", "a"])
print(X, dir(X))
print(X.__annotations__)
