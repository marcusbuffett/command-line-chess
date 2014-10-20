from Move import Move

class MoveNode :

    parent = None
    move = []
    pointAdvantage = None
    children = []

    def __init__(self, move, children, parent) :
        self.move = move
        self.children = children
        self.parent = parent

    def __str__(self) :
        stringRep = "Move : " + str(self.move) + " Point advantage : " + str(self.pointAdvantage)
        stringRep += "\n"
        #stringRep = ""
        for child in self.children :
            stringRep += " " * self.getDepth() * 4
            stringRep += str(child)

        return stringRep
        #return "Move : " + str(self.move) + " Children : " + str(self.children)

    def __gt__(self, other) :
        return self.pointAdvantage > other.pointAdvantage

    def __lt__(self, other) :
        return self.pointAdvantage < other.pointAdvantage

    def __eq__(self, other) :
        return self.pointAdvantage == other.pointAdvantage

    def getHighestNode(self) :
        highestNode = self
        while True :
            if highestNode.parent is not None :
                highestNode = highestNode.parent
            else :
                return highestNode

    def getDepth(self) :
        depth = 1
        highestNode = self
        while True :
            if highestNode.parent is not None :
                highestNode = highestNode.parent
                depth += 1
            else :
                return depth
