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
        #self.board = np.array([black_pieces,black_pawns,blank,blank,blank,blank,white_pawns,white_pieces])
        self.board = [black_pieces, black_pawns, blank, blank, blank, blank, white_pawns, white_pieces]
        self.move_log = []
    def make_move(self, start, end):
        board = chess.Board()
        print(board, start, end)
        start_row = start[0]
        start_column = start[1]
        end_row = end[0]
        end_column = end[1]
        piece_moved = self.board[start_row][start_column]
        #piece_captured = self.board[end_row][end_column]
        self.board[start_row][start_column] = '--'
        self.board[end_row][end_column] = piece_moved

        self.move_log.append(self.notation(start, end))
        print(self.move_log)

    def notation(self, start, end):
        board_dict = {'a1': (7, 0), 'b1': 7, 'c1': 7, 'd1': 7, 'e1': 7, 'f1': 7, 'g1': 7, 'h1': 7, 'a2': (6, 0),
                      'b2': 7, 'c2': 7, 'd2': 7, 'e2': 7, 'f2': 7, 'g2': 7, 'h2': 7, 'a3': (5, 0), 'b3': 7, 'c3': 7,
                      'd3': 7, 'e3': 7, 'f3': 7, 'g3': 7, 'h3': 7, 'a4': 7, 'b4': 7, 'c4': 7, 'd4': 7, 'e4': 7, 'f4': 7,
                      'g4': 7, 'h4': 7, 'a5': 7, 'b5': 7, 'c5': 7, 'd5': 7, 'e5': 7, 'f5': 7, 'g5': 7, 'h5': 7, 'a6': 7,
                      'b6': 7, 'c6': 7, 'd6': 7, 'e6': 7, 'f6': 7, 'g6': 7, 'h6': 7, 'a7': 7, 'b7': 7, 'c7': 7, 'd7': 7,
                      'e7': 7, 'f7': 7, 'g7': 7, 'h7': 7, 'a8': 7, 'b8': 7, 'c8': 7, 'd8': 7, 'e8': 7, 'f8': 7, 'g8': 7,
                      'h8': 7}
        row_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        move = ''
        if start in board_dict.values():
            for key, value in board_dict.items():
                if value == start:
                    move += key
                elif value == end:
                    move += key
        return move


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
                if len(moves) == 2: #после хода белых и черных
                    start = moves[0]
                    end = moves[1]
                    gamestate.make_move(start, end)
                    sq_selected = ()
                    moves = []



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