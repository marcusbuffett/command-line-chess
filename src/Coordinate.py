from __future__ import annotations

from typing import Any


class Coordinate(tuple[int, int]):

    def __new__(cls, *args: int) -> Coordinate:
        return tuple.__new__(cls, args)

    def __reduce__(self) -> tuple[Any, Any]:
        return (self.__class__, tuple(self))

    def __add__(self, other: object) -> Coordinate:
        if not isinstance(other, Coordinate):
            return NotImplemented
        return Coordinate(self[0] + other[0], self[1] + other[1])

    def __sub__(self, other: object) -> Coordinate:
        if not isinstance(other, Coordinate):
            return NotImplemented
        return Coordinate(self[0] - other[0], self[1] - other[1])
