import pygame
import numpy as np


width = height = 512
dimension = 8
SQ_SIZE = height // dimension
fps = 30
images = {}
def loadimage():
    figures = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for role in figures:
        images[role] = pygame.transform.scale(pygame.image.load('images/'+role+'.png'), (SQ_SIZE, SQ_SIZE))


class ChessEngine:
    def __init__(self):
        white_pieces = ['wR', 'wN', 'bK', 'wQ', 'wK', 'bK', 'wN', 'wR']
        white_pawns = ['wp' for i in range(8)]
        black_pawns = ['bp' for i in range(8)]
        blank = ['--' for i in range(8)]
        black_pieces = ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR']
        self.board = np.array([[black_pieces],[black_pawns],[blank],[blank],[blank],[blank],[white_pawns],[white_pieces]])


def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color('white'))
    gamestate = ChessEngine()
    loadimage()
    running = True
    while running:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                running = False
        draw_game(screen, gamestate)
        clock.tick(fps)
        pygame.display.flip()

def draw_game(screen, gamestate):
    draw_squares(screen)

    draw_pieces(screen, gamestate.board)

def draw_squares(screen):
    colors = [pygame.Color('white'), pygame.Color('black')]
    for i in range(dimension):
        for z in range(dimension):
            color = colors[((i+z) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(i*SQ_SIZE, z*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def draw_pieces(screen, board):
    pass

if __name__ == '__main__':
    main()