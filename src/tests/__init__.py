from typing import List

from src.Board import Board
from src.InputParser import InputParser

def makeBoardMoves(board: Board, moves: List[str]):
    parser = InputParser(board, True)
    
    for moveStr in moves:
        move = parser.parse(moveStr)
        parser.side = not parser.side
        board.makeMove(move)