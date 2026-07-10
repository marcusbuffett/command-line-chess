"""Unit tests for InputParser move parsing."""

import pytest

from src.Board import Board
from src.InputParser import InputParser


class TestInputParserCoordinateNotation:
    """Tests for parsing coordinate notation (e.g., e2e4)."""

    def test_parse_valid_coordinate_notation(self):
        """Valid coordinate notation should return a Move."""
        board = Board()
        parser = InputParser(board, True)  # White side
        # e2e4 is a valid opening move for white
        move = parser.parse("e2e4")
        assert move is not None

    def test_parse_coordinate_notation_case_insensitive(self):
        """Coordinate notation should be case-insensitive."""
        board = Board()
        parser = InputParser(board, True)
        # Should work with uppercase
        move = parser.parse("E2E4")
        assert move is not None

    def test_parse_invalid_coordinate_raises(self):
        """Invalid coordinate notation should raise ValueError."""
        board = Board()
        parser = InputParser(board, True)
        with pytest.raises(ValueError):
            parser.parse("z9z9")

    def test_parse_illegal_move_raises(self):
        """Legal notation but illegal move should raise ValueError."""
        board = Board()
        parser = InputParser(board, True)
        # e1e5 is not a legal move from starting position (King can't jump there)
        with pytest.raises(ValueError):
            parser.parse("e1e5")


class TestInputParserAlgebraicNotation:
    """Tests for parsing algebraic notation (e.g., e4, Nf3)."""

    def test_parse_pawn_move(self):
        """Simple pawn move like e4 should parse."""
        board = Board()
        parser = InputParser(board, True)
        move = parser.parse("e4")
        assert move is not None

    def test_parse_knight_move(self):
        """Knight move like Nf3 should parse."""
        board = Board()
        parser = InputParser(board, True)
        move = parser.parse("Nf3")
        assert move is not None

    def test_parse_invalid_algebraic_raises(self):
        """Completely invalid notation should raise ValueError."""
        board = Board()
        parser = InputParser(board, True)
        with pytest.raises(ValueError):
            parser.parse("xyz123")

    def test_parse_empty_string_raises(self):
        """Empty string should raise ValueError."""
        board = Board()
        parser = InputParser(board, True)
        with pytest.raises(ValueError):
            parser.parse("")
