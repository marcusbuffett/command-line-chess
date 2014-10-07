from Pawn import Pawn
from Rook import Rook
from King import King
from Bishop import Bishop
from Knight import Knight
from Queen import Queen
from Piece import Piece
from Coordinate import Coordinate as C
from termcolor import colored


WHITE = True
BLACK = False

class Board :

    #boardArray = []

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
        #self.boardArray = [backRowBlack, frontRowBlack, emptyRow, emptyRow, emptyRow, emptyRow, frontRowWhite, backRowWhite]
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

    def __str__(self) :
        return '\n'.join(' '.join(str(item) for item in row) for row in self.boardArray)

    def makeStringRep(self) :
        stringRep = ''
        for x in range(8) :
            for y in range(8) :
                coord = self.locationInArrayToCoord([x, y])
                piece = self.pieceAtPosition(coord)
                if piece is not None:
                    pieceRep = self.pieceAtPosition(coord).stringRep
                    if piece.side == WHITE :
                        stringRep += colored(pieceRep, 'blue')
                    else :
                        stringRep += colored(pieceRep, 'red')
                else :
                    stringRep += 'x'
                stringRep += ' '
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
        pieceToMove = self.pieceAtPosition(move.oldPos)
        self.movePieceToPosition(pieceToMove, move.newPos)
        if isinstance(pieceToMove, Pawn) :
            pieceToMove.hasMoved = True

    def checkForKings(self) :
        kingsFound = 0
        for piece in self.getAllPieces() :
            if isinstance(piece, King) :
                kingsFound += 1
        if kingsFound == 2 :
            return True
        else :
            return False


