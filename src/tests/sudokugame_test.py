import pytest
from Sudoku.game import SudokuGame
from Sudoku.solver import SudokuSolver

@pytest.fixture
def empty_game():
    return SudokuGame()

@pytest.fixture
def sample_game():
    return SudokuGame()

def test_initialization(empty_game):
    assert empty_game.board == [[0] * 9 for _ in range(9)]
    assert empty_game.selected is None
    assert empty_game.font is not None

def test_draw_board(empty_game, capsys):
    empty_game.draw_board(None)
    captured = capsys.readouterr()
    assert "draw_board" in captured.out

def test_is_valid_move(empty_game):
    empty_game.board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    assert empty_game.is_valid_move(0, 2, 4)  
    assert not empty_game.is_valid_move(0, 2, 3)

def test_solve_sudoku(empty_game):
   
    empty_game.solve_sudoku()
    assert empty_game.find_empty_cell() is None