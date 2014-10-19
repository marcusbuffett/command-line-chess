from Piece import Piece
from Move import Move
from Coordinate import Coordinate as C

WHITE = True
BLACK = False

class King (Piece) :

    stringRep = 'K'
    value = 100

    def __init__(self, board, side) :
        super(King, self).__init__(board, side)

    def getPossibleMoves(self) :
        board = self.board
        currentPos = self.position
        movements = [C(0, 1), C(0, -1), C(1, 0), C(-1, 0), C(1, 1), C(1, -1), C(-1, 1), C(-1, -1)]
        for movement in movements :
            newPos = currentPos + movement
            if board.isValidPos(newPos) :
                if board.pieceAtPosition(newPos) is None or board.pieceAtPosition(newPos).side != self.side :
                    yield Move(currentPos, newPos)

        
            


