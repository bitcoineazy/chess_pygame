import pygame
import numpy as np
import chess
import os

width = height = 1001
dimension = 8
SQ_SIZE = height // dimension
fps = 30
images = {}
#сделать массив фигур и нарисовать их

def loadimage():
    figures = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for role in figures:
        images[role] = pygame.transform.scale(pygame.image.load('images/'+role+'.png'), (SQ_SIZE, SQ_SIZE))


class ChessEngine:
    def __init__(self):
        hex_1 = ['bB']
        hex_2 = ['bQ', 'bK']
        hex_3 = ['bR', 'bB', 'bR']
        hex_4 = ['bp', 'bN', 'bN', 'bp']
        hex_5 = ['--', 'bp', 'bB', 'bp', '--']
        hex_6 = ['--', '--', 'bp', 'bp', '--', '--']
        hex_7 = ['--', '--', 'bp', '--', '--', '--']
        hex_8 = ['--' for i in range(6)]
        hex_9 = ['--' for i in range(5)]
        hex_10 = ['--' for i in range(6)]
        hex_11 = ['--' for i in range(5)]
        hex_12 = ['--' for i in range(6)]
        hex_13 = ['--' for i in range(5)]
        hex_14 = ['--' for i in range(6)]
        hex_15 = ['--', '--', 'wp', '--', '--', '--']
        hex_16 = ['--', '--', 'wp', 'wp', '--', '--']
        hex_17 = ['--', 'wp', 'wB', 'wp', '--']
        hex_18 = ['wp', 'wN', 'wN', 'wp']
        hex_19 = ['wR', 'wB', 'wR']
        hex_20 = ['wQ', 'wK']
        hex_21 = ['wB']

        white_pieces = ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
        white_pawns = ['wp' for i in range(8)]
        black_pawns = ['bp' for i in range(8)]
        blank1 = ['--' for i in range(8)]
        blank2 = ['--' for i in range(8)]
        blank3 = ['--' for i in range(8)]
        blank4 = ['--' for i in range(8)]
        black_pieces = ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR']
        #self.board = np.array([black_pieces,black_pawns,blank,blank,blank,blank,white_pawns,white_pieces])
        self.board = [black_pieces, black_pawns, blank1, blank2, blank3, blank4, white_pawns, white_pieces]
        self.move_log = []
        self.chess = []
        self.chess_table = chess.Board()


    def make_move(self, start, end):
        #board = chess.Board()
        #print(board, start, end)
        uci_move_1 = chess.Move.from_uci(self.notation(start, end))
        print(self.notation(start, end))
        start_row = start[0]
        start_column = start[1]
        end_row = end[0]
        end_column = end[1]
        piece_moved = self.board[start_row][start_column]
        #piece_captured = self.board[end_row][end_column]
        if not self.chess_table.is_game_over(claim_draw=True):
            '''checkmate, stalemate, insufficient material, the seventyfive-move rule, fivefold repetition or a variant end condition'''
            if uci_move_1 in self.chess_table.legal_moves:
                if not self.chess_table.is_castling(uci_move_1):
                    self.board[start_row][start_column] = '--'


                self.board[end_row][end_column] = piece_moved

                #print(self.notation(start, end))
                self.move_log.append(self.notation(start, end))
                print(self.move_log)
                self.chess_table.push(uci_move_1)
            else:
                print('нету в списке легал')
                print(self.chess_table.legal_moves)
        else:
            print('Игра окончена')

    def notation(self, start, end):
        board_dict = {'a1': (7, 0), 'b1': (7, 1), 'c1': (7, 2), 'd1': (7, 3), 'e1': (7, 4), 'f1': (7, 5), 'g1': (7, 6), 'h1': (7, 7), 'a2': (6, 0),
                      'b2': (6, 1), 'c2': (6, 2), 'd2': (6, 3), 'e2': (6, 4), 'f2': (6, 5), 'g2': (6, 6), 'h2': (6, 7), 'a3': (5, 0), 'b3': (5, 1), 'c3': (5, 2),
                      'd3': (5, 3), 'e3': (5, 4), 'f3': (5, 5), 'g3': (5, 6), 'h3': (5, 7), 'a4': (4, 0), 'b4': (4, 1), 'c4': (4, 2), 'd4': (4, 3), 'e4': (4, 4), 'f4': (4, 5),
                      'g4': (4, 6), 'h4': (4, 7), 'a5': (3, 0), 'b5': (3, 1), 'c5': (3, 2), 'd5': (3, 3), 'e5': (3, 4), 'f5': (3, 5), 'g5': (3, 6), 'h5': (3, 7), 'a6': (2, 0),
                      'b6': (2, 1), 'c6': (2, 2), 'd6': (2, 3), 'e6': (2, 4), 'f6': (2, 5), 'g6': (2, 6), 'h6': (2, 7), 'a7': (1, 0), 'b7': (1, 1), 'c7': (1, 2), 'd7': (1, 3),
                      'e7': (1, 4), 'f7': (1, 5), 'g7': (1, 6), 'h7': (1, 7), 'a8': (0, 0), 'b8': (0, 1), 'c8': (0, 2), 'd8': (0, 3), 'e8': (0, 4), 'f8': (0, 5), 'g8': (0, 6),
                      'h8': (0, 7)}
        #row_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        move_start = ''
        move_end = ''
        for key, value in board_dict.items():
            if value == start:
                move_start += key
            elif value == end:
                move_end += key
        move = move_start + move_end
        return move

    def is_check(self):
        pass



def main():
    pygame.init()
    chess_icon = pygame.image.load(os.path.join('chess_icon.png'))
    pygame.display.set_icon(chess_icon)
    pygame.display.set_caption('Chess')
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color('white'))
    gamestate = ChessEngine()
    loadimage()

    running = True
    sq_selected = () # выбранная область
    moves = [] #[(x,y),(x,y)] - координаты хода

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos() # (x,y)
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
                    #print(f'{start[0]} s')
                    end = moves[1]
                    gamestate.make_move(start, end)

                    sq_selected = ()
                    moves = []
            elif event.type == pygame.KEYDOWN:
                pass

        draw_game(screen, gamestate)
        clock.tick(fps)
        pygame.display.flip()


def draw_game(screen, gamestate):
    draw_squares(screen)
    #draw_pieces(screen, gamestate.board)


class Hexagons:
    def __init__(self, xc, yc, st):
        self.xc = xc  # координата центра на оси абсцисс
        self.yc = yc  # координата центра на оси ординат

        self.st = st  # размер под ключ
        self.r = st / 2  # радиус вписанной окружности
        self.R = st / pow(3, .5)  # радиус описанной окружности
        self.a = self.R  # сторона шестиугольника
        self.points = [(self.xc + self.a / 2, self.yc + self.r),  # массив координат вершин
                       (self.xc + self.R, self.yc),
                       (self.xc + self.a / 2, self.yc - self.r),
                       (self.xc - self.a / 2, self.yc - self.r),
                       (self.xc - self.R, self.yc),
                       (self.xc - self.a / 2, self.yc + self.r)]

def draw_squares(screen):
    WHITE = (255, 255, 255)

    hex_unit = 22.5
    r1 = pygame.Rect((150, 20, 100, 75))
    colors = [pygame.Color('beige'), pygame.Color(255, 136, 0), pygame.Color('red')]
    pygame.draw.rect(screen, WHITE, (20, 20, 100, 75))
    pygame.draw.line(screen, WHITE,
                     [10, 30],
                     [290, 15], 3)
    start_cord = (500, 500)
    for part_1 in range(6):
        color = colors[((part_1) % 3)]
        hexagon_1 = Hexagons(500-(part_1*52), 900-(part_1*30), 60)
        pygame.draw.polygon(screen, color, hexagon_1.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_1.points)
    for part_2 in range(7):
        color = colors[((part_2 + 1) % 3)]
        hexagon_2 = Hexagons(552 - (part_2 * 52), 870 - (part_2 * 30), 60)
        pygame.draw.polygon(screen, color, hexagon_2.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_2.points)
    for part_3 in range(8):
        color = colors[((part_3 + 2) % 3)]
        hexagon_3 = Hexagons(604 - (part_3 * 52), 840 - (part_3 * 30), 60)
        pygame.draw.polygon(screen, color, hexagon_3.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_3.points)
    for part_4 in range(9):
        color = colors[((part_4 + 3) % 3)]
        hexagon_4 = Hexagons(656 - (part_4 * 52), 810 - (part_4 * 30), 60)
        pygame.draw.polygon(screen, color, hexagon_4.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_4.points)
    for part_5 in range(10):
        color = colors[((part_5 + 4) % 3)]
        hexagon_5 = Hexagons(708 - (part_5 * 52), 780 - (part_5 * 30), 60)
        pygame.draw.polygon(screen, color, hexagon_5.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_5.points)
    for part_6 in range(11):
        color = colors[((part_6 + 5) % 3)]
        hexagon_6 = Hexagons(760 - (part_6 * 52), 750 - (part_6 * 30), 60)
        pygame.draw.polygon(screen, color, hexagon_6.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_6.points)
    for part_7 in range(10):
        color = colors[((part_7 + 7) % 3)]
        hexagon_7 = Hexagons(760 - (part_7 * 52), 690 - (part_7 * 30), 60)
        pygame.draw.polygon(screen, color, hexagon_7.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_7.points)
    for part_8 in range(9):
        color = colors[((part_8) % 3)]
        hexagon_8 = Hexagons(760 - (part_8 * 52), 630 - (part_8 * 30), 60)
        pygame.draw.polygon(screen, color, hexagon_8.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_8.points)
    for part_9 in range(8):
        color = colors[((part_9 + 2) % 3)]
        hexagon_9 = Hexagons(760 - (part_9 * 52), 570 - (part_9 * 30), 60)
        pygame.draw.polygon(screen, color, hexagon_9.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_9.points)
    for part_10 in range(7):
        color = colors[((part_10 + 1) % 3)]
        hexagon_10 = Hexagons(760 - (part_10 * 52), 510 - (part_10 * 30), 60)
        pygame.draw.polygon(screen, color, hexagon_10.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_10.points)
    for part_11 in range(6):
        color = colors[((part_11) % 3)]
        hexagon_11 = Hexagons(760 - (part_11 * 52), 450 - (part_11 * 30), 60)
        pygame.draw.polygon(screen, color, hexagon_11.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_11.points)



    '''colors = [pygame.Color('beige'), pygame.Color(255, 136, 0)]
    for i in range(dimension):
        for z in range(dimension):
            color = colors[((i+z) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(z*SQ_SIZE, i*SQ_SIZE, SQ_SIZE, SQ_SIZE))'''

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