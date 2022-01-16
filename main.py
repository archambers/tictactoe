import pygame
from sys import argv
from constants import *
from game import Game

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("tictactoe")
clock = pygame.time.Clock()

num_players = argv[1]

def main():
    run = True
    finished = False
    game = Game(num_players)

    game.update()
    pygame.display.update()
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game.reset()
                    finished = False

        while not finished:

            if game.num_players == '2':
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = game.convert(pygame.mouse.get_pos())
                        game.human_move(pos)

            elif game.num_players == '10':
                if game.turn == 1:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pos = game.convert(pygame.mouse.get_pos())
                            game.human_move(pos)
                else:
                    game.comp_move()

            elif game.num_players == '01':
                if game.turn == -1:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pos = game.convert(pygame.mouse.get_pos())
                            game.human_move(pos)
                else:
                    game.comp_move()

            else:
                game.comp_move()

            if game.board.game_over():
                result = game.board.check_win()
                if result == 1:
                    print('RED WINS')
                    finished = True
                elif result == -1:
                    print('BLUE WINS')
                    finished = True  
                else:
                    print('CATS GAME')
                    finished = True

            game.update()
            pygame.display.update()


    pygame.quit()


if __name__ == '__main__':
    main()