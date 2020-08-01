from Bishop import Bishop
from Coordinate import Coordinate as C
from King import King
from Knight import Knight
from Move import Move
from Pawn import Pawn
from Queen import Queen
from Rook import Rook
from termcolor import colored

WHITE = True
BLACK = False


class Board:

    def __init__(self, mateInOne=False, castleBoard=False,
                 passant=False, promotion=False):
        self.pieces = []
        self.history = []
        self.points = 0
        self.currentSide = WHITE
        self.movesMade = 0
        self.checkmate = False

        if not mateInOne and not castleBoard and not passant and not promotion:
            self.pieces.extend([Rook(self, BLACK, C(0, 7)),
                                Knight(self, BLACK, C(1, 7)),
                                Bishop(self, BLACK, C(2, 7)),
                                Queen(self, BLACK, C(3, 7)),
                                King(self, BLACK, C(4, 7)),
                                Bishop(self, BLACK, C(5, 7)),
                                Knight(self, BLACK, C(6, 7)),
                                Rook(self, BLACK, C(7, 7))])
            for x in range(8):
                self.pieces.append(Pawn(self, BLACK, C(x, 6)))
            for x in range(8):
                self.pieces.append(Pawn(self, WHITE, C(x, 1)))
            self.pieces.extend([Rook(self, WHITE, C(0, 0)),
                                Knight(self, WHITE, C(1, 0)),
                                Bishop(self, WHITE, C(2, 0)),
                                Queen(self, WHITE, C(3, 0)),
                                King(self, WHITE, C(4, 0)),
                                Bishop(self, WHITE, C(5, 0)),
                                Knight(self, WHITE, C(6, 0)),
                                Rook(self, WHITE, C(7, 0))])

        elif promotion:
            pawnToPromote = Pawn(self, WHITE, C(1, 6))
            pawnToPromote.movesMade = 1
            kingWhite = King(self, WHITE, C(4, 0))
            kingBlack = King(self, BLACK, C(3, 2))
            self.pieces.extend([pawnToPromote, kingWhite, kingBlack])

        elif passant:
            pawn = Pawn(self, WHITE, C(1, 4))
            pawn2 = Pawn(self, BLACK, C(2, 6))
            kingWhite = King(self, WHITE, C(4, 0))
            kingBlack = King(self, BLACK, C(3, 2))
            self.pieces.extend([pawn, pawn2, kingWhite, kingBlack])
            self.history = []
            self.currentSide = BLACK
            self.points = 0
            self.movesMade = 0
            self.checkmate = False
            firstMove = Move(pawn2, C(2, 4))
            self.makeMove(firstMove)
            self.currentSide = WHITE
            return

    def __str__(self):
        return self.wrapStringRep(self.makeStringRep(self.pieces))

    def undoLastMove(self):
        lastMove, pieceTaken = self.history.pop()

        if lastMove.queensideCastle or lastMove.kingsideCastle:
            king = lastMove.piece
            rook = lastMove.specialMovePiece

            self.movePieceToPosition(king, lastMove.oldPos)
            self.movePieceToPosition(rook, lastMove.rookMove.oldPos)

            king.movesMade -= 1
            rook.movesMade -= 1

        elif lastMove.passant:
            pawnMoved = lastMove.piece
            pawnTaken = pieceTaken
            self.pieces.append(pawnTaken)
            self.movePieceToPosition(pawnMoved, lastMove.oldPos)
            pawnMoved.movesMade -= 1
            if pawnTaken.side == WHITE:
                self.points += 1
            if pawnTaken.side == BLACK:
                self.points -= 1

        elif lastMove.promotion:
            pawnPromoted = lastMove.piece
            promotedPiece = self.pieceAtPosition(lastMove.newPos)
            self.pieces.remove(promotedPiece)
            if pieceTaken:
                if pieceTaken.side == WHITE:
                    self.points += pieceTaken.value
                if pieceTaken.side == BLACK:
                    self.points -= pieceTaken.value
                self.pieces.append(pieceTaken)
            self.pieces.append(pawnPromoted)
            if pawnPromoted.side == WHITE:
                self.points -= promotedPiece.value - 1
            elif pawnPromoted.side == BLACK:
                self.points += promotedPiece.value - 1
            pawnPromoted.movesMade -= 1

        else:
            pieceToMoveBack = lastMove.piece
            self.movePieceToPosition(pieceToMoveBack, lastMove.oldPos)
            if pieceTaken:
                if pieceTaken.side == WHITE:
                    self.points += pieceTaken.value
                if pieceTaken.side == BLACK:
                    self.points -= pieceTaken.value
                self.addPieceToPosition(pieceTaken, lastMove.newPos)
                self.pieces.append(pieceTaken)
            pieceToMoveBack.movesMade -= 1

        self.currentSide = not self.currentSide

    def isCheckmate(self):
        if len(self.getAllMovesLegal(self.currentSide)) == 0:
            for move in self.getAllMovesUnfiltered(not self.currentSide):
                pieceToTake = move.pieceToCapture
                if pieceToTake and pieceToTake.stringRep == "K":
                    return True
        return False

    def isStalemate(self):
        if len(self.getAllMovesLegal(self.currentSide)) == 0:
            for move in self.getAllMovesUnfiltered(not self.currentSide):
                pieceToTake = move.pieceToCapture
                if pieceToTake and pieceToTake.stringRep == "K":
                    return False
            return True
        return False

    def getLastMove(self):
        if self.history:
            return self.history[-1][0]

    def getLastPieceMoved(self):
        if self.history:
            return self.history[-1][0].piece

    def addMoveToHistory(self, move):
        pieceTaken = None
        if move.passant:
            pieceTaken = move.specialMovePiece
            self.history.append([move, pieceTaken])
            return
        pieceTaken = move.pieceToCapture
        if pieceTaken:
            self.history.append([move, pieceTaken])
            return

        self.history.append([move, None])

    def getCurrentSide(self):
        return self.currentSide
    
    def makeStringRep(self, pieces):
        stringRep = ''
        for y in range(7, -1, -1):
            for x in range(8):
                piece = None
                for p in pieces:
                    if p.position == C(x, y):
                        piece = p
                        break
                pieceRep = ''
                if piece:
                    side = piece.side
                    color = 'blue' if side == WHITE else 'red'
                    pieceRep = colored(piece.stringRep, color)
                else:
                    pieceRep = '·'
                stringRep += pieceRep + ' '
            stringRep += '\n'
        return stringRep.rstrip()
    
    def makeUnicodeStringRep(self, pieces):
        DISPLAY_LOOKUP = {
            "R": '♜',
            "N": '♞',
            "B": '♝',
            "K": '♚',	
            "Q": '♛',
            "P": '♟',
        }

        stringRep = ''
        for y in range(7, -1, -1):
            for x in range(8):
                piece = None
                for p in pieces:
                    if p.position == C(x, y):
                        piece = p
                        break
                on_color = 'on_cyan' if y % 2 == x % 2 else 'on_yellow'
                pieceRep = colored('  ', on_color=on_color)
                if piece:
                    side = piece.side
                    color = 'white' if side == WHITE else 'grey'
                    pieceRep = colored(piece.stringRep + ' ', color=color, on_color=on_color)
                stringRep += pieceRep
            stringRep += '\n'
        return stringRep.rstrip()

    def wrapStringRep(self, stringRep):
        sRep = '\n'.join(
            ['%d  %s' % (8-r, s.rstrip())
             for r, s in enumerate(stringRep.split('\n'))] +
            [' '*21, '   a b c d e f g h']
            ).rstrip()
        return sRep

    def rankOfPiece(self, piece):
        return str(piece.position[1] + 1)

    def fileOfPiece(self, piece):
        transTable = str.maketrans('01234567', 'abcdefgh')
        return str(piece.position[0]).translate(transTable)

    def getCoordinateNotationOfMove(self, move):
        notation = ""
        notation += self.positionToHumanCoord(move.oldPos)
        notation += self.positionToHumanCoord(move.newPos)

        if move.promotion:
            notation += str(move.specialMovePiece.stringRep)

        return notation

    def getCaptureNotation(self, move, short=False):
        notation = ""
        pieceToMove = move.piece
        pieceToTake = move.pieceToCapture

        if type(pieceToMove) is Pawn:
            notation += self.fileOfPiece(pieceToMove)
        else:
            notation += pieceToMove.stringRep
        notation += 'x'
        if short:
            notation += pieceToTake.stringRep
        else:
            notation += self.positionToHumanCoord(move.newPos)

        if move.promotion:
            notation += str(move.specialMovePiece.stringRep)

        return notation

    def currentSideRep(self):
        return "White" if self.currentSide else "Black"

    def getAlgebraicNotationOfMove(self, move, short=True):
        notation = ""
        pieceToMove = move.piece
        pieceToTake = move.pieceToCapture

        if move.queensideCastle:
            return "0-0-0"

        if move.kingsideCastle:
            return "0-0"

        if not short or type(pieceToMove) is not Pawn:
            notation += pieceToMove.stringRep

        if pieceToTake is not None:
            if short and type(pieceToMove) is Pawn:
                notation += self.fileOfPiece(pieceToMove)
            notation += 'x'

        notation += self.positionToHumanCoord(move.newPos)

        if move.promotion:
            notation += "=" + str(move.specialMovePiece.stringRep)

        return notation

    def getAlgebraicNotationOfMoveWithFile(self, move, short=True):
        # TODO: Use self.getAlgebraicNotationOfMove instead of repeating code
        notation = ""
        pieceToMove = self.pieceAtPosition(move.oldPos)
        pieceToTake = self.pieceAtPosition(move.newPos)

        if not short or type(pieceToMove) is not Pawn:
            notation += pieceToMove.stringRep
        notation += self.fileOfPiece(pieceToMove)

        if pieceToTake is not None:
            notation += 'x'

        notation += self.positionToHumanCoord(move.newPos)
        return notation

    def getAlgebraicNotationOfMoveWithRank(self, move, short=True):
        # TODO: Use self.getAlgebraicNotationOfMove instead of repeating code
        notation = ""
        pieceToMove = self.pieceAtPosition(move.oldPos)
        pieceToTake = self.pieceAtPosition(move.newPos)

        if not short or type(pieceToMove) is not Pawn:
            notation += pieceToMove.stringRep

        notation += self.rankOfPiece(pieceToMove)

        if pieceToTake is not None:
            if short and type(pieceToMove) is Pawn:
                notation += self.fileOfPiece(pieceToMove)
            notation += 'x'

        notation += self.positionToHumanCoord(move.newPos)
        return notation

    def getAlgebraicNotationOfMoveWithFileAndRank(self, move, short=True):
        # TODO: Use self.getAlgebraicNotationOfMove instead of repeating code
        notation = ""
        pieceToMove = self.pieceAtPosition(move.oldPos)
        pieceToTake = self.pieceAtPosition(move.newPos)

        if not short or type(pieceToMove) is not Pawn:
            notation += pieceToMove.stringRep

        notation += self.fileOfPiece(pieceToMove)
        notation += self.rankOfPiece(pieceToMove)

        if pieceToTake is not None:
            notation += 'x'

        notation += self.positionToHumanCoord(move.newPos)
        return notation

    def humanCoordToPosition(self, coord):
        transTable = str.maketrans('abcdefgh', '12345678')
        coord = coord.translate(transTable)
        coord = [int(c)-1 for c in coord]
        pos = C(coord[0], coord[1])
        return pos

    def positionToHumanCoord(self, pos):
        transTable = str.maketrans('01234567', 'abcdefgh')
        notation = str(pos[0]).translate(transTable) + str(pos[1]+1)
        return notation

    def isValidPos(self, pos):
        if 0 <= pos[0] <= 7 and 0 <= pos[1] <= 7:
            return True
        else:
            return False

    def getSideOfMove(self, move):
        return move.piece.side

    def getPositionOfPiece(self, piece):
        for y in range(8):
            for x in range(8):
                if self.boardArray[y][x] is piece:
                    return C(x, 7-y)

    def pieceAtPosition(self, pos):
        for piece in self.pieces:
            if piece.position == pos:
                return piece

    def movePieceToPosition(self, piece, pos):
        piece.position = pos

    def addPieceToPosition(self, piece, pos):
        piece.position = pos

    def clearPosition(self, pos):
        x, y = self.coordToLocationInArray(pos)
        self.boardArray[x][y] = None

    def coordToLocationInArray(self, pos):
        return (7-pos[1], pos[0])

    def locationInArrayToCoord(self, loc):
        return (loc[1], 7-loc[0])

    def makeMove(self, move):
        self.addMoveToHistory(move)
        if move.kingsideCastle or move.queensideCastle:
            kingToMove = move.piece
            rookToMove = move.specialMovePiece
            self.movePieceToPosition(kingToMove, move.newPos)
            self.movePieceToPosition(rookToMove, move.rookMove.newPos)
            kingToMove.movesMade += 1
            rookToMove.movesMade += 1

        elif move.passant:
            pawnToMove = move.piece
            pawnToTake = move.specialMovePiece
            pawnToMove.position = move.newPos
            self.pieces.remove(pawnToTake)
            pawnToMove.movesMade += 1

        elif move.promotion:
            pieceToTake = move.pieceToCapture
            self.pieces.remove(move.piece)
            if pieceToTake:
                if pieceToTake.side == WHITE:
                    self.points -= pieceToTake.value
                if pieceToTake.side == BLACK:
                    self.points += pieceToTake.value
                self.pieces.remove(pieceToTake)

            self.pieces.append(move.specialMovePiece)
            if move.piece.side == WHITE:
                self.points += move.specialMovePiece.value - 1
            if move.piece.side == BLACK:
                self.points -= move.specialMovePiece.value - 1
            move.piece.movesMade += 1

        else:
            pieceToMove = move.piece
            pieceToTake = move.pieceToCapture

            if pieceToTake:
                if pieceToTake.side == WHITE:
                    self.points -= pieceToTake.value
                if pieceToTake.side == BLACK:
                    self.points += pieceToTake.value
                self.pieces.remove(pieceToTake)

            self.movePieceToPosition(pieceToMove, move.newPos)
            pieceToMove.movesMade += 1
        self.movesMade += 1
        self.currentSide = not self.currentSide

    def getPointValueOfSide(self, side):
        points = 0
        for piece in self.pieces:
            if piece.side == side:
                points += piece.value
        return points

    def getPointAdvantageOfSide(self, side):
        pointAdvantage = self.getPointValueOfSide(side) - \
            self.getPointValueOfSide(not side)
        return pointAdvantage
        if side == WHITE:
            return self.points
        if side == BLACK:
            return -self.points

    def getAllMovesUnfiltered(self, side, includeKing=True):
        unfilteredMoves = []
        for piece in self.pieces:
            if piece.side == side:
                if includeKing or piece.stringRep != 'K':
                    for move in piece.getPossibleMoves():
                        unfilteredMoves.append(move)
        return unfilteredMoves

    def testIfLegalBoard(self, side):
        for move in self.getAllMovesUnfiltered(side):
            pieceToTake = move.pieceToCapture
            if pieceToTake and pieceToTake.stringRep == 'K':
                return False
        return True

    def moveIsLegal(self, move):
        side = move.piece.side
        self.makeMove(move)
        isLegal = self.testIfLegalBoard(not side)
        self.undoLastMove()
        return isLegal

    # TODO: remove side parameter, unneccesary
    def getAllMovesLegal(self, side):
        unfilteredMoves = list(self.getAllMovesUnfiltered(side))
        legalMoves = []
        for move in unfilteredMoves:
            if self.moveIsLegal(move):
                legalMoves.append(move)
        return legalMoves
