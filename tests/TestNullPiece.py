import pytest

from src.Board import Board
from src.Piece import NullPiece


def test_getLastPieceMoved_on_empty_board():
    """Test that getLastPieceMoved returns NullPiece on empty board"""
    board = Board()

    lastPiece = board.getLastPieceMoved()

    assert isinstance(lastPiece, NullPiece)
    assert lastPiece is not None


def test_nullpiece_is_falsy():
    """Test that NullPiece evaluates to False in boolean context"""
    board = Board()
    lastPiece = board.getLastPieceMoved()

    if lastPiece:
        pytest.fail('NullPiece should be falsy')
    else:
        pass  # Expected


def test_nullpiece_properties():
    """Test that NullPiece has all expected properties"""
    nullPiece = NullPiece()

    assert nullPiece.stringRep == ''
    assert nullPiece.value == 0
    assert nullPiece.movesMade == 0
    assert nullPiece.position == (0, 0)
    assert nullPiece.board is None
    assert nullPiece.side is None


def test_getLastPieceMoved_after_real_move(makeBoardMoves):
    """Test that getLastPieceMoved returns real Piece after a move"""
    board = Board()

    makeBoardMoves(board, ['e4'])

    lastPiece = board.getLastPieceMoved()

    # Should NOT be a NullPiece anymore
    assert not isinstance(lastPiece, NullPiece)
    assert lastPiece is not None
    assert bool(lastPiece) is True
    assert lastPiece.stringRep == '▲'  # Pawn


def test_nullpiece_string_representation():
    """Test string representation of NullPiece"""
    nullPiece = NullPiece()

    assert str(nullPiece) == 'NullPiece (no piece)'


def test_nullpiece_equality():
    """Test that NullPiece instances are equal to each other"""
    nullPiece1 = NullPiece()
    nullPiece2 = NullPiece()

    assert nullPiece1 == nullPiece2


def test_nullpiece_has_no_moves():
    """Test that NullPiece has no possible moves"""
    nullPiece = NullPiece()

    moves = list(nullPiece.getPossibleMoves())
    assert moves == []


def test_compatibility_with_pawn_code():
    """Test that existing Pawn.py code works with NullPiece"""
    board = Board()

    # Simulates code in Pawn.py line 100
    lastPieceMoved = board.getLastPieceMoved()

    # This should work without errors
    assert lastPieceMoved.stringRep == ''  # NullPiece has empty stringRep

    # Identity check should work
    somePiece = board.pieces[0]
    assert lastPieceMoved is not somePiece
