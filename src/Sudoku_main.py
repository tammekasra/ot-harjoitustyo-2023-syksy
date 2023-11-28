import random

def is_valid_move(grid, row, col, num):
    # Check if the number is not present in the current row or column
    return (
        num not in grid[row] and
        num not in (grid[i][col] for i in range(9)) and
        num not in (
            grid[i][j]
            for i in range(3 * (row // 3), 3 * (row // 3) + 3)
            for j in range(3 * (col // 3), 3 * (col // 3) + 3)
        )
    )

def fill_sudoku(grid):
    # Iterate through each cell in the grid
    for row in range(9):
        for col in range(9):
            # Try filling a random number from 1 to 9
            for num in random.sample(range(1, 10), 9):
                if is_valid_move(grid, row, col, num):
                    grid[row][col] = num
                    break
            else:
                # If no valid number is found, backtrack
                return False
    return True

def print_sudoku(grid):
    for row in grid:
        print(" ".join(map(str, row)))

# Initialize an empty 9x9 grid
sudoku_grid = [[0] * 9 for _ in range(9)]

# Fill the Sudoku grid
if fill_sudoku(sudoku_grid):
    print("Sudoku Puzzle:")
    print_sudoku(sudoku_grid)
else:
    print("Unable to generate a valid Sudoku puzzle.")
