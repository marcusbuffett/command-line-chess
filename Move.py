from Coordinate import Coordinate as C 
import re

class Move :
    
    def __init__(self, oldPos, newPos) :
        self.oldPos = oldPos
        self.newPos = newPos

    def __str__(self) :
        return 'Old pos : ' + str(self.oldPos) + ' -- New pos : ' + str(self.newPos)

    def __eq__(self, other) :
        if self.oldPos == other.oldPos and self.newPos == other.newPos :
            return True
        else :
            return False

    def __hash__(self):
          return hash((self.oldPos, self.newPos))

    @classmethod
    def moveFromHumanCoords(cls, coords) :
        coords = coords.lower()
        transTable = str.maketrans('abcdefgh', '12345678')

        regexLongNotation = re.compile('[a-z][1-8][a-z][1-8]')
        if regexLongNotation.match(coords) :
            coords = coords.translate(transTable)
            coords = [int(c)-1 for c in coords]
            oldPos = C(coords[0], coords[1])
            newPos = C(coords[2], coords[3])
            return Move(oldPos, newPos)

            



        coords = list(int(x) for x in coords.translate(transTable))

        return Move(coords[0], coords[1])
        



#if __name__ == '__main__' :
    #coord = 'A4'
    #print(Move.moveFromHumanCoords(coord).)
        
        

