import pygame
import numpy as np
import chess

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
        white_pieces = ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
        white_pawns = ['wp' for i in range(8)]
        black_pawns = ['bp' for i in range(8)]
        blank = ['--' for i in range(8)]
        black_pieces = ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR']
        self.board = np.array([black_pieces,black_pawns,blank,blank,blank,blank,white_pawns,white_pieces])

    def make_move(self, start, end):
        board = chess.Board()
        print(board, start, end)

class Move:
    def __init__(self):
        pass


def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color('white'))
    gamestate = ChessEngine()
    loadimage()
    running = True
    sq_selected = () # выбранная область
    moves = [] #[(x,y),(x,y)] - координаты хода
    while running:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                running = False
            elif i.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos() # x,y
                column = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if sq_selected == (row, column): #если кликлун туда же
                    sq_selected = () #очистить выбор
                    moves = [] #очистить ходы
                else:
                    sq_selected = (row, column)
                    moves.append(sq_selected) #добавляем 1 и 2 клики
                print(sq_selected, moves)
                if len(moves) % 2 == 0: #после хода белых и черных
                    start = moves[0]
                    end = moves[1]
                    gamestate.make_move(start, end)



        draw_game(screen, gamestate)
        clock.tick(fps)
        pygame.display.flip()

def draw_game(screen, gamestate):
    draw_squares(screen)

    draw_pieces(screen, gamestate.board)

def draw_squares(screen):
    colors = [pygame.Color('white'), pygame.Color('gray')]
    for i in range(dimension):
        for z in range(dimension):
            color = colors[((i+z) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(z*SQ_SIZE, i*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def draw_pieces(screen, board):
    for i in range(dimension):
        for z in range(dimension):
            piece = board[i][z]
            if piece != '--':
                screen.blit(images[piece], pygame.Rect(z*SQ_SIZE, i*SQ_SIZE, SQ_SIZE, SQ_SIZE)) #блиттинг (копирование битов) изображения в опр позицию

'''def chess_lib(square, moves):
    board = chess.Board()
    piece_cords = 1
    is_legal = 1'''

if __name__ == '__main__':
    main()