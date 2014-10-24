from Coordinate import Coordinate as C 
import re

class Move :
    
    notation = None
    check = False
    checkmate = False
    castle = False
    pessant = False
    stalemate = False

    def __init__(self, oldPos, newPos) :
        self.oldPos = oldPos
        self.newPos = newPos

    def __str__(self) :
        displayString = 'Old pos : ' + str(self.oldPos) + ' -- New pos : ' + str(self.newPos)
        if self.notation :
            displayString += ' Notation : ' + self.notation
        if self.castle :
            displayString += ' CASTLE'
        if self.pessant :
            displayString += ' PESSANT'
        return displayString

    def __eq__(self, other) :
        if self.oldPos == other.oldPos and self.newPos == other.newPos :
            return True
        else :
            return False

    def __hash__(self):
        return hash((self.oldPos, self.newPos))
