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
    movesAnalyzed = 0
    board = None

    def __init__(self, board) :
        self.board = board

    def getAllMovesUnfiltered (self, side) :
        for piece in self.board.getAllPieces() :
            if piece.side == side :
                for move in piece.getPossibleMoves() :
                    yield move


    def testIfLegalBoard(self, side, board) :
        for move in self.getAllMovesUnfiltered(side) :
            self.board.makeMove(move)
            kingsPresent = self.board.checkForKings()
            self.board.undoLastMove()
            if kingsPresent == False :
                return False
        return True


    def moveIsLegal(self, move) :
        self.movesAnalyzed += 1
        side = self.board.pieceAtPosition(move.oldPos).side 
        self.board.makeMove(move)
        isLegal = self.testIfLegalBoard(not side, self.board)
        self.board.undoLastMove()
        return isLegal  


    def getAllMovesLegal (self, side) :
        unfilteredMoves = self.getAllMovesUnfiltered(side)
        for move in unfilteredMoves :
            if self.moveIsLegal(move) :
                yield move


    def getFirstMove(self, side) :
        move = list(self.getAllMovesLegal(side))[0]
        return move



    def getAllMovesLegalConcurrent (self, side) :
        p = Pool(8)
        print("SHOULD NOT BE HERE")
        unfilteredMovesWithBoard = [(move, copy.deepcopy(self.board)) for move in self.getAllMovesUnfiltered(side)]
        #for thing in unfilteredMovesWithBoard :
            #print(thing)
            #print(thing[0])
        #sys.exit()
        legalMoves = p.starmap(self.returnMoveIfLegal, unfilteredMovesWithBoard)
        p.close()
        p.join()
        #print([str(move) for move in legalMoves])
        return list(filter(None, legalMoves))


    def returnMoveIfLegal(self, move) :
        #print('MOVE : \n' + str(move))
        #print('BOARD : \n' + str(board.makeStringRep()))
        if self.moveIsLegal(move) :
            return move

    def generateMoveTree(self, side) :
        moveTree = {}
        
    def populateMoveTree(self, moveTree, side) :
        pass


    def getRandomMove(self, side) :
        legalMoves = list(self.getAllMovesLegal(side))
        #print(legalMoves)
        randomMove = random.choice(legalMoves)
        return randomMove
    
    def getBestMove(self, side) :
        legalMoves = self.getAllMovesLegal(side)
        moveTree = {move : {} for move in legalMoves}
        #print(moveTree)

        bestMoveWithAdvantage = []

        for move in moveTree :
            self.board.makeMove(move)
            pointAdvantage = self.board.getPointAdvantageOfSide(side)
            self.board.undoLastMove()
            if not bestMoveWithAdvantage :
                bestMoveWithAdvantage = [move, pointAdvantage]
                continue
            if pointAdvantage > bestMoveWithAdvantage[1] :
                #print("Best move is : " + str(move))
                #print("Point advantage is : " + str(pointAdvantage))
                bestMoveWithAdvantage = [move, pointAdvantage]
        
        return bestMoveWithAdvantage[0]

    def isValidMove(self, move, side) :
        for legalMove in self.getAllMovesLegal(side) :
            if move == legalMove :
                return True
        return False


    def recursiveMoveFinder(self, moveTree, bestMove) :
        pass



    #def getRandomMoveConcurrent(self, side) :
        #randomMove = random.choice(self.getAllMovesLegalConcurrent(side))
        #return randomMove

    def makeRandomMove(self, side) :
        moveToMake = self.getRandomMove(side)
        self.board.makeMove(moveToMake)

