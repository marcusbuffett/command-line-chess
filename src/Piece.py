from __future__ import annotations

from typing import Iterator
from typing import TYPE_CHECKING

from src.Coordinate import Coordinate as C
from src.Move import Move

if TYPE_CHECKING:
    from src.Board import Board

WHITE = True
BLACK = False
X = 0
Y = 1


class Piece:
    stringRep: str
    value: int

    def __init__(
            self, board: Board, side: bool, position: C, movesMade: int = 0,
    ) -> None:
        self.board = board
        self.side = side
        self.position = position
        self.movesMade = 0

    def __str__(self) -> str:
        sideString = 'White' if self.side == WHITE else 'Black'
        return 'Type : ' + type(self).__name__ + \
               ' - Position : ' + str(self.position) + \
               ' - Side : ' + sideString + \
               ' -- Value : ' + str(self.value) + \
               ' -- Moves made : ' + str(self.movesMade)

    def movesInDirectionFromPos(
            self, pos: C, direction: C, side: bool,
    ) -> Iterator[Move]:
        for dis in range(1, 8):
            movement = C(dis * direction[X], dis * direction[Y])
            newPos = pos + movement
            if self.board.isValidPos(newPos):
                pieceAtNewPos = self.board.pieceAtPosition(newPos)
                if pieceAtNewPos is None:
                    yield Move(self, newPos)

                elif pieceAtNewPos is not None:
                    if pieceAtNewPos.side != side:
                        yield Move(self, newPos, pieceToCapture=pieceAtNewPos)
                    return

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Piece):
            return NotImplemented
        if (
                self.board == other.board and self.side == other.side
                and self.position == other.position
                and self.__class__ == other.__class__
        ):
            return True
        return False

    def getPossibleMoves(self) -> Iterator[Move]:  # type: ignore[empty-body]
        pass
