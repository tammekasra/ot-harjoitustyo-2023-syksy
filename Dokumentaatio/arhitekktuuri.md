```mermaid
classDiagram

class SudokuApp {
  - main()
  - initialize_game()
  - run_game()
}

class SudokuGame {
  - board: List<List<int>>
  - font: PygameFont


  + draw_board
  + is_valid_move(check if it is the correct slot)
  + solve_sudoku( solves the sudoku)
}

class SudokuSolver {
  + is_valid_move(says if it can be played there or not)
  + find_empty_cell(board) : Tuple<int, int> or None
}

SudokuApp --> SudokuGame : contains
SudokuGame --> SudokuSolver : uses
