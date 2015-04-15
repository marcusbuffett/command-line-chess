from Board import Board
from MoveNode import MoveNode
from InputParser import InputParser
import copy
import random
from multiprocessing import Pool


WHITE = True
BLACK = False


class AI:

    depth = 1
    board = None
    side = None
    movesAnalyzed = 0

    def __init__(self, board, side, depth):
        self.board = board
        self.side = side
        self.depth = depth
        self.parser = InputParser(self.board, self.side)

    def getFirstMove(self, side):
        move = list(self.board.getAllMovesLegal(side))[0]
        return move

    def getAllMovesLegalConcurrent(self, side):
        p = Pool(8)
        unfilteredMovesWithBoard = \
            [(move, copy.deepcopy(self.board))
             for move in self.board.getAllMovesUnfiltered(side)]
        legalMoves = p.starmap(self.returnMoveIfLegal,
                               unfilteredMovesWithBoard)
        p.close()
        p.join()
        return list(filter(None, legalMoves))

    def minChildrenOfNode(self, node):
        lowestNodes = []
        for child in node.children:
            if not lowestNodes:
                lowestNodes.append(child)
            elif child < lowestNodes[0]:
                lowestNodes = []
                lowestNodes.append(child)
            elif child == lowestNodes[0]:
                lowestNodes.append(child)
        return lowestNodes

    def maxChildrenOfNode(self, node):
        highestNodes = []
        for child in node.children:
            if not highestNodes:
                highestNodes.append(child)
            elif child < highestNodes[0]:
                highestNodes = []
                highestNodes.append(child)
            elif child == highestNodes[0]:
                highestNodes.append(child)
        return highestNodes

    def getRandomMove(self):
        legalMoves = list(self.board.getAllMovesLegal(self.side))
        randomMove = random.choice(legalMoves)
        return randomMove

    def generateMoveTree(self):
        moveTree = []
        for move in self.board.getAllMovesLegal(self.side):
            moveTree.append(MoveNode(move, [], None))

        for node in moveTree:
            self.board.makeMove(node.move)
            self.populateNodeChildren(node)
            self.board.undoLastMove()
        return moveTree

    def populateNodeChildren(self, node):
        node.pointAdvantage = self.board.getPointAdvantageOfSide(self.side)
        node.depth = node.getDepth()
        if node.depth == self.depth:
            return

        side = self.board.currentSide

        legalMoves = self.board.getAllMovesLegal(side)
        if not legalMoves:
            if self.board.isCheckmate():
                node.move.checkmate = True
                return
            elif self.board.isStalemate():
                node.move.stalemate = True
                node.pointAdvantage = 0
                return
            raise Exception()

        for move in legalMoves:
            self.movesAnalyzed += 1
            node.children.append(MoveNode(move, [], node))
            self.board.makeMove(move)
            self.populateNodeChildren(node.children[-1])
            self.board.undoLastMove()

    def getOptimalPointAdvantageForNode(self, node):
        if node.children:
            for child in node.children:
                child.pointAdvantage = \
                    self.getOptimalPointAdvantageForNode(child)

            # If the depth is divisible by 2,
            # it's a move for the AI's side, so return max
            if node.children[0].depth % 2 == 1:
                return(max(node.children).pointAdvantage)
            else:
                return(min(node.children).pointAdvantage)
        else:
            return node.pointAdvantage

    def getBestMove(self):
        moveTree = self.generateMoveTree()
        bestMoves = self.bestMovesWithMoveTree(moveTree)
        randomBestMove = random.choice(bestMoves)
        randomBestMove.notation = self.parser.notationForMove(randomBestMove)
        return randomBestMove

    def makeBestMove(self):
        self.board.makeMove(self.getBestMove())

    def bestMovesWithMoveTree(self, moveTree):
        bestMoveNodes = []
        for moveNode in moveTree:
            moveNode.pointAdvantage = \
                self.getOptimalPointAdvantageForNode(moveNode)
            if not bestMoveNodes:
                bestMoveNodes.append(moveNode)
            elif moveNode > bestMoveNodes[0]:
                bestMoveNodes = []
                bestMoveNodes.append(moveNode)
            elif moveNode == bestMoveNodes[0]:
                bestMoveNodes.append(moveNode)

        return [node.move for node in bestMoveNodes]

    def isValidMove(self, move, side):
        for legalMove in self.board.getAllMovesLegal(side):
            if move == legalMove:
                return True
        return False

    def makeRandomMove(self):
        moveToMake = self.getRandomMove()
        self.board.makeMove(moveToMake)


if __name__ == "__main__":
    mainBoard = Board()
    ai = AI(mainBoard, True, 3)
    print(mainBoard)
    ai.makeBestMove()
    print(mainBoard)
    print(ai.movesAnalyzed)
    print(mainBoard.movesMade)
