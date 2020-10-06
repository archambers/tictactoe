import pygame
from constants import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

class Board:
    def __init__(self, setup=None):
        if setup is None:
            self.grid = [[0 for col in range(COLS)]
                         for row in range(ROWS)]
        else:
            self.grid = setup

    def draw(self):

        pygame.draw.rect(WIN, DIVIDER, (0, 0, WIDTH, HEIGHT))

        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(WIN, WHITE,
                         (col * (BOX_WIDTH + DIVIDER_SIZE),
                          row * (BOX_HEIGHT + DIVIDER_SIZE),
                          BOX_WIDTH, BOX_HEIGHT))

                if self.grid[row][col] == 1:
                    pygame.draw.circle(WIN, XS,
                               (col * (BOX_WIDTH + DIVIDER_SIZE) + (BOX_WIDTH // 2),
                                row * (BOX_HEIGHT + DIVIDER_SIZE) + (BOX_HEIGHT // 2)),
                               (BOX_HEIGHT // 2) - 15)

                elif self.grid[row][col] == -1:
                    pygame.draw.circle(WIN, OS,
                               (col * (BOX_WIDTH + DIVIDER_SIZE) + (BOX_WIDTH // 2),
                                row * (BOX_HEIGHT + DIVIDER_SIZE) + (BOX_HEIGHT // 2)),
                               (BOX_HEIGHT // 2) - 15)

    def place_piece(self, pos, piece_type):
        x, y = pos
        self.grid[y][x] = piece_type

    def empty(self):
        nulls = [(col, row) for row in range(ROWS) for col in range(COLS) if self.grid[row][col] == 0]
        return nulls

    def check_win(self):
        for row in range(ROWS):
            across = self.grid[row]
            if sum(across) == COLS:
                return 1
            if sum(across) == -COLS:
                return -1

        for col in range(COLS):
            down = [self.grid[row][col] for row in range(ROWS)]
            if sum(down) == ROWS:
                return 1
            if sum(down) == -ROWS:
                return -1

        diag1 = [self.grid[i][i] for i in range(ROWS)]
        if sum(diag1) == ROWS:
            return 1
        if sum(diag1) == -ROWS:
                return -1

        diag2 = [self.grid[i][-i - 1] for i in range(ROWS)]
        if sum(diag2) == ROWS:
            return 1
        if sum(diag2) == -ROWS:
            return -1

        return 0

    def game_over(self):
        if self.check_win() or not self.empty():
            return True
        else:
            return False

    def copy(self):
        new_grid = [[square for square in row] for row in self.grid]
        return new_grid
