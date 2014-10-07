import sys
from Coordinate import Coordinate as C
from Move import Move
from Piece import Piece
from Board import Board
import copy
import random

WHITE = True
BLACK = False

class AI :
    
    #board = None
    
    #def __init__(self, board) :
        #self.board = board

    def getAllMovesUnfiltered (self, side, board) :
        for piece in board.getAllPieces() :
            if piece.side == side :
                for move in piece.getPossibleMoves() :
                    yield move

    def getAllMovesLegal (self, side, board) :
        for move in self.getAllMovesUnfiltered(side, board) :
            if self.moveIsLegal(move, board) :
                yield move

    def moveIsLegal(self, move, board) :
        copyBoard = copy.deepcopy(board)
        side = copyBoard.pieceAtPosition(move.oldPos).side 
        copyBoard.makeMove(move)
        return self.testIfLegalBoard(copyBoard, not side)

    def testIfLegalBoard(self, board, side) :
        for move in self.getAllMovesUnfiltered(side, board) :
            boardCopy = copy.deepcopy(board)
            boardCopy.makeMove(move)
            if boardCopy.checkForKings() == False :
                sys.exit()
                return False
        return True

    def getRandomMove(self, side, board) :
        randomMove = random.choice(list(self.getAllMovesLegal(side, board)))
        return randomMove

    def makeRandomMove(self, side, board) :
        moveToMake = random.choice(list(self.getAllMovesLegal(side, board)))
        board.makeMove(moveToMake)
