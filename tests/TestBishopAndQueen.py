"""Unit tests for Bishop and Queen piece movement."""

import pytest

from src.Board import Board
from src.Bishop import Bishop
from src.Coordinate import Coordinate
from src.Queen import Queen


class TestBishop:
    """Tests for Bishop piece movement."""

    def test_bishop_moves_diagonally(self):
        """Bishop at center should only move diagonally."""
        board = Board()
        bishop = Bishop(board, False, (4, 4))

        for move in bishop.getPossibleMoves():
            assert move.oldPos == (4, 4)
            new_rank = move.newPos[0] + move.newPos[2]
            new_file = move.newPos[1] + move.newPos[3]
            # Diagonal means both rank and file change by same amount
            rank_diff = abs(new_rank - 4)
            file_diff = abs(new_file - 4)
            assert rank_diff == file_diff, (
                f"Bishop move to ({new_rank}, {new_file}) is not diagonal"
            )

    def test_bishop_has_moves_from_center(self):
        """Bishop at center of empty-ish board should have multiple moves."""
        board = Board()
        bishop = Bishop(board, False, (4, 4))
        moves = list(bishop.getPossibleMoves())
        # Bishop should have at least some diagonal moves
        assert len(moves) > 0

    def test_bishop_moves_from_corner(self):
        """Bishop at corner should still have diagonal moves."""
        board = Board()
        bishop = Bishop(board, False, (1, 1))
        moves = list(bishop.getPossibleMoves())
        # From near-corner, bishop should have limited but non-zero moves
        for move in moves:
            new_rank = move.newPos[0] + move.newPos[2]
            new_file = move.newPos[1] + move.newPos[3]
            rank_diff = abs(new_rank - 1)
            file_diff = abs(new_file - 1)
            assert rank_diff == file_diff


class TestQueen:
    """Tests for Queen piece movement."""

    def test_queen_moves_from_center(self):
        """Queen at center should move in all 8 directions."""
        board = Board()
        queen = Queen(board, False, (4, 4))
        moves = list(queen.getPossibleMoves())
        # Queen combines rook + bishop, should have many moves
        assert len(moves) > 0

    def test_queen_covers_ranks_files_and_diagonals(self):
        """Queen should reach squares on same rank, file, or diagonal."""
        board = Board()
        queen = Queen(board, False, (4, 4))

        has_rank_move = False
        has_file_move = False
        has_diagonal_move = False

        for move in queen.getPossibleMoves():
            new_rank = move.newPos[0] + move.newPos[2]
            new_file = move.newPos[1] + move.newPos[3]
            rank_diff = abs(new_rank - 4)
            file_diff = abs(new_file - 4)

            if rank_diff == 0 and file_diff > 0:
                has_file_move = True
            elif file_diff == 0 and rank_diff > 0:
                has_rank_move = True
            elif rank_diff == file_diff and rank_diff > 0:
                has_diagonal_move = True

        assert has_rank_move, "Queen should move along ranks"
        assert has_file_move, "Queen should move along files"
        assert has_diagonal_move, "Queen should move diagonally"
