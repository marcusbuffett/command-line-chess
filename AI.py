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
        legalMoves = p.starmap(self.returnMoveIfLegal, unfilteredMovesWithBoard)
        p.close()
        p.join()
        return list(filter(None, legalMoves))


    def returnMoveIfLegal(self, move) :
        if self.moveIsLegal(move) :
            return move

    def generateMoveTree(self, side) :
        moveTree = {move : {} for move in self.getAllMovesLegal(side)}
        moveTree = self.populateMoveTree(moveTree, not side, self.depth-1)
        import pprint
        pprinter = pprint.PrettyPrinter(indent=4)
        pprinter.pprint(moveTree)
        
    def populateMoveTree(self, moveTree, side, layersLeft) :
        if layersLeft > 0 :
            for move in moveTree :
                board.makeMove(move)
                moveTree[move] = {legalMove : {} for legalMove in self.getAllMovesLegal(side)}
                self.board.undoLastMove()
                moveTree[move] = self.populateMoveTree(moveTree[move], not side, layersLeft-1)
            return moveTree
        else :
            return moveTree

    def getRandomMove(self, side) :
        legalMoves = list(self.getAllMovesLegal(side))
        #print(legalMoves)
        randomMove = random.choice(legalMoves)
        return randomMove
    
    def getBestMove(self, side) :
        moveTree = self.generateMoveTree(side)
        bestMoveWithAdvantage = []
        return self.bestMoveWithMoveTree(moveTree, side)
    
        
    def bestMoveWithMoveTree(moveTree, side) :

        for move in moveTree :
            board.makeMove(move)
            for lowerMove in moveTree[move] :
                board.makeMove(lowerMove)


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

    def traverseTreeForBestMove(self, side, moveTree, layersTraversed, bestMovesFound) :
        if layersLeft < self.depth :
            for move in moveTree :
                board.makeMove(move)
                return traverseTreeForBestMove(moveTree[move], layersLeft+1, bestMoveFound)
        if layersLeft == self.depth :
            for move in moveTree :
                board.makeMove(move)
                pointAdvantage = board.getPointAdvantageOfSide(side)
                ##TODO
                previousBestAdvantage = 1
                return move
                


                



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


if __name__ == "__main__" :
    board = Board()
    ai = AI(board)
    ai.depth = 3
    ai.generateMoveTree(True)

