from Coordinate import Coordinate as C 
import re

class Move :
    
    def __init__(self, oldPos, newPos) :
        self.notation = None
        self.check = False
        self.checkmate = False
        self.kingsideCastle = False
        self.queensideCastle = False
        self.promotion = False
        self.pessant = False
        self.stalemate = False

        self.oldPos = oldPos
        self.newPos = newPos
        #For en pessant and castling
        self.specialMovePiece = None
        #For castling
        self.rookMove = None



    def __str__(self) :
        displayString = 'Old pos : ' + str(self.oldPos) + ' -- New pos : ' + str(self.newPos)
        if self.notation :
            displayString += ' Notation : ' + self.notation
        if self.pessant :
            displayString = 'Old pos : ' + str(self.oldPos) + ' -- New pos : ' + str(self.newPos) + ' -- Pawn taken : ' + str(self.specialMovePiece)
            displayString += ' PESSANT'
        return displayString

    def __eq__(self, other) :
        if self.oldPos == other.oldPos and self.newPos == other.newPos :
            return True
        else :
            return False

    def __hash__(self):
        return hash((self.oldPos, self.newPos))
