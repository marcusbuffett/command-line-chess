from Move import Move
from Coordinate import Coordinate as C


class InputParser:

    def __init__(self, board, side):
        self.board = board
        self.side = side

    def parse(self, humanInput):

        humanInput = humanInput.lower()
        regexLongNotation = re.compile('[a-z][1-8][a-z][1-8]')
        if regexLongNotation.match(humanInput):
            return self.moveForLongNotation(humanInput)

        regexShortNotation = re.compile('[rnbkqp][a-z][1-8]')
        if regexShortNotation.match(humanInput):
            return self.moveForShortNotation(humanInput)

    def moveForLongNotation(self, notation):
        transTable = str.maketrans('abcdefgh', '01234567')
        humanInput = humanInput.translate(transTable)
        humanInput = [int(c) for c in humanInput]
        oldPos = C(humanInput[0], humanInput[1])
        newPos = C(humanInput[2], humanInput[3])
        return Move(oldPos, newPos)

    def moveForShortNotation(self, notation):
        moves = self.getLegalMovesWithShortNotation(self.side)
        for move in moves:
            if move.notation.lower() == notation.lower():
                return move

    def notationForMove(self, move):
        side = self.board.getSideOfMove(move)
        moves = self.getLegalMovesWithShortNotation(side)
        for m in moves:
            if m == move:
                return m.notation

    def getLegalMovesWithShortNotation(self, side):
        moves = []
        for legalMove in self.board.getAllMovesLegal(side):
            moves.append(legalMove)
            legalMove.notation = self.board.getShortNotationOfMove(legalMove)

        duplicateNotationMoves = self.duplicateMovesFromMoves(moves)
        for duplicateMove in duplicateNotationMoves:
            duplicateMove.notation = \
                self.board.getShortNotationOfMoveWithFile(duplicateMove)

        duplicateNotationMoves = self.duplicateMovesFromMoves(moves)
        for duplicateMove in duplicateNotationMoves:
            duplicateMove.notation = \
                self.board.getShortNotationOfMoveWithRank(duplicateMove)

        duplicateNotationMoves = self.duplicateMovesFromMoves(moves)
        for duplicateMove in duplicateNotationMoves:
            duplicateMove.notation = \
                self.board.getShortNotationOfMoveWithFileAndRank(duplicateMove)

        return moves

    def duplicateMovesFromMoves(self, moves):
        return list(filter(
            lambda move:
            len([m for m in moves if m.notation == move.notation]) > 1, moves))
