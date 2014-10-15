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

    depth = 1
    #board = None
    #def __init__(self, board) :
        #self.board = board

    def getAllMovesUnfiltered (self, side, board) :
        for piece in board.getAllPieces() :
            if piece.side == side :
                for move in piece.getPossibleMoves() :
                    yield move


    def testIfLegalBoard(self, board, side) :
        for move in self.getAllMovesUnfiltered(side, board) :
            board.makeMove(move)
            kingsPresent = board.checkForKings()
            board.undoLastMove()
            if kingsPresent == False :
                return False
        return True


    def moveIsLegal(self, move, board) :
        side = board.pieceAtPosition(move.oldPos).side 
        board.makeMove(move)
        isLegal = self.testIfLegalBoard(board, not side)
        board.undoLastMove()
        return isLegal  


    def getAllMovesLegal (self, side, board) :
        unfilteredMoves = self.getAllMovesUnfiltered(side, board)
        for move in unfilteredMoves :
            if self.moveIsLegal(move, board) :
                yield move


    def getFirstMove(self, side, board) :
        move = list(self.getAllMovesLegal(side, board))[0]
        return move



    def getAllMovesLegalConcurrent (self, side, board) :
        p = Pool(8)
        unfilteredMovesWithBoard = [(move, copy.deepcopy(board)) for move in self.getAllMovesUnfiltered(side, board)]
        #for thing in unfilteredMovesWithBoard :
            #print(thing)
            #print(thing[0])
        #sys.exit()
        legalMoves = p.starmap(self.returnMoveIfLegal, unfilteredMovesWithBoard)
        p.close()
        p.join()
        #print([str(move) for move in legalMoves])
        return list(filter(None, legalMoves))


    def returnMoveIfLegal(self, move, board) :
        #print('MOVE : \n' + str(move))
        #print('BOARD : \n' + str(board.makeStringRep()))
        if self.moveIsLegal(move, board) :
            return move


    def getRandomMove(self, side, board) :
        legalMoves = list(self.getAllMovesLegal(side, board))
        #print(legalMoves)
        randomMove = random.choice(legalMoves)
        return randomMove
    
    def getBestMove(self, side, board) :
        legalMoves = self.getAllMovesLegal(side, board)
        moveTree = {move : {} for move in legalMoves}
        #print(moveTree)

        bestMoveWithAdvantage = []

        for move in moveTree :
            board.makeMove(move)
            pointAdvantage = board.getPointAdvantageOfSide(side)
            board.undoLastMove()
            if not bestMoveWithAdvantage :
                bestMoveWithAdvantage = [move, pointAdvantage]
                continue
            if pointAdvantage > bestMoveWithAdvantage[1] :
                #print("Best move is : " + str(move))
                #print("Point advantage is : " + str(pointAdvantage))
                bestMoveWithAdvantage = [move, pointAdvantage]
        
        return bestMoveWithAdvantage[0]

    def isValidMove(self, move, side, board) :
        for legalMove in self.getAllMovesLegal(side, board) :
            if move == legalMove :
                return True
        return False


    def recursiveMoveFinder(self, moveTree, bestMove) :
        pass



    #def getRandomMoveConcurrent(self, side, board) :
        #randomMove = random.choice(self.getAllMovesLegalConcurrent(side, board))
        #return randomMove

    def makeRandomMove(self, side, board) :
        moveToMake = self.getRandomMove(side, board)
        board.makeMove(moveToMake)
