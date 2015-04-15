import re


class InputParser:

    def __init__(self, board, side):
        self.board = board
        self.side = side

    def parse(self, humanInput):
        humanInput = humanInput.lower()
        regexShortNotation = re.compile('[rnbkqp][a-z][1-8]')
        if regexShortNotation.match(humanInput):
            return self.moveForShortNotation(humanInput)

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
