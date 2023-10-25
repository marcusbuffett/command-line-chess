from __future__ import annotations

from colored import attr
from colored import bg
from colored import fg

from src.Bishop import Bishop
from src.Coordinate import Coordinate as C
from src.King import King
from src.Knight import Knight
from src.Move import Move
from src.Pawn import Pawn
from src.Piece import Piece
from src.Queen import Queen
from src.Rook import Rook


WHITE = True
BLACK = False


class Board:
    def __init__(
            self,
            mateInOne: bool = False,
            castleBoard: bool = False,
            passant: bool = False,
            promotion: bool = False,
    ):
        self.pieces: list[Piece] = []
        self.history: list[tuple[Move, Piece | None]] = []
        self.points = 0
        self.currentSide = WHITE
        self.movesMade = 0
        self.checkmate = False
        self.whiteColor = 'white'
        self.blackColor = 'black'
        self.isCheckered = False
        self.tileColors = {
            0: '#769656',
            1: '#BACA44',
        }

        if not mateInOne and not castleBoard and not passant and not promotion:
            self.pieces.extend(
                [
                    Rook(self, BLACK, C(0, 7)),
                    Knight(self, BLACK, C(1, 7)),
                    Bishop(self, BLACK, C(2, 7)),
                    Queen(self, BLACK, C(3, 7)),
                    King(self, BLACK, C(4, 7)),
                    Bishop(self, BLACK, C(5, 7)),
                    Knight(self, BLACK, C(6, 7)),
                    Rook(self, BLACK, C(7, 7)),
                ],
            )
            for x in range(8):
                self.pieces.append(Pawn(self, BLACK, C(x, 6)))
            for x in range(8):
                self.pieces.append(Pawn(self, WHITE, C(x, 1)))
            self.pieces.extend(
                [
                    Rook(self, WHITE, C(0, 0)),
                    Knight(self, WHITE, C(1, 0)),
                    Bishop(self, WHITE, C(2, 0)),
                    Queen(self, WHITE, C(3, 0)),
                    King(self, WHITE, C(4, 0)),
                    Bishop(self, WHITE, C(5, 0)),
                    Knight(self, WHITE, C(6, 0)),
                    Rook(self, WHITE, C(7, 0)),
                ],
            )

        elif promotion:
            pawnToPromote = Pawn(self, WHITE, C(1, 6))
            pawnToPromote.movesMade = 1
            kingWhite = King(self, WHITE, C(4, 0))
            kingBlack = King(self, BLACK, C(3, 2))
            self.pieces.extend([pawnToPromote, kingWhite, kingBlack])

        elif passant:
            pawn = Pawn(self, WHITE, C(1, 4))
            pawn2 = Pawn(self, BLACK, C(2, 6))
            kingWhite = King(self, WHITE, C(4, 0))
            kingBlack = King(self, BLACK, C(3, 2))
            self.pieces.extend([pawn, pawn2, kingWhite, kingBlack])
            self.history = []
            self.currentSide = BLACK
            self.points = 0
            self.movesMade = 0
            self.checkmate = False
            firstMove = Move(pawn2, C(2, 4))
            self.makeMove(firstMove)
            self.currentSide = WHITE
            return

    def __str__(self) -> str:
        return self.wrapStringRep(self.makeUnicodeStringRep(self.pieces))

    def undoLastMove(self) -> None:
        lastMove, pieceTaken = self.history.pop()

        if lastMove.queensideCastle or lastMove.kingsideCastle:
            king = lastMove.piece
            rook = lastMove.specialMovePiece

            self.movePieceToPosition(king, lastMove.oldPos)
            king.movesMade -= 1

            if rook:
                self.movePieceToPosition(rook, lastMove.rookMove.oldPos)
                rook.movesMade -= 1

        elif lastMove.passant:
            pawnMoved = lastMove.piece
            pawnTaken = pieceTaken
            if pawnTaken:
                self.pieces.append(pawnTaken)
                if pawnTaken.side == WHITE:
                    self.points += 1
                if pawnTaken.side == BLACK:
                    self.points -= 1
            self.movePieceToPosition(pawnMoved, lastMove.oldPos)
            pawnMoved.movesMade -= 1

        elif lastMove.promotion:
            pawnPromoted = lastMove.piece
            promotedPiece = self.pieceAtPosition(lastMove.newPos)
            self.pieces.remove(promotedPiece)
            if pieceTaken:
                if pieceTaken.side == WHITE:
                    self.points += pieceTaken.value
                if pieceTaken.side == BLACK:
                    self.points -= pieceTaken.value
                self.pieces.append(pieceTaken)
            self.pieces.append(pawnPromoted)
            if pawnPromoted.side == WHITE:
                self.points -= promotedPiece.value - 1
            elif pawnPromoted.side == BLACK:
                self.points += promotedPiece.value - 1
            pawnPromoted.movesMade -= 1

        else:
            pieceToMoveBack = lastMove.piece
            self.movePieceToPosition(pieceToMoveBack, lastMove.oldPos)
            if pieceTaken:
                if pieceTaken.side == WHITE:
                    self.points += pieceTaken.value
                if pieceTaken.side == BLACK:
                    self.points -= pieceTaken.value
                self.addPieceToPosition(pieceTaken, lastMove.newPos)
                self.pieces.append(pieceTaken)
            pieceToMoveBack.movesMade -= 1

        self.currentSide = not self.currentSide

    def isCheckmate(self) -> bool:
        # Game continue even after checkmate
        if len(self.getAllMovesLegal(self.currentSide)) == 0:
            for move in self.getAllMovesUnfiltered(not self.currentSide):
                pieceToTake = move.pieceToCapture
                if pieceToTake and pieceToTake.stringRep == 'K':
                    return True
        return False

    def isStalemate(self) -> bool:
        return (
            len(self.getAllMovesLegal(self.currentSide)) == 0
            and not self.isCheckmate()
        )

    def noMatingMaterial(self) -> bool:
        if len(self.pieces) == 2:
            return True  # just the kings
        if len(self.pieces) == 3 and any(
                piece.stringRep == 'B' or piece.stringRep == 'N'
                for piece in self.pieces
        ):
            return True
        return False

    # TODO: add consistent return for else condition
    def getLastMove(self) -> Move:  # type: ignore[return]
        if self.history:
            return self.history[-1][0]

    # TODO: add consistent return for else condition
    def getLastPieceMoved(self) -> Piece:  # type: ignore[return]
        if self.history:
            return self.history[-1][0].piece

    def addMoveToHistory(self, move: Move) -> None:
        pieceTaken = None
        if move.passant:
            pieceTaken = move.specialMovePiece
            self.history.append((move, pieceTaken))
            return
        pieceTaken = move.pieceToCapture
        if pieceTaken:
            self.history.append((move, pieceTaken))
            return

        self.history.append((move, None))

    def makeUnicodeStringRep(self, pieces: list[Piece]) -> str:
        DISPLAY_LOOKUP = {
            'R': '♜',
            'N': '♞',
            'B': '♝',
            'K': '♚',
            'Q': '♛',
            '▲': '♟',
        }

        stringRep = ''
        for y in range(7, -1, -1):
            for x in range(8):
                piece = None
                for p in pieces:
                    if p.position == C(x, y):
                        piece = p
                        break
                bg_color = (
                    bg(self.tileColors[(x + y) % 2])
                    if self.isCheckered
                    else ''
                )
                pieceRep = bg_color + '  ' + attr(0)
                if piece:
                    side = piece.side
                    color = (
                        self.whiteColor if side == WHITE else self.blackColor
                    )
                    fg_color = fg(color)
                    pieceRep = fg_color + bg_color + \
                        DISPLAY_LOOKUP[piece.stringRep] + ' ' + attr(0)

                stringRep += pieceRep
            stringRep += '\n'
        return stringRep.rstrip()

    def wrapStringRep(self, stringRep: str) -> str:
        sRep = '\n'.join(
            [
                '%d  %s' % (8 - r, s.rstrip())
                for r, s in enumerate(stringRep.split('\n'))
            ]
            + [' ' * 21, '   a b c d e f g h'],
        ).rstrip()
        return sRep

    def rankOfPiece(self, piece: Piece) -> str:
        return str(piece.position[1] + 1)

    def fileOfPiece(self, piece: Piece) -> str:
        transTable = str.maketrans('01234567', 'abcdefgh')
        return str(piece.position[0]).translate(transTable)

    def getCoordinateNotationOfMove(self, move: Move) -> str:
        notation = ''
        notation += self.positionToHumanCoord(move.oldPos)
        notation += self.positionToHumanCoord(move.newPos)

        if move.promotion:
            notation += str(
                move.specialMovePiece.stringRep,  # type: ignore[attr-defined] # noqa: E501
            )
        return notation

    def getCaptureNotation(self, move: Move, short: bool = True) -> str:
        notation = ''
        pieceToMove = move.piece
        pieceToTake = move.pieceToCapture

        if type(pieceToMove) is Pawn:
            notation += self.fileOfPiece(pieceToMove)
        else:
            notation += pieceToMove.stringRep
        notation += 'x'
        if short:
            notation += pieceToTake.stringRep  # type: ignore[union-attr]
        else:
            notation += self.positionToHumanCoord(move.newPos)

        if move.promotion:
            notation += str(
                move.specialMovePiece.stringRep,   # type: ignore[attr-defined, operator]  # noqa: E501
            )
        return notation

    def currentSideRep(self) -> str:
        return 'White' if self.currentSide else 'Black'

    def getAlgebraicNotationOfMove(
            self, move: Move, short: bool = True,
    ) -> str:
        notation = ''
        pieceToMove = move.piece
        pieceToTake = move.pieceToCapture

        if move.queensideCastle:
            return '0-0-0'

        if move.kingsideCastle:
            return '0-0'

        if not short or type(pieceToMove) is not Pawn:
            notation += pieceToMove.stringRep

        if pieceToTake is not None:
            if short and type(pieceToMove) is Pawn:
                notation += self.fileOfPiece(pieceToMove)
            notation += 'x'

        notation += self.positionToHumanCoord(move.newPos)

        if move.promotion:
            notation += '=' + str(
                move.specialMovePiece.stringRep,   # type: ignore[attr-defined]  # noqa: E501
            )

        return notation

    def getAlgebraicNotationOfMoveWithFile(
            self, move: Move, short: bool = True,
    ) -> str:
        # TODO: Use self.getAlgebraicNotationOfMove instead of repeating code
        notation = ''
        pieceToMove = self.pieceAtPosition(move.oldPos)
        pieceToTake = self.pieceAtPosition(move.newPos)

        if not short or type(pieceToMove) is not Pawn:
            notation += pieceToMove.stringRep
        notation += self.fileOfPiece(pieceToMove)

        if pieceToTake is not None:
            notation += 'x'

        notation += self.positionToHumanCoord(move.newPos)
        return notation

    def getAlgebraicNotationOfMoveWithRank(
            self, move: Move, short: bool = True,
    ) -> str:
        # TODO: Use self.getAlgebraicNotationOfMove instead of repeating code
        notation = ''
        pieceToMove = self.pieceAtPosition(move.oldPos)
        pieceToTake = self.pieceAtPosition(move.newPos)

        if not short or type(pieceToMove) is not Pawn:
            notation += pieceToMove.stringRep

        notation += self.rankOfPiece(pieceToMove)

        if pieceToTake is not None:
            if short and type(pieceToMove) is Pawn:
                notation += self.fileOfPiece(pieceToMove)
            notation += 'x'

        notation += self.positionToHumanCoord(move.newPos)
        return notation

    def getAlgebraicNotationOfMoveWithFileAndRank(
            self, move: Move, short: bool = True,
    ) -> str:
        # TODO: Use self.getAlgebraicNotationOfMove instead of repeating code
        notation = ''
        pieceToMove = self.pieceAtPosition(move.oldPos)
        pieceToTake = self.pieceAtPosition(move.newPos)

        if not short or type(pieceToMove) is not Pawn:
            notation += pieceToMove.stringRep

        notation += self.fileOfPiece(pieceToMove)
        notation += self.rankOfPiece(pieceToMove)

        if pieceToTake is not None:
            notation += 'x'

        notation += self.positionToHumanCoord(move.newPos)
        return notation

    def positionToHumanCoord(self, pos: C) -> str:
        transTable = str.maketrans('01234567', 'abcdefgh')
        notation = str(pos[0]).translate(transTable) + str(pos[1] + 1)
        return notation

    def isValidPos(self, pos: C) -> bool:
        return 0 <= pos[0] <= 7 and 0 <= pos[1] <= 7

    def getSideOfMove(self, move: Move) -> bool:
        return move.piece.side

    # TODO: add consistent return for else condition
    def pieceAtPosition(self, pos: C) -> Piece:  # type: ignore[return]
        for piece in self.pieces:
            if piece.position == pos:
                return piece

    def movePieceToPosition(self, piece: Piece, pos: C) -> None:
        piece.position = pos

    def addPieceToPosition(self, piece: Piece, pos: C) -> None:
        piece.position = pos

    def makeMove(self, move: Move) -> None:
        self.addMoveToHistory(move)
        if move.kingsideCastle or move.queensideCastle:
            kingToMove = move.piece
            rookToMove = move.specialMovePiece
            self.movePieceToPosition(kingToMove, move.newPos)
            self.movePieceToPosition(
                rookToMove,  # type: ignore[arg-type]
                move.rookMove.newPos,  # type: ignore[attr-defined]
            )
            kingToMove.movesMade += 1
            rookToMove.movesMade += 1  # type: ignore[attr-defined]

        elif move.passant:
            pawnToMove = move.piece
            # TODO fix specialMovePiece default type to be not None
            pawnToTake = move.specialMovePiece
            pawnToMove.position = move.newPos
            self.pieces.remove(pawnToTake)  # type: ignore[arg-type]
            pawnToMove.movesMade += 1

        elif move.promotion:
            pieceToTake = move.pieceToCapture
            self.pieces.remove(move.piece)
            if pieceToTake:
                if pieceToTake.side == WHITE:
                    self.points -= pieceToTake.value
                if pieceToTake.side == BLACK:
                    self.points += pieceToTake.value
                self.pieces.remove(pieceToTake)
            # TODO fix specialMovePiece default type to be not None
            self.pieces.append(move.specialMovePiece)  # type: ignore[arg-type]
            if move.piece.side == WHITE:
                self.points += move.specialMovePiece.value - 1  # type: ignore[attr-defined]  # noqa: E501
            if move.piece.side == BLACK:
                self.points -= move.specialMovePiece.value - 1  # type: ignore[attr-defined]  # noqa: E501
            move.piece.movesMade += 1

        else:
            pieceToMove = move.piece
            pieceToTake = move.pieceToCapture

            if pieceToTake:
                if pieceToTake.side == WHITE:
                    self.points -= pieceToTake.value
                if pieceToTake.side == BLACK:
                    self.points += pieceToTake.value
                self.pieces.remove(pieceToTake)

            self.movePieceToPosition(pieceToMove, move.newPos)
            pieceToMove.movesMade += 1
        self.movesMade += 1
        self.currentSide = not self.currentSide

    def getPointValueOfSide(self, side: bool) -> int:
        points = 0
        for piece in self.pieces:
            if piece.side == side:
                points += piece.value
        return points

    def getPointAdvantageOfSide(self, side: bool) -> int:
        return (
            self.getPointValueOfSide(side)
            - self.getPointValueOfSide(not side)
        )

    def getAllMovesUnfiltered(
            self, side: bool, includeKing: bool = True,
    ) -> list[Move]:
        unfilteredMoves = []
        for piece in self.pieces:
            if piece.side == side:
                if includeKing or piece.stringRep != 'K':
                    for move in piece.getPossibleMoves():
                        unfilteredMoves.append(move)
        return unfilteredMoves

    def testIfLegalBoard(self, side: bool) -> bool:
        for move in self.getAllMovesUnfiltered(side):
            pieceToTake = move.pieceToCapture
            if pieceToTake and pieceToTake.stringRep == 'K':
                return False
        return True

    def moveIsLegal(self, move: Move) -> bool:
        side = move.piece.side
        self.makeMove(move)
        isLegal = self.testIfLegalBoard(not side)
        self.undoLastMove()
        return isLegal

    # TODO: remove side parameter, unnecessary
    def getAllMovesLegal(self, side: bool) -> list[Move]:
        unfilteredMoves = list(self.getAllMovesUnfiltered(side))
        legalMoves = []
        for move in unfilteredMoves:
            if self.moveIsLegal(move):
                legalMoves.append(move)
        return legalMoves
