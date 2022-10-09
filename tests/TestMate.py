import pytest
from src.Board import Board
from src.InputParser import InputParser


@pytest.mark.parametrize(
    "moves",
    [
        # https://www.chess.com/terms/fools-mate
        # Walter Thomas Mayfield and William Robert Trinks in the 1959 U.S. Open in Omaha, Nebraska
        ["e4", "g5", "Nc3", "f5", "Qh5"],
    ],
)
def testMate(moves, makeBoardMoves):
    board = Board()

    makeBoardMoves(board, moves)

    assert board.isCheckmate()
