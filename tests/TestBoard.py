import pytest

from src.Board import Board


@pytest.mark.parametrize(
    'moves',
    [
        # Scholar’s mate
        ['e4', 'e5', 'Bc4', 'Nc6', 'Qh5', 'Nf6', 'Qxf7'],
        # Fool’s mate
        ['e4', 'g5', 'Nc3', 'f5', 'Qh5'],
        ['g4', 'e5', 'f3', 'Qh4'],
        # Smothered Checkmate
        ['e4', 'e5', 'Ne2', 'Nc6', 'Nbc3', 'Nd4', 'g3', 'Nf3'],
        # Hippopotamus mate
        [
            'e4',
            'e5',
            'Ne2',
            'Qh4',
            'Nbc3',
            'Nc6',
            'g3',
            'Qg5',
            'd4',
            'Nxd4',
            'Bxg5',
            'Nf3',
        ],
        # Legal’s mate
        [
            'e4',
            'e5',
            'Bc4',
            'd6',
            'Nf3',
            'Bg4',
            'Nc3',
            'g6',
            'Nxe5',
            'Bxd1',
            'Bxf7',
            'Ke7',
            'Nd5',
        ],
    ],
)
def testMate(moves, makeBoardMoves):
    board = Board()

    makeBoardMoves(board, moves)

    assert board.isCheckmate()
