import pytest

from src.InputParser import InputParser
from src.Board import Board


@pytest.fixture
def makeBoardMoves():
    def makeBoardMovesFactory(board, moves):
        parser = InputParser(board, True)

        for moveStr in moves:
            move = parser.parse(moveStr)
            parser.side = not parser.side
            board.makeMove(move)

    return makeBoardMovesFactory
