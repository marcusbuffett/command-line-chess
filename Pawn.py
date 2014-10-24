from Piece import Piece
from Coordinate import Coordinate as C
from Move import Move

WHITE = True
BLACK = False

class Pawn (Piece) :

    stringRep = 'p'
    value = 1

    def __init__(self, board, side, movesMade=0) :
        super(Pawn, self).__init__(board, side)
        self.movesMade = movesMade

    def getPossibleMoves(self) :
        currentPosition = self.position

        # Pawn moves one up
        movement = C(0, 1) if self.side == WHITE else C(0, -1)
        advanceOnePosition = currentPosition + movement
        if self.board.isValidPos(advanceOnePosition) :
            if self.board.pieceAtPosition(advanceOnePosition) is None :
                yield Move(currentPosition, advanceOnePosition)

        #Pawn moves two up
        if self.movesMade == 0 :
            movement = C(0, 2) if self.side == WHITE else C(0, -2)
            advanceTwoPosition = currentPosition + movement
            if self.board.isValidPos(advanceTwoPosition) :
                if self.board.pieceAtPosition(advanceTwoPosition) is None and self.board.pieceAtPosition(advanceOnePosition) is None:
                    yield Move(currentPosition, advanceTwoPosition)

        #Pawn takes
        movements = [C(1,1), C(-1,1)] if self.side == WHITE else [C(1,-1), C(-1,-1)]

        for movement in movements :
            newPosition = self.position + movement
            if self.board.isValidPos(newPosition) :
                pieceToTake = self.board.pieceAtPosition(newPosition)
                if pieceToTake and pieceToTake.side != self.side :
                    yield Move(currentPosition, newPosition)

        #En pessane
        movements = [C(1,1), C(-1,1)] if self.side == WHITE else [C(1,-1), C(-1,-1)]
        for movement in movements :
            posBesidePawn = self.position + C(movement[0], 0)
            if self.board.isValidPos(posBesidePawn) :
                pieceBesidePawn = self.board.pieceAtPosition(posBesidePawn)
                lastPieceMoved = self.board.getLastPieceMoved()
                if pieceBesidePawn and pieceBesidePawn.stringRep == 'p' and lastPieceMoved is pieceBesidePawn :
                    move = Move(self.position, self.position + movement)
                    move.pessant = True
                    yield move





