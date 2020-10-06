from board import Board
from constants import *
from algorithm import rand, blocking, best_move
from time import sleep


class Game:
    def __init__(self, num_players):
        self.board = Board()
        self.turn = 1
        self.num_players = num_players

    def convert(self, mouse_pos):
        mouse_x, mouse_y = mouse_pos
        new_x = mouse_x // (WIDTH // COLS)
        new_y = mouse_y // (HEIGHT // ROWS)
        return (new_x, new_y)

    def update(self):
        self.board.draw()

    def human_move(self, pos):
        self.board.place_piece(pos, self.turn)
        self.change_turn()

    def comp_move(self):
        sleep(1)
        self.board.place_piece(best_move(self.board, self.turn), self.turn)
        self.change_turn()

    def change_turn(self):
        if self.turn == 1:
            self.turn = -1
        else:
            self.turn = 1

    def reset(self):
        self.board = Board()
        self.turn = 1
