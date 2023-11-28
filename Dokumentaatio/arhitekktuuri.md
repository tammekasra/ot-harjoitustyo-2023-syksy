```mermaid
classDiagram

class SudokuApp {
  - main()
  - initialize_game()
  - run_game()
}

class SudokuGame {
  - board: List<List<int>>
  - selected: Tuple<int, int> or None
  - font: PygameFont


  + draw_board(screen)
  + is_valid_move(row, col, num)
  + solve_sudoku()
  + find_empty_cell() : Tuple<int, int> or None
  + draw_message(screen, message)
  + run_game()
}

class SudokuSolver {
  + is_valid_move(board, row, col, num) : bool
  + solve_sudoku(board) : bool
  + find_empty_cell(board) : Tuple<int, int> or None
}

SudokuApp --> SudokuGame : contains
SudokuGame --> SudokuSolver : uses
