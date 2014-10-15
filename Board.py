from Pawn import Pawn
from Rook import Rook
from King import King
from Bishop import Bishop
from Knight import Knight
from Queen import Queen
from Piece import Piece
from Coordinate import Coordinate as C
from termcolor import colored
import copy


WHITE = True
BLACK = False

class Board :

    def __init__(self) :
        backRowBlack = [Rook(self, BLACK), Knight(self, BLACK), Bishop(self, BLACK), King(self, BLACK), Queen(self, BLACK), Bishop(self, BLACK), Knight(self, BLACK), Rook(self, BLACK)]
        frontRowBlack = []
        for _ in range(8) :
            frontRowBlack.append(Pawn(self, BLACK))
        emptyRow = [None]*8

        frontRowWhite = []
        for _ in range(8) :
            frontRowWhite.append(Pawn(self, WHITE))
        backRowWhite = [Rook(self, WHITE), Knight(self, WHITE), Bishop(self, WHITE), King(self, WHITE), Queen(self, WHITE), Bishop(self, WHITE), Knight(self, WHITE), Rook(self, WHITE)]
        self.boardArray = []
        self.boardArray.append(backRowBlack)
        self.boardArray.append(frontRowBlack)
        for _ in range(4) :
            self.boardArray.append([None] * 8)
        self.boardArray.append(frontRowWhite)
        self.boardArray.append(backRowWhite)
        
        for pawn in frontRowBlack :
            pawn.getPossibleMoves()
        pass

        self.history = []

    def __str__(self) :
        return self.makeStringRep(self.boardArray)

    def undoLastMove(self) :
        lastMove, pieceTaken = self.history.pop()
        pieceToMoveBack = self.pieceAtPosition(lastMove.newPos)
        self.movePieceToPosition(pieceToMoveBack, lastMove.oldPos)
        if pieceTaken :
            pieceTaken.board = self
            self.addPieceToPosition(pieceTaken, lastMove.newPos)

    def addMoveToHistory(self, move) :
        self.history.append([move, copy.deepcopy(self.pieceAtPosition(move.newPos))])

    def makeStringRep(self, boardArray) :
        stringRep = ''
        for x in range(8) :
            for y in range(8) :
                piece =  boardArray[x][y]
                if piece is not None :
                    side = piece.side
                    color = 'blue' if side == WHITE else 'red'
                pieceRep = ''
                if isinstance(piece, Pawn) :
                    pieceRep = colored('P', color)

                elif isinstance(piece, Rook) :
                    pieceRep = colored('R', color)

                elif isinstance(piece, Knight) :
                    pieceRep = colored('N', color)

                elif isinstance(piece, Bishop) :
                    pieceRep = colored('B', color)

                elif isinstance(piece, King) :
                    pieceRep = colored('K', color)

                elif isinstance(piece, Queen) :
                    pieceRep = colored('Q', color)

                else :
                    pieceRep = 'x'
                stringRep += pieceRep + ' '
            stringRep += '\n'
        return stringRep

    def isValidPos(self, pos) :
        if 0 <= pos[0] <= 7 and 0 <= pos[1] <= 7 :
            return True
        else :
            return False

    def getPositionOfPiece(self, piece) :
        for y in range(8) :
            for x in range(8) :
                if self.boardArray[y][x] is piece :
                    return C(x, 7-y)

    def pieceAtPosition(self, pos) :
        x, y = self.coordToLocationInArray(pos)
        return self.boardArray[x][y]

    def movePieceToPosition(self, piece, pos) :
        oldPos = self.getPositionOfPiece(piece)
        self.addPieceToPosition(piece, pos)
        self.clearPosition(oldPos)

    def addPieceToPosition(self, piece, pos) :
        x, y = self.coordToLocationInArray(pos)
        self.boardArray[x][y] = piece

    def clearPosition(self, pos) :
        x, y = self.coordToLocationInArray(pos)
        self.boardArray[x][y] = None
        
    def coordToLocationInArray(self, pos) :
        return (7-pos[1], pos[0])

    def locationInArrayToCoord(self, loc) :
        return (loc[1], 7-loc[0])

    def getAllPieces(self) :
        for row in range(8) :
            for col in range(8) :
                if isinstance(self.boardArray[row][col], Piece) :
                    yield self.boardArray[row][col]

    def makeMove(self, move) :
        self.addMoveToHistory(move)
        pieceToMove = self.pieceAtPosition(move.oldPos)
        self.movePieceToPosition(pieceToMove, move.newPos)

    def getPointValueOfSide(self, side) :
        points = 0
        for piece in self.getAllPieces() :
            if piece.side == side :
                points += piece.value
        return points

    def getPointAdvantageOfSide(self, side) :
        mySideValue = self.getPointValueOfSide(side)
        otherSideValue = self.getPointValueOfSide(not side)
        return mySideValue - otherSideValue
        

    def checkForKings(self) :
        kingsFound = 0
        for piece in self.getAllPieces() :
            if isinstance(piece, King) :
                kingsFound += 1
        if kingsFound == 2 :
            return True
        else :
            return False


