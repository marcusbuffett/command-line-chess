import pytest

from src.Board import Board
from src.Knight import Knight
from src.Move import Move


@pytest.mark.parametrize(
    ['a', 'b', 'c'],
    [
        [(1, 1), (1, 1), (2, 2)],
        [(3, 3), (3, 3), (5, 3)],
        [(3, 3), (3, 3), (6, 6)],
    ],
)
def testEqual(a, b, c):
    board = Board()
    knight = Knight(board, False, a)
    m1 = Move(knight, a)
    assert m1 == Move(knight, a)
    assert Move(knight, a) == Move(knight, b)
    assert not Move(knight, a) == Move(knight, c)


@pytest.mark.parametrize(
    ['coord', 'newpos'],
    [
        [(1, 1), (3, 2)],
        [(2, 2), (4, 3)],
    ],
)
def testStr(coord, newpos):
    board = Board()
    knight = Knight(board, False, coord)
    m1 = Move(knight, newpos)
    assert str(m1).find(str(coord)) > -1
    assert str(m1).find(str(newpos)) > -1
