from Move import Move
from Coordinate import Coordinate as C

class InputParser :
    
    def __init__(self, board, side) :
        self.board = board

    def parse(self, humanInput) :

        humanInput = humanInput.lower()
        regexLongNotation = re.compile('[a-z][1-8][a-z][1-8]')
        if regexLongNotation.match(humanInput) :
            return self.moveForLongNotation(humanInput)
        
        regexShortNotation = re.compile('[rnbkqp][a-z][1-8]')
        if regexShortNotation.match(humanInput) :
            return self.moveForShortNotation(humanInput)

    def moveForLongNotation(self, notation) :
            transTable = str.maketrans('abcdefgh', '12345678')
            humanInput = humanInput.translate(transTable)
            humanInput = [int(c)-1 for c in humanInput]
            oldPos = C(humanInput[0], humanInput[1])
            newPos = C(humanInput[2], humanInput[3])
            return Move(oldPos, newPos)

    def moveForShortNotation(self, notation) :





