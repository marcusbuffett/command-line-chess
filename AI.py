import sys
from Coordinate import Coordinate as C
from Move import Move
from Piece import Piece
from Board import Board
from MoveNode import MoveNode
import copy
import random
from multiprocessing import Queue, Pool, Process


WHITE = True
BLACK = False

class AI :

    depth = 1
    movesAnalyzed = 0
    board = None
    side = None

    def __init__(self, board, side, depth) :
        self.board = board
        self.side = side
        self.depth = depth

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
        legalMoves = []
        for move in unfilteredMoves :
            if self.moveIsLegal(move) :
                legalMoves.append(move)
        return legalMoves


    def getFirstMove(self, side) :
        move = list(self.getAllMovesLegal(side))[0]
        return move



    def getAllMovesLegalConcurrent (self, side) :
        p = Pool(8)
        unfilteredMovesWithBoard = [(move, copy.deepcopy(self.board)) for move in self.getAllMovesUnfiltered(side)]
        legalMoves = p.starmap(self.returnMoveIfLegal, unfilteredMovesWithBoard)
        p.close()
        p.join()
        return list(filter(None, legalMoves))


    def returnMoveIfLegal(self, move) :
        if self.moveIsLegal(move) :
            return move

    #def generateMoveTree(self, side) :
        #moves
        #for move in self.getAllMovesLegal(side) :

        #moveTree = {move : {} for move in self.getAllMovesLegal(side)}
        #moveTree = self.populateMoveTree(moveTree, not side, self.depth-1)
        
    #def populateMoveTree(self, moveTree, side, layersLeft) :
        #if layersLeft > 0 :
            #for move in moveTree :
                #board.makeMove(move)
                #moveTree[move] = {legalMove : {} for legalMove in self.getAllMovesLegal(side)}
                #self.board.undoLastMove()
                #moveTree[move] = self.populateMoveTree(moveTree[move], not side, layersLeft-1)
            #return moveTree
        #else :
            #return moveTree

    def minChildOfNode(self, node) :
        lowestNode = None
        for child in node.children :
            board.makeMove(child.move)
            pointAdvantage = board.getPointAdvantageOfSide(self.side)
            board.undoLastMove()
            child.pointAdvantage = pointAdvantage
            if lowestNode is None :
                lowestNode = child
            elif child.pointAdvantage < lowestNode.pointAdvantage :
                lowestNode = child
        return lowestNode

    def maxChildOfNode(self, node) :
        highestNode = None
        for child in node.children :
            board.makeMove(child.move)
            pointAdvantage = board.getPointAdvantageOfSide(self.side)
            board.undoLastMove()
            child.pointAdvantage = pointAdvantage
            if highestNode is None :
                highestNode = child
            elif child.pointAdvantage < highestNode.pointAdvantage :
                highestNode = child
        return highestNode

    #def traverseNodeForPointAdvantage(self, node) :
        #nodeSide = board.sideOfMove(node.move)
        #if not node.children :
            #board.makeMove(node.move)
            #pointAdvantage = board.getPointAdvantageOfSide(side)
            #for _ in range(node.depth) :
                #board.undoLastMove()
            #return pointAdvantage

        #child = None
        #if side  == self.side :
            #child = self.maxChildOfNode(node)
        #else :
            #child = self.minChildOfNode(node)

        #board.makeMove(child.move)
        #return traverseNodeForPointAdvantage(self, child)
        
    def getRandomMove(self) :
        legalMoves = list(self.getAllMovesLegal(self.side))
        randomMove = random.choice(legalMoves)
        return randomMove

    def generateMoveTree(self) :
        moveTree = []
        for move in self.getAllMovesLegal(self.side) :
            moveTree.append(MoveNode(move, [], None))
        for node in moveTree :
            self.board.makeMove(node.move)
            self.populateNodeChildren(node)
            self.board.undoLastMove()
            #for _ in range(self.depth) :

        for node in moveTree :
            print(node)
        return moveTree


    #def generateNode(self, node) :
        #if node.getDepth() == self.depth :
            #return node
        #move = node.move
        
        #side = self.board.getSideOfMove(move)
        #node.pointAdvantage = self.board.getPointAdvantageOfSide(side)
        #self.board.makeMove(move)
        #for childMove in self.getAllMovesLegal(side) :
            #node.children.append(MoveNode(childMove, [], node))
        #for child in node.children :
            #self.generateNode(child)
            ##if child.children : 
                ##self.board.undoLastMove()
        ##self.board.undoLastMove()

    def populateNodeChildren(self, node) :
        if node.getDepth() == self.depth :
            node.pointAdvantage = self.board.getPointAdvantageOfSide(self.side)
            return
        side = self.board.getCurrentSide()
        pointAdvantage = self.board.getPointAdvantageOfSide(self.side)
        node.pointAdvantage = pointAdvantage
        for move in self.getAllMovesLegal(not side) :
            node.children.append(MoveNode(move, [], node))
            self.board.makeMove(move)
            for child in node.children :
                self.populateNodeChildren(child)
            self.board.undoLastMove()

    
    def getBestMove(self) :
        moveTree = self.generateMoveTree()

        bestMoveWithAdvantage = []
        return self.bestMoveWithMoveTree(moveTree, self.side)
    
        
    def bestMoveWithMoveTree(moveTree, side) :
        for baseMoveNode in moveTree :
            for _ in range(self.depth-1) :
                pass
            if not bestMoveWithAdvantage :
                bestMoveWithAdvantage = [move, pointAdvantage]
                continue
            if pointAdvantage > bestMoveWithAdvantage[1] :
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

    def makeRandomMove(self) :
        moveToMake = self.getRandomMove()
        self.board.makeMove(moveToMake)


if __name__ == "__main__" :
    mainBoard = Board()
    ai = AI(mainBoard, False, 2)
    print(mainBoard)
    print(ai.generateMoveTree())

    move = ai.getBestMove()
    print(mainBoard)
    #ai.depth = 3
    #ai.generateMoveTree(True)

