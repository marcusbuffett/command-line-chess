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

    def __init__(self, mateInOne = False, castleBoard = False) :
        self.boardArray = []

        if not mateInOne and not castleBoard:
            backRowBlack = [Rook(self, BLACK), Knight(self, BLACK), Bishop(self, BLACK), King(self, BLACK), Queen(self, BLACK), Bishop(self, BLACK), Knight(self, BLACK), Rook(self, BLACK)]
            frontRowBlack = [Pawn(self, BLACK) for _ in range(8)]
            frontRowWhite = [Pawn(self, WHITE) for _ in range(8)]
            backRowWhite = [Rook(self, WHITE), Knight(self, WHITE), Bishop(self, WHITE), King(self, WHITE), Queen(self, WHITE), Bishop(self, WHITE), Knight(self, WHITE), Rook(self, WHITE)]

            self.boardArray.append(backRowBlack)
            self.boardArray.append(frontRowBlack)
            for _ in range(4) :
                self.boardArray.append([None] * 8)
            self.boardArray.append(frontRowWhite)
            self.boardArray.append(backRowWhite)
            self.movesMade = 0

        elif mateInOne :
            self.boardArray.append([None, None, None, None, None, None, None, None])
            self.boardArray.append([None, None, None, None, None, None, None, None])
            self.boardArray.append([None, None, None, None, None, None, None, None])
            self.boardArray.append([None, None, None, None, None, None, None, None])
            self.boardArray.append([None, None, None, None, None, None, None, None])
            self.boardArray.append([None, None, None, King(self, BLACK), None, None, None, None])
            self.boardArray.append([None, None, None, None, None, None, None, Queen(self, BLACK)])
            self.boardArray.append([None, None, None, King(self, WHITE), None, None, None, None])


        elif castleBoard :
            self.boardArray.append([None, None, None, None, None, None, None, None])
            self.boardArray.append([None, None, None, None, None, None, None, None])
            self.boardArray.append([None, None, None, None, None, None, None, None])
            self.boardArray.append([None, None, None, None, None, None, None, None])
            self.boardArray.append([None, None, None, None, None, None, None, None])
            self.boardArray.append([None, None, None, King(self, BLACK), None, None, None, None])
            self.boardArray.append([None, None, None, None, None, None, None, None])
            self.boardArray.append([Rook(self, WHITE), None, None, None, King(self, WHITE), None, None, None])

        self.history = []
        self.pieces = list(filter(None, [piece for sublist in self.boardArray for piece in sublist]))
        for piece in self.pieces :
            piece.updatePosition()

        self.points = 0
        self.currentSide = WHITE
        self.movesMade = 0
        self.checkmate = False





    def __str__(self) :
        return self.makeStringRep(self.boardArray)

    def undoLastMove(self) :
        lastMove, pieceTaken = self.history.pop()
        pieceToMoveBack = self.pieceAtPosition(lastMove.newPos)
        self.movePieceToPosition(pieceToMoveBack, lastMove.oldPos)
        if pieceTaken :
            if pieceTaken.side == WHITE :
                self.points += pieceTaken.value
            if pieceTaken.side == BLACK :
                self.points -= pieceTaken.value
            self.addPieceToPosition(pieceTaken, lastMove.newPos)
            self.pieces.append(pieceTaken)



        pieceToMoveBack.movesMade -= 1
        self.currentSide = not self.currentSide



    def isCheckmate(self) :
        if len(self.getAllMovesLegal(self.currentSide)) == 0 :
            for move in self.getAllMovesUnfiltered(not self.currentSide) :
                pieceToTake = self.pieceAtPosition(move.newPos)
                if pieceToTake and pieceToTake.stringRep == "K" :
                    return True
        return False
    
    def getLastMove(self) :
        return self.history[-1][0]

    def getLastPieceMoved(self) :
        if self.history :
            return self.pieceAtPosition(self.history[-1][0].newPos)
    
    def addMoveToHistory(self, move) :
        pieceAtNewPos = self.pieceAtPosition(move.newPos)
        if pieceAtNewPos :
            self.history.append([move, pieceAtNewPos.copy()])
            self.pieces.remove(pieceAtNewPos)
        else :
            self.history.append([move, None])

    def getCurrentSide(self) :
        return self.currentSide
            
    def makeStringRep(self, boardArray) :
        stringRep = ''
        for x in range(8) :
            for y in range(8) :
                piece =  boardArray[x][y]
                pieceRep = ''
                if piece is not None :
                    side = piece.side
                    color = 'blue' if side == WHITE else 'red'
                    pieceRep = colored(piece.stringRep, color)
                else :
                    pieceRep = 'x'
                stringRep += pieceRep + ' '
            stringRep += '\n'
        stringRep = stringRep.strip()
        return stringRep

    def rankOfPiece(self, piece) :
        return str(piece.position[1] + 1)


    def fileOfPiece(self, piece) :
        transTable = str.maketrans('01234567', 'abcdefgh')
        return str(piece.position[0]).translate(transTable)


    def getShortNotationOfMove(self, move) :
        notation = ""
        pieceToMove = self.pieceAtPosition(move.oldPos)
        pieceToTake = self.pieceAtPosition(move.newPos)

        if pieceToMove.stringRep != 'p' :
            notation += pieceToMove.stringRep

        if pieceToTake is not None :
            if pieceToMove.stringRep == 'p' :
                notation += self.fileOfPiece(pieceToMove)
            notation += 'x'

        notation += self.positionToHumanCoord(move.newPos)
        return notation
    
    def getShortNotationOfMoveWithFile(self, move) :
        #TODO: Use self.getShortNotationOfMove instead of repeating code
        notation = ""
        pieceToMove = self.pieceAtPosition(move.oldPos)
        pieceToTake = self.pieceAtPosition(move.newPos)

        if pieceToMove.stringRep != 'p' :
            notation += pieceToMove.stringRep
            notation += self.fileOfPiece(pieceToMove)

        if pieceToTake is not None :
            notation += 'x'

        notation += self.positionToHumanCoord(move.newPos)
        return notation
    
    def getShortNotationOfMoveWithRank(self, move) :
        #TODO: Use self.getShortNotationOfMove instead of repeating code
        notation = ""
        pieceToMove = self.pieceAtPosition(move.oldPos)
        pieceToTake = self.pieceAtPosition(move.newPos)

        if pieceToMove.stringRep != 'p' :
            notation += pieceToMove.stringRep
            notation += self.rankOfPiece(pieceToMove)

        if pieceToTake is not None :
            notation += 'x'

        notation += self.positionToHumanCoord(move.newPos)
        return notation

    def getShortNotationOfMoveWithFileAndRank(self, move) :
        #TODO: Use self.getShortNotationOfMove instead of repeating code
        notation = ""
        pieceToMove = self.pieceAtPosition(move.oldPos)
        pieceToTake = self.pieceAtPosition(move.newPos)

        if pieceToMove.stringRep != 'p' :
            notation += pieceToMove.stringRep
            notation += self.fileOfPiece(pieceToMove)
            notation += self.rankOfPiece(pieceToMove)
            

        if pieceToTake is not None :
            notation += 'x'

        notation += self.positionToHumanCoord(move.newPos)
        return notation
        return 

    def humanCoordToPosition(self, coord) :
        transTable = str.maketrans('abcdefgh', '12345678')
        coord = coord.translate(transTable)
        coord = [int(c)-1 for c in coord]
        pos = C(coord[0], coord[1])
        return pos
        
    def positionToHumanCoord(self, pos) :
        transTable = str.maketrans('01234567', 'abcdefgh')
        notation = str(pos[0]).translate(transTable) + str(pos[1]+1) 
        return notation

    def isValidPos(self, pos) :
        if 0 <= pos[0] <= 7 and 0 <= pos[1] <= 7 :
            return True
        else :
            return False

    def getSideOfMove(self, move) :
        return self.pieceAtPosition(move.oldPos).side

    def getPositionOfPiece(self, piece) :
        for y in range(8) :
            for x in range(8) :
                if self.boardArray[y][x] is piece :
                    return C(x, 7-y)

    def pieceAtPosition(self, pos) :
        x, y = self.coordToLocationInArray(pos)
        return self.boardArray[x][y]

    def movePieceToPosition(self, piece, pos) :
        oldPos = piece.position
        self.addPieceToPosition(piece, pos)
        self.clearPosition(oldPos)

    def addPieceToPosition(self, piece, pos) :
        x, y = self.coordToLocationInArray(pos)
        self.boardArray[x][y] = piece
        piece.position = pos

    def clearPosition(self, pos) :
        x, y = self.coordToLocationInArray(pos)
        self.boardArray[x][y] = None

        
    def coordToLocationInArray(self, pos) :
        return (7-pos[1], pos[0])

    def locationInArrayToCoord(self, loc) :
        return (loc[1], 7-loc[0])

    def makeMove(self, move) :
        self.movesMade += 1
        self.addMoveToHistory(move)
        pieceToMove = self.pieceAtPosition(move.oldPos)
        pieceToTake = self.pieceAtPosition(move.newPos)

        if pieceToTake :
            if pieceToTake.side == WHITE :
                self.points -= pieceToTake.value
            if pieceToTake.side == BLACK :
                self.points += pieceToTake.value
            
        self.movePieceToPosition(pieceToMove, move.newPos)
        pieceToMove.movesMade += 1
        self.currentSide = not self.currentSide

    def getPointValueOfSide(self, side) :
        points = 0
        for piece in self.pieces :
            if piece.side == side :
                points += piece.value
        return points

    def getPointAdvantageOfSide(self, side) :
        if side == WHITE :
            return self.points
        if side == BLACK :
            return -self.points
        

    def getAllMovesUnfiltered (self, side, includeKing=True) :
        unfilteredMoves = []
        for piece in self.pieces :
            if piece.side == side :
                if includeKing or piece.stringRep != 'K' :
                    for move in piece.getPossibleMoves() :
                        unfilteredMoves.append(move)
        return unfilteredMoves

    def testIfLegalBoard(self, side) :
        for move in self.getAllMovesUnfiltered(side) :
            pieceToTake = self.pieceAtPosition(move.newPos)
            if pieceToTake and pieceToTake.stringRep == 'K' :
                return False
        return True


    def moveIsLegal(self, move) :
        side = self.pieceAtPosition(move.oldPos).side 
        self.makeMove(move)
        isLegal = self.testIfLegalBoard(not side)
        self.undoLastMove()
        return isLegal  



    def getAllMovesLegal (self, side) :
        unfilteredMoves = list(self.getAllMovesUnfiltered(side))
        legalMoves = []
        for move in unfilteredMoves :
            if self.moveIsLegal(move) :
                legalMoves.append(move)
        return legalMoves


