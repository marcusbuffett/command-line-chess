from Coordinate import Coordinate as C 

class Move :
    
    def __init__(self, oldPos, newPos) :
        self.oldPos = oldPos
        self.newPos = newPos

    def __str__(self) :
        return 'Old pos : ' + str(self.oldPos) + ' -- New pos : ' + str(self.newPos)

    @classmethod
    def moveFromHumanCoords(cls, coords) :
        coords = coords.lower()
        transTable = str.maketrans('abcdefgh', '12345678')
        coords = list(int(x) for x in coords.translate(transTable))
        return Move(coords[0], coords[1])
        



#if __name__ == '__main__' :
    #coord = 'A4'
    #print(Move.moveFromHumanCoords(coord).)
        
        

