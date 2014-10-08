import sys
from Coordinate import Coordinate as C
from Move import Move
from Piece import Piece
from Board import Board
import copy
import random
from multiprocessing import Queue, Pool, Process

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

    def getAllMovesLegalConcurrent (self, side, board) :
        p = Pool(8)
        unfilteredMovesWithBoard = [(move, copy.deepcopy(board)) for move in self.getAllMovesUnfiltered(side, board)]
        #for thing in unfilteredMovesWithBoard :
            #print(thing)
            #print(thing[0])
        #sys.exit()
        legalMoves = [move for move in p.starmap(self.returnMoveIfLegal, unfilteredMovesWithBoard) if move is not None]
        p.close()
        p.join()
        print([str(move) for move in legalMoves])
        return legalMoves

    def moveIsLegal(self, move, board) :
        copyBoard = copy.deepcopy(board)
        side = copyBoard.pieceAtPosition(move.oldPos).side 
        copyBoard.makeMove(move)
        return self.testIfLegalBoard(copyBoard, not side)

    def returnMoveIfLegal(self, move, board) :
        #print('MOVE : \n' + str(move))
        #print('BOARD : \n' + str(board.makeStringRep()))
        side = board.pieceAtPosition(move.oldPos).side 
        board.makeMove(move)
        if self.testIfLegalBoard(board, not side) :
            return move

    def testIfLegalBoard(self, board, side) :
        for move in self.getAllMovesUnfiltered(side, board) :
            boardCopy = copy.deepcopy(board)
            boardCopy.makeMove(move)
            if boardCopy.checkForKings() == False :
                return False
        return True

    def getRandomMove(self, side, board) :
        randomMove = random.choice(list(self.getAllMovesLegal(side, board)))
        return randomMove

    def getRandomMoveConcurrent(self, side, board) :
        randomMove = random.choice(self.getAllMovesLegalConcurrent(side, board))
        return randomMove

    def makeRandomMove(self, side, board) :
        moveToMake = self.getRandomMove(side, board)
        board.makeMove(moveToMake)
