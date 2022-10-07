from __future__ import annotations

from typing import NamedTuple


class Coordinate(NamedTuple):
    rank: int
    file: int

    def __add__(self, other: object) -> Coordinate:
        if not isinstance(other, Coordinate):
            return NotImplemented
        return Coordinate(self[0] + other[0], self[1] + other[1])

    def __sub__(self, other: object) -> Coordinate:
        if not isinstance(other, Coordinate):
            return NotImplemented
        return Coordinate(self[0] - other[0], self[1] - other[1])
