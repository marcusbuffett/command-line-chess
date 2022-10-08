from src.Board import Board
from src.InputParser import InputParser

from . import makeBoardMoves

def testMate():
    board = Board()
    
    # https://www.chess.com/terms/fools-mate
    # Walter Thomas Mayfield and William Robert Trinks in the 1959 U.S. Open in Omaha, Nebraska
    makeBoardMoves(board, ["e4", "g5", "Nc3", "f5", "Qh5"])

    assert board.isCheckmate()