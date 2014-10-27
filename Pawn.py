from Rook import Rook
from Bishop import Bishop
from Knight import Knight
from Queen import Queen

from Piece import Piece
from Coordinate import Coordinate as C
from Move import Move

WHITE = True
BLACK = False

class Pawn (Piece) :

    stringRep = 'p'
    value = 1

    def __init__(self, board, side, position,  movesMade=0) :
        super(Pawn, self).__init__(board, side, position)
        self.movesMade = movesMade

    def getPossibleMoves(self) :
        currentPosition = self.position

        # Pawn moves one up
        movement = C(0, 1) if self.side == WHITE else C(0, -1)
        advanceOnePosition = currentPosition + movement
        if self.board.isValidPos(advanceOnePosition) :
            #Promotion moves
            #col = advanceOnePosition[1]
            #if col == 7 or col == 0:
                #piecesForPromotion = [Rook(self.board, self.side), Knight(self.board, self.side), Bishop(self.board, self.side)]
                #for piece in piecesForPromotion :
                    #print("YEAH")
                    #move = Move(self.position, advanceOnePosition)
                    #move.promotion = True
                    #move.specialMovePiece = piece
                    #yield move

                

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

        #En pessant
        movements = [C(1,1), C(-1,1)] if self.side == WHITE else [C(1,-1), C(-1,-1)]
        for movement in movements :
            posBesidePawn = self.position + C(movement[0], 0)
            if self.board.isValidPos(posBesidePawn) :
                pieceBesidePawn = self.board.pieceAtPosition(posBesidePawn)
                lastPieceMoved = self.board.getLastPieceMoved()
                lastMoveWasAdvanceTwo = False
                lastMove = self.board.getLastMove()

                if lastMove :
                    if lastMove.newPos - lastMove.oldPos == C(0,2) or lastMove.newPos - lastMove.oldPos == C(0,-2) :
                        lastMoveWasAdvanceTwo = True


                if pieceBesidePawn and pieceBesidePawn.stringRep == 'p' and pieceBesidePawn.side != self.side and lastPieceMoved is pieceBesidePawn and lastMoveWasAdvanceTwo:
                    move = Move(self.position, self.position + movement)
                    move.pessant = True
                    move.specialMovePiece = pieceBesidePawn
                    print("YIELDING EN PESSANT")
                    print(vars(move))
                    print(self.board)
                    yield move

        





