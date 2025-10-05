import pytest

from src.Board import Board
from src.Move import NullMove


def test_getLastMove_on_empty_board():
    """Test that getLastMove returns NullMove on empty board"""
    board = Board()
    
    lastMove = board.getLastMove()
    
    # Should return a NullMove, not None
    assert isinstance(lastMove, NullMove)
    assert lastMove is not None


def test_nullmove_is_falsy():
    """Test that NullMove evaluates to False in boolean context"""
    board = Board()
    lastMove = board.getLastMove()
    
    # This is how it's used in Pawn.py
    if lastMove:
        pytest.fail("NullMove should be falsy")
    else:
        pass  # This is expected


def test_nullmove_properties():
    """Test that NullMove has all expected properties"""
    nullMove = NullMove()
    
    assert nullMove.notation == ''
    assert nullMove.checkmate is False
    assert nullMove.kingsideCastle is False
    assert nullMove.queensideCastle is False
    assert nullMove.promotion is False
    assert nullMove.passant is False
    assert nullMove.stalemate is False
    assert nullMove.piece is None
    assert nullMove.oldPos is None
    assert nullMove.newPos is None


def test_getLastMove_after_real_move(makeBoardMoves):
    """Test that getLastMove returns real Move after a move is made"""
    board = Board()
    
    makeBoardMoves(board, ['e4'])
    
    lastMove = board.getLastMove()
    
    # Should NOT be a NullMove anymore
    assert not isinstance(lastMove, NullMove)
    assert lastMove is not None
    assert bool(lastMove) is True  # Real moves are truthy


def test_nullmove_string_representation():
    """Test string representation of NullMove"""
    nullMove = NullMove()
    
    assert str(nullMove) == 'NullMove (no move history)'


def test_nullmove_equality():
    """Test that NullMove instances are equal to each other"""
    nullMove1 = NullMove()
    nullMove2 = NullMove()
    
    assert nullMove1 == nullMove2


def test_compatibility_with_existing_code():
    """Test that existing Pawn.py code works with NullMove"""
    board = Board()
    
    # This simulates the code in Pawn.py line 106-113
    lastMove = board.getLastMove()
    lastMoveWasAdvanceTwo = False
    
    if lastMove:
        # This block should NOT execute for NullMove
        pytest.fail("Should not enter this block with NullMove")
    
    # This should work without errors
    assert lastMoveWasAdvanceTwo is False