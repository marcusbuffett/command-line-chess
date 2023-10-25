from __future__ import annotations

from src.Move import Move


class MoveNode:
    def __init__(
            self,
            move: Move,
            children: list[MoveNode],
            parent: MoveNode | None,
    ) -> None:
        self.move = move
        self.children = children
        self.parent = parent
        self.pointAdvantage = 0
        self.depth = 1

    def __str__(self) -> str:
        stringRep = 'Move : ' + str(self.move) + \
                    ' Point advantage : ' + str(self.pointAdvantage) + \
                    ' Checkmate : ' + str(self.move.checkmate)
        stringRep += '\n'

        for child in self.children:
            stringRep += ' ' * self.getDepth() * 4
            stringRep += str(child)

        return stringRep

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, MoveNode):
            return NotImplemented
        if self.move.checkmate and not other.move.checkmate:
            return True
        if not self.move.checkmate and other.move.checkmate:
            return False
        if self.move.checkmate and other.move.checkmate:
            return False
        return self.pointAdvantage > other.pointAdvantage

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, MoveNode):
            return NotImplemented
        if self.move.checkmate and not other.move.checkmate:
            return False
        if not self.move.checkmate and other.move.checkmate:
            return True
        if self.move.stalemate and other.move.stalemate:
            return False
        return self.pointAdvantage < other.pointAdvantage

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, MoveNode):
            return NotImplemented
        if self.move.checkmate and other.move.checkmate:
            return True
        return self.pointAdvantage == other.pointAdvantage

    def getDepth(self) -> int:
        depth = 1
        highestNode = self
        while True:
            if highestNode.parent is not None:
                highestNode = highestNode.parent
                depth += 1
            else:
                return depth
