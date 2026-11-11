from src.Board import Board
from src.main import twoPlayerGame


def test_gm_command_does_not_report_invalid_move(monkeypatch, capsys):
    board = Board()
    inputs = iter(['gm', 'quit'])
    monkeypatch.setattr('builtins.input', lambda *args: next(inputs))
    twoPlayerGame(board)
    out = capsys.readouterr().out
    assert 'Invalid move' not in out
