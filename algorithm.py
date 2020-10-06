from random import choice, shuffle
from collections import deque
from board import Board

def minimax(board, max_player, depth, piece):
    if depth == 0 or board.game_over():
        return board.check_win() * piece

    if max_player:
        max_score = -100
        for square in board.empty():
            new_board = Board(board.copy())
            new_board.place_piece(square, piece)
            score = minimax(new_board, False, depth - 1, piece)
            max_score = max(max_score, score)
        return max_score

    else:
        min_score = 100
        for square in board.empty():
            new_board = Board(board.copy())
            new_board.place_piece(square, piece * -1)
            score = minimax(new_board, True, depth - 1, piece)
            min_score = min(min_score, score)
        return min_score

def best_move(board, piece):

    scores = []
    for square in board.empty():
        new_board = Board(board.copy())
        new_board.place_piece(square, piece)
        score = minimax(new_board, False, 7, piece)
        scores.append((score, square))
    max_scores = [s for s in scores if s[0] == max(scores)[0]]
    return choice(max_scores)[1]




def rand(board):
    moves = board.empty()
    return choice(moves)


def blocking(board, piece):
    block = []
    for square in board.empty():
        new_board = Board(board.copy())
        new_board.place_piece(square, piece) 
        if new_board.check_win() == piece:
            return square
    for square in board.empty():
        new_board = Board(board.copy())
        new_board.place_piece(square, piece * -1) 
        if new_board.check_win() == piece * -1:
            return square
    return rand(board)