import pytest

from src.Board import Board
from src.Coordinate import Coordinate
from src.Knight import Knight


@pytest.mark.parametrize(
    ["coord", "expected"],
    [
        [(4, 4), [(6, 5), (6, 3), (2, 5), (2, 3), (5, 6), (5, 2), (3, 2), (3, 6)]],
        [(6, 4), [(8, 5), (8, 3), (4, 5), (4, 3), (7, 6), (7, 2), (5, 2), (5, 6)]],
    ],
)
def testKnight(coord, expected):
    board = Board()

    knight = Knight(board, False, coord)

    poss = []
    for i in knight.getPossibleMoves():
        assert i.oldPos == coord
        poss.append(Coordinate(*i.newPos[:2]) + Coordinate(*i.newPos[2:]))

    assert poss == expected
