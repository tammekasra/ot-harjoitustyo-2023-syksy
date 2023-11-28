class SudokuSolver:
    def is_valid_move(board, row, col, num): #we check if we have valid moves
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False

        return True

    def solve_sudoku(board):  #we check if the sudoku is indeed solvable or not
        empty_cell = SudokuSolver.find_empty_cell(board)  #finds the empty cells
        if not empty_cell:
            return True

        row, col = empty_cell
        for num in range(1, 10):
            if SudokuSolver.is_valid_move(board, row, col, num):
                board[row][col] = num

                if SudokuSolver.solve_sudoku(board): #we check if indeed it is solavabe
                    return True

                board[row][col] = 0

        return False

    def find_empty_cell(board): # Finds the empty cells
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return None