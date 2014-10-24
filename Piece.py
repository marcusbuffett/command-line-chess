from Coordinate import Coordinate as C
from Move import Move

WHITE = True
BLACK = False
X = 0
Y = 1

class Piece :

    position = None
    movesMade = 0

    def __init__ (self, board, side, movesMade=0) :
        self.board = board
        self.side = side

    def __str__(self) :
        sideString = 'White' if self.side == WHITE else 'Black'
        return 'Type : ' + type(self).__name__ + ' - Position : ' + str(self.position) + " - Side : " + sideString

    def movesInDirectionFromPos(self, pos, direction, side) :
        for dis in range(1, 8) :
            movement = C(dis * direction[X], dis * direction[Y])
            newPos = pos + movement
            if self.board.isValidPos(newPos) :
                if self.board.pieceAtPosition(newPos) is None :
                    yield Move(pos, newPos)
                
                elif self.board.pieceAtPosition(newPos) is not None :
                    if self.board.pieceAtPosition(newPos).side != side :
                        yield Move(pos, newPos)
                    return

    def updatePosition(self) :
        self.position = self.board.getPositionOfPiece(self)
        print("UPDATING POSITION")
    
    def copy(self) :
        cpy = self.__class__(self.board, self.side, movesMade = self.movesMade)
        return self.__class__(self.board, self.side)

    
    

