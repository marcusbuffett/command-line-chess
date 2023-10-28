import pytest

from src.Board import Board
from src.Coordinate import Coordinate
from src.Knight import Knight
from src.Pawn import Pawn
from src.Rook import Rook


@pytest.mark.parametrize(
    ['coord', 'expected'],
    [
        [
            (4, 4), [
                (6, 5), (6, 3), (2, 5), (2, 3), (5, 6), (5, 2), (3, 2), (3, 6),
            ],
        ],
        [
            (6, 4), [
                (8, 5), (8, 3), (4, 5), (4, 3), (7, 6), (7, 2), (5, 2), (5, 6),
            ],
        ],
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


@pytest.mark.parametrize(
    ['coord', 'expected'],
    [
        [(2, 2), [(2, 1), (2, 0)]],
        [(3, 3), [(3, 2), (3, 1)]],
    ],
)
def testPawn(coord, expected):
    board = Board()

    pawn = Pawn(board, False, coord)

    poss = []
    for i in pawn.getPossibleMoves():
        assert i.oldPos == coord
        poss.append(Coordinate(*i.newPos[:2]) + Coordinate(*i.newPos[2:]))

    assert poss == expected


@pytest.mark.parametrize(
    ['coord', 'expected'],
    [
        [(2, 2), [(2, 1)]],
        [(3, 3), [(3, 2)]],
    ],
)
def testMovedPawn(coord, expected):
    # Moved pawn can move only one.
    board = Board()

    pawn = Pawn(board, False, coord)
    pawn.movesMade = 1
    poss = []
    for i in pawn.getPossibleMoves():
        assert i.oldPos == coord
        poss.append(Coordinate(*i.newPos[:2]) + Coordinate(*i.newPos[2:]))

    assert poss == expected


@pytest.mark.parametrize(
    ['coord', 'expected'],
    [
        [(4, 4), []],
    ],
)
def testRook(coord, expected):
    board = Board()

    rook = Rook(board, False, coord)

    for i in rook.getPossibleMoves():
        assert i.oldPos == coord
        newcoord = Coordinate(*i.newPos[:2]) + Coordinate(*i.newPos[2:])
        assert newcoord.rank == 4 or newcoord.file == 4  # left/right/up/down
