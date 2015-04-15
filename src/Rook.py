from Piece import Piece
from Coordinate import Coordinate as C

WHITE = True
BLACK = False


class Rook (Piece):

    stringRep = 'R'
    value = 5

    def __init__(self, board, side, position,  movesMade=0):
        super(Rook, self).__init__(board, side, position)
        self.movesMade = movesMade

    def getPossibleMoves(self):
        currentPosition = self.position

        directions = [C(0, 1), C(0, -1), C(1, 0), C(-1, 0)]
        for direction in directions:
            for move in self.movesInDirectionFromPos(currentPosition,
                                                     direction, self.side):
                yield move
