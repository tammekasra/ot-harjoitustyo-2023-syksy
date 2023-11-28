import unittest
from Sudoku.game import SudokuGame  # Import the sudoku game itself to do the tests
class TestSudokuGame(unittest.TestCase):

    def setUp(self):
        # We initialize the test
        self.sudoku_game = SudokuGame()

    def test_is_valid_move(self):
        # Check is number 4 is correct on 0x2
        self.assertTrue(self.sudoku_game.is_valid_move(0, 2, 4))

        # Test if 3 is incorrect on 0 and 2
        self.assertFalse(self.sudoku_game.is_valid_move(0, 2, 3))

    def test_solve_sudoku(self):
        # Assuming your SudokuSolver is correctly implemented
        self.assertTrue(self.sudoku_game.solve_sudoku())
        self.assertIsNone(self.sudoku_game.find_empty_cell())