import random

def valid_move(grid, row, col, num):
    # This Function allows to generate random numbers such that it can be inputted there
    return (
        num not in grid[row] and
        num not in (grid[i][col] for i in range(9)) and
        num not in (
            grid[i][j]
            for i in range(3 * (row // 3), 3 * (row // 3) + 3) #check if it is not on the same row
            for j in range(3 * (col // 3), 3 * (col // 3) + 3) #checks if it is not on the same column
        )
    )

def fill_sudoku(grid):
    #  We are filling the sudoku while generating random tables (so it wont be the same sudoku every time)
    for row in range(9):
        for col in range(9):
            # Try filling a random number from 1 to 9
            for num in random.sample(range(1, 10), 9):
                if valid_move(grid, row, col, num):
                    grid[row][col] = num
                    break
            else:
                # backtrack if it is false or can not get a valid puzzle generated from there - so we generate again from the start using another input
                return False
    return True

#we print the game - when we have finally generated it
def print_sudoku(grid):
    for row in grid:
        print(" ".join(map(str, row))) #map converts str to columns and rows to rows so it will be printed like that more easily, rather than through 2 for loops

#sudoku table - empty filled with 0
sudoku_grid = [[0] * 9 for _ in range(9)]

# replaces 0 with number from 1-9 such that it is a sudoku game
if fill_sudoku(sudoku_grid):
    print("Sudoku:")
    print_sudoku(sudoku_grid)
else:
    print("Unable to generate - bad puzzle input")
