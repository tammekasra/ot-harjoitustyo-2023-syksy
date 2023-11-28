import unittest
from Sudoku.game import SudokuGame

class TestSudokuGame(unittest.TestCase):
    def setUp(self):
        self.game = SudokuGame()

    def test_board(self):
        initial_board =  [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                      [6, 0, 0, 1, 9, 5, 0, 0, 0],
                      [0, 9, 8, 0, 0, 0, 0, 6, 0],
                      [8, 0, 0, 0, 6, 0, 0, 0, 3],
                      [4, 0, 0, 8, 0, 3, 0, 0, 1],
                      [7, 0, 0, 0, 2, 0, 0, 0, 6],
                      [0, 6, 0, 0, 0, 0, 2, 8, 0],
                      [0, 0, 0, 4, 1, 9, 0, 0, 5],
                      [0, 0, 0, 0, 8, 0, 0, 7, 9]]
           
        self.assertEqual(self.game.board, initial_board)

    def test_valid_move(self): #we test if the number 4 on row 0 and col 2 is is indeed 4 (which is the only correct one)
        row, col, num = 0, 2, 4
        result = self.game.is_valid_move(row, col, num)
        self.assertTrue(result)
        
        row, col, num = 0, 2, 5 # test if the number 5 on row 0 and column 2 is indeed 5
        result = self.game.is_valid_move(row, col, num)
        self.assertFalse(result)

    def test_solve_sudoku(self):
    
        result = self.game.solve_sudoku() #we see if the sudoku table is indeed solvable
        self.assertTrue(result)

        for row in self.game.board: #we check if the values are not 0
            for num in row:
                self.assertNotEqual(num, 0)