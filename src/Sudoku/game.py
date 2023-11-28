# sudoku/game.py

import pygame
import sys
from Sudoku.solver import SudokuSolver


pygame.init()
pygame.font.init()
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# Screen dimensions
SCREEN_WIDTH = 540
SCREEN_HEIGHT = 600

# Grid dimensions
GRID_SIZE = 9
CELL_SIZE = SCREEN_WIDTH // GRID_SIZE

class SudokuGame:
    def __init__(self):
        self.board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                      [6, 0, 0, 1, 9, 5, 0, 0, 0],
                      [0, 9, 8, 0, 0, 0, 0, 6, 0],
                      [8, 0, 0, 0, 6, 0, 0, 0, 3],
                      [4, 0, 0, 8, 0, 3, 0, 0, 1],
                      [7, 0, 0, 0, 2, 0, 0, 0, 6],
                      [0, 6, 0, 0, 0, 0, 2, 8, 0],
                      [0, 0, 0, 4, 1, 9, 0, 0, 5],
                      [0, 0, 0, 0, 8, 0, 0, 7, 9]]
        self.selected = None
        self.font = pygame.font.SysFont("comicsans", 40)

    def draw_board(self, screen):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                x, y = j * CELL_SIZE, i * CELL_SIZE

                # Draw grid lines
                pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE), 1)

                # Draw initial values
                if self.board[i][j] != 0:
                    value = self.font.render(str(self.board[i][j]), True, BLACK)
                    screen.blit(value, (x + CELL_SIZE // 3, y + CELL_SIZE // 4))

                # Draw user input
                elif self.board[i][j] != 0:
                    value = self.font.render(str(self.board[i][j]), True, GRAY)
                    screen.blit(value, (x + CELL_SIZE // 3, y + CELL_SIZE // 4))

        # Highlight selected cell
        if self.selected:
            pygame.draw.rect(screen, (0, 128, 255), (self.selected[1] * CELL_SIZE, self.selected[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)

    def is_valid_move(self, row, col, num):
        for i in range(GRID_SIZE):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == num:
                    return False

        return True

    def solve_sudoku(self):
        empty_cell = SudokuSolver.find_empty_cell(self.board)
        if not empty_cell:
            return True

        row, col = empty_cell
        for num in range(1, 10):
            if self.is_valid_move(row, col, num):
                self.board[row][col] = num

                if SudokuSolver.solve_sudoku(self.board):
                    return True

                self.board[row][col] = 0

        return False

    def find_empty_cell(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.board[i][j] == 0:
                    return i, j
        return None

    def draw_message(self, screen, message):
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render(message, True, BLACK)
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))

    def run_game(self):
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Sudoku Game")

        clock = pygame.time.Clock()
        running = True

        while running:
            clock.tick(10)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    col, row = pos[0] // CELL_SIZE, pos[1] // CELL_SIZE
                    self.selected = (row, col)
                elif event.type == pygame.KEYDOWN:
                    if self.selected and self.board[self.selected[0]][self.selected[1]] == 0:
                        if event.key in range(pygame.K_1, pygame.K_9 + 1):
                            num = event.key - pygame.K_0
                            if self.is_valid_move(self.selected[0], self.selected[1], num):
                                self.board[self.selected[0]][self.selected[1]] = num
                        elif event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                            self.board[self.selected[0]][self.selected[1]] = 0
                        elif event.key == pygame.K_SPACE:
                            self.solve_sudoku()

            screen.fill(WHITE)
            self.draw_board(screen)

            # Check if the puzzle is solved
            if self.find_empty_cell() is None:
                self.draw_message(screen, "Sudoku Solved!")

            pygame.display.flip()

        pygame.quit()
        sys.exit()