
from Piece import Piece
from Coordinate import Coordinate as C

WHITE = True
BLACK = False

class Bishop (Piece) :

    stringRep = 'B'
    value = 3

    def __init__(self, board, side) :
        super(Bishop, self).__init__(board, side)


    def getPossibleMoves(self) :
        currentPosition = self.position
        board = self.board

        directions = [C(1, 1), C(1, -1), C(-1, 1), C(-1, -1)]
        for direction in directions :
            for move in self.movesInDirectionFromPos(currentPosition, direction, self.side) :
                yield move

        
            


