from Piece import Piece
from Coordinate import Coordinate as C
from Move import Move

WHITE = True
BLACK = False

class Knight (Piece) :

    stringRep = 'N'

    def __init__(self, board, side) :
        super(Knight, self).__init__(board, side)


    def getPossibleMoves(self) :
        board = self.board
        currentPos = board.getPositionOfPiece(self)
        movements = [C(2, 1), C(2, -1), C(-2, 1), C(-2, -1), C(1, 2), C(1, -2), C(-1, -2), C(-1, 2)]
        for movement in movements :
            newPos = currentPos + movement
            if board.isValidPos(newPos) :
                if board.pieceAtPosition(newPos) is None or board.pieceAtPosition(newPos).side != self.side :
                    yield Move(currentPos, newPos)
