from Piece import Piece
from Coordinate import Coordinate as C
from Move import Move

WHITE = True
BLACK = False

class Pawn (Piece) :

    stringRep = 'p'
    value = 1

    def __init__(self, board, side) :
        super(Pawn, self).__init__(board, side)
        self.hasMoved = False

    def getPossibleMoves(self) :
        currentPosition = self.position
        board = self.board
        if self.side == WHITE and self.position[1] != 1 :
            self.hasMoved = True
        elif self.side == BLACK and self.position[1] != 6 :
            self.hasMoved = True
        else :
            self.hasMoved = False


            self.hasMoved 

        # Pawn moves one up
        movement = C(0, 1) if self.side is WHITE else C(0, -1)

        advanceOnePosition = currentPosition + movement
        if board.isValidPos(advanceOnePosition) :
            if board.pieceAtPosition(advanceOnePosition) is None :
                yield Move(currentPosition, advanceOnePosition)

        #Pawn moves two up
        if not self.hasMoved :
            movement = C(0, 2) if self.side is WHITE else C(0, -2)
            advanceTwoPosition = currentPosition + movement
            if board.isValidPos(advanceTwoPosition) :
                if board.pieceAtPosition(advanceTwoPosition) is None :
                    yield Move(currentPosition, advanceTwoPosition)


