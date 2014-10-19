from Piece import Piece
from Coordinate import Coordinate as C

WHITE = True
BLACK = False

class Queen (Piece) :

    stringRep = 'Q'
    value = 9

    def __init__(self, board, side) :
        super(Queen, self).__init__(board, side)

    def getPossibleMoves(self) :
        currentPosition = self.position
        board = self.board

        # Rook moves
        directions = [C(0, 1), C(0, -1), C(1, 0), C(-1, 0), C(1, 1), C(1, -1), C(-1, 1), C(-1, -1)]
        for direction in directions :
            for move in self.movesInDirectionFromPos(currentPosition, direction, self.side) :
                yield move

        
            


