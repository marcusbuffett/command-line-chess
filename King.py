from Piece import Piece
from Move import Move
from Coordinate import Coordinate as C

WHITE = True
BLACK = False


class King (Piece):

    stringRep = 'K'
    value = 100

    def __init__(self, board, side, position,  movesMade=0):
        super(King, self).__init__(board, side, position)
        self.movesMade = movesMade

    def getPossibleMoves(self):
        currentPos = self.position
        movements = [C(0, 1), C(0, -1), C(1, 0), C(-1, 0), C(1, 1),
                     C(1, -1), C(-1, 1), C(-1, -1)]
        for movement in movements:
            newPos = currentPos + movement
            if self.board.isValidPos(newPos):
                pieceAtNewPos = self.board.pieceAtPosition(newPos)
                if self.board.pieceAtPosition(newPos) is None:
                    yield Move(self, newPos)
                elif pieceAtNewPos.side != self.side:
                    yield Move(self, newPos, pieceToCapture=pieceAtNewPos)

        # Castling
        if self.movesMade == 0:
            inCheck = False
            kingsideCastleBlocked = False
            queensideCastleBlocked = False
            kingsideCastleCheck = False
            queensideCastleCheck = False
            kingsideRookMoved = True
            queensideRookMoved = True

            kingsideCastlePositions = [self.position - C(1, 0),
                                       self.position - C(2, 0)]
            for pos in kingsideCastlePositions:
                if self.board.pieceAtPosition(pos):
                    kingsideCastleBlocked = True

            queensideCastlePositions = [self.position + C(1, 0),
                                        self.position + C(2, 0),
                                        self.position + C(3, 0)]
            for pos in queensideCastlePositions:
                if self.board.pieceAtPosition(pos):
                    queensideCastleBlocked = True

            if kingsideCastleBlocked and queensideCastleBlocked:
                return

            otherSideMoves = \
                self.board.getAllMovesUnfiltered(not self.side,
                                                 includeKing=False)
            for move in otherSideMoves:
                if move.newPos == self.position:
                    inCheck = True
                    break
                if move.newPos == self.position - C(1, 0) or \
                   move.newPos == self.position - C(2, 0):
                    kingsideCastleCheck = True
                if move.newPos == self.position + C(1, 0) or \
                   move.newPos == self.position + C(2, 0):
                    queensideCastleCheck = True

            kingsideRookPos = self.position - C(3, 0)
            kingsideRook = self.board.pieceAtPosition(kingsideRookPos) \
                if self.board.isValidPos(kingsideRookPos) \
                else None
            if kingsideRook and \
               kingsideRook.stringRep == 'R' and \
               kingsideRook.movesMade == 0:
                kingsideRookMoved = False

            queensideRookPos = self.position + C(4, 0)
            queensideRook = self.board.pieceAtPosition(queensideRookPos) \
                if self.board.isValidPos(queensideRookPos) \
                else None
            if queensideRook and \
               queensideRook.stringRep == 'R' and \
               queensideRook.movesMade == 0:
                queensideRookMoved = False

            if not inCheck:
                if not kingsideCastleBlocked and \
                   not kingsideCastleCheck and \
                   not kingsideRookMoved:
                    move = Move(self, self.position - C(2, 0))
                    rookMove = Move(self.position, self.position - C(1, 0))
                    move.specialMovePiece = \
                        self.board.pieceAtPosition(kingsideRookPos)
                    move.kingsideCastle = True
                    move.rookMove = rookMove
                    yield move
                if not queensideCastleBlocked and \
                   not queensideCastleCheck and \
                   not queensideRookMoved:
                    move = Move(self, self.position + C(2, 0))
                    rookMove = Move(self.position, self.position + C(1, 0))
                    move.specialMovePiece = \
                        self.board.pieceAtPosition(queensideRookPos)
                    move.queensideCastle = True
                    move.rookMove = rookMove
                    yield move
