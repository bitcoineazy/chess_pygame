import pygame
import numpy as np
import chess
import os

height = 990
width = 900
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
        hex_1 = ['wB', 'wQ', 'wN', 'wR', 'wp', '--']
        hex_2 = ['wK', 'wB', '--', '--', 'wp', '--', '--']
        hex_3 = ['wN', '--', 'wB', '--', 'wp', '--', '--', '--']
        hex_4 = ['wR', '--', '--', '--', 'wp', '--', '--', '--', '--']
        hex_5 = ['wp', 'wp', 'wp', 'wp', 'wp', '--', '--', '--', '--', '--']
        hex_6 = ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
        hex_7 = ['--', '--', '--', '--', '--', 'bp', 'bp', 'bp', 'bp', 'bp']
        hex_8 = ['--', '--', '--', '--', 'bp', '--', '--', '--', 'bR']
        hex_9 = ['--', '--', '--', 'bp', '--', 'bB', '--', 'bN']
        hex_10 = ['--', '--', 'bp', '--', '--', 'bB', 'bQ']
        hex_11 = ['--', 'bp', 'bR', 'bN', 'bK', 'bB']


        #self.board = np.array([black_pieces,black_pawns,blank,blank,blank,blank,white_pawns,white_pieces])
        self.board = [hex_1, hex_2, hex_3, hex_4, hex_5, hex_6, hex_7, hex_8, hex_9, hex_10, hex_11]
        self.move_log = []
        self.chess = []
        self.recorded_centers_of_hexagons = {}
        self.chess_table = chess.Board()


    def make_move(self, start, end):
        #board = chess.Board()
        #print(board, start, end)
        #uci_move_1 = chess.Move.from_uci(self.notation(start, end))
        print(self.notation(start, end))
        start_row = start[0]
        start_column = start[1]
        end_row = end[0]
        end_column = end[1]
        #piece_moved = self.board[start_row][start_column]
        #piece_captured = self.board[end_row][end_column]
        '''if not self.chess_table.is_game_over(claim_draw=True):
            
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
            print('Игра окончена')'''

    def notation(self, start, end):
        board_dict = {'a1': (7, 0), 'b1': (7, 1), 'c1': (7, 2), 'd1': (7, 3), 'e1': (7, 4), 'f1': (7, 5), 'g1': (7, 6), 'h1': (7, 7), 'i1': (0, 0), 'k1': (0, 0), 'l1': (0, 0),
                      'a2': (6, 0), 'b2': (6, 1), 'c2': (6, 2), 'd2': (6, 3), 'e2': (6, 4), 'f2': (6, 5), 'g2': (6, 6), 'h2': (6, 7), 'i2': (0, 0), 'k2': (0, 0), 'l2': (0, 0),
                      'a3': (5, 0), 'b3': (5, 1), 'c3': (5, 2), 'd3': (5, 3), 'e3': (5, 4), 'f3': (5, 5), 'g3': (5, 6), 'h3': (5, 7), 'i3': (0, 0), 'k3': (0, 0), 'l3': (0, 0),
                      'a4': (4, 0), 'b4': (4, 1), 'c4': (4, 2), 'd4': (4, 3), 'e4': (4, 4), 'f4': (4, 5), 'g4': (4, 6), 'h4': (4, 7), 'i4': (0, 0), 'k4': (0, 0), 'l4': (0, 0),
                      'a5': (3, 0), 'b5': (3, 1), 'c5': (3, 2), 'd5': (3, 3), 'e5': (3, 4), 'f5': (3, 5), 'g5': (3, 6), 'h5': (3, 7), 'i5': (0, 0), 'k5': (0, 0), 'l5': (0, 0),
                      'a6': (2, 0), 'b6': (2, 1), 'c6': (2, 2), 'd6': (2, 3), 'e6': (2, 4), 'f6': (2, 5), 'g6': (2, 6), 'h6': (2, 7), 'i6': (0, 0), 'k6': (0, 0), 'l6': (0, 0),
                      'a7': (1, 0), 'b7': (1, 1), 'c7': (1, 2), 'd7': (1, 3), 'e7': (1, 4), 'f7': (1, 5), 'g7': (1, 6), 'h7': (1, 7), 'i7': (0, 0), 'k7': (0, 0), 'l7': (0, 0),
                      'a8': (0, 0), 'b8': (0, 1), 'c8': (0, 2), 'd8': (0, 3), 'e8': (0, 4), 'f8': (0, 5), 'g8': (0, 6), 'h8': (1, 7), 'i8': (0, 0), 'k8': (0, 0), 'l8': (0, 0),
                      'a9': (0, 0), 'b9': (0, 1), 'c9': (0, 2), 'd9': (0, 3), 'e9': (0, 4), 'f9': (0, 5), 'g9': (0, 6), 'h9': (1, 7), 'i9': (0, 0), 'k9': (0, 0), 'l9': (0, 0),
                      'a10': (0, 0), 'b10': (0, 1), 'c10': (0, 2), 'd10': (0, 3), 'e10': (0, 4), 'f10': (0, 5), 'g10': (0, 6), 'h10': (1, 7), 'i10': (0, 0), 'k10': (0, 0), 'l10': (0, 0),
                      'a11': (0, 0), 'b11': (0, 1), 'c11': (0, 2), 'd11': (0, 3), 'e11': (0, 4), 'f11': (0, 5), 'g11': (0, 6), 'h11': (1, 7), 'i11': (0, 0), 'k11': (0, 0), 'l11': (0, 0),
                      }
        board_dict_1 = {}
        hex_notation_1 = ['f1', 'e1', 'd1', 'c1', 'b1', 'a1']

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

    def define_nearest_hex(self, coords):
        difference_x = []
        difference_y = []
        print(coords)
        print(self.recorded_centers_of_hexagons.values())
        for key in self.recorded_centers_of_hexagons.values():
            difference_x.append(abs(key[0]- coords[0]))
            difference_y.append(abs(key[1]- coords[1]))
        minimal_dist_x = min(difference_x)
        minimal_dist_y = min(difference_y)
        exact_hex_x = coords[0]- minimal_dist_x
        exact_hex_y = coords[1]- minimal_dist_y
        print(minimal_dist_x, exact_hex_x)
        print(difference_x, difference_y)
        print(f'Ближайший шестиугольник: ({exact_hex_x}.{exact_hex_y})')
        #print(f'Координаты мышки:{coords[0]} . {coords[1]}'
        #    f'Ближайший шестиугольник: ', difference_x, minimal_dist_x, exact_hex)



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
                print(gamestate.recorded_centers_of_hexagons)
                column = location[0]
                row = location[1]
                offset = pygame.Surface.get_offset(screen)

                if sq_selected == (row, column): #если кликлун туда же
                    sq_selected = () #очистить выбор
                    moves = [] #очистить ходы
                else:
                    sq_selected = (row, column)
                    moves.append(sq_selected) #добавляем 1 и 2 клики
                gamestate.define_nearest_hex(location)
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
    draw_squares(screen, gamestate)
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

def draw_squares(screen, gamestate):
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
        hexagon_1 = Hexagons(450-(part_1*78), 945 - (part_1*45), 90)
        pygame.draw.polygon(screen, color, hexagon_1.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_1.points)
        gamestate.recorded_centers_of_hexagons.update({f'{part_1}hex':[(450-part_1*78), 945 - (part_1*45)]})
    for part_2 in range(7):
        color = colors[((part_2 + 1) % 3)]
        hexagon_2 = Hexagons(528 - (part_2 * 78), 900 - (part_2 * 45), 90)
        pygame.draw.polygon(screen, color, hexagon_2.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_2.points)
        gamestate.recorded_centers_of_hexagons.update({f'{part_2}hex': [(450 - part_2 * 78), 945 - (part_2 * 45)]})
    for part_3 in range(8):
        color = colors[((part_3 + 2) % 3)]
        hexagon_3 = Hexagons(606 - (part_3 * 78), 855 - (part_3 * 45), 90)
        pygame.draw.polygon(screen, color, hexagon_3.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_3.points)
        gamestate.recorded_centers_of_hexagons.update({f'{part_3}hex': [(450 - part_3 * 78), 945 - (part_3 * 45)]})
    for part_4 in range(9):
        color = colors[((part_4 + 3) % 3)]
        hexagon_4 = Hexagons(684 - (part_4 * 78), 810 - (part_4 * 45), 90)
        pygame.draw.polygon(screen, color, hexagon_4.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_4.points)
        gamestate.recorded_centers_of_hexagons.update({f'{part_4}hex': [(450 - part_4 * 78), 945 - (part_4 * 45)]})
    for part_5 in range(10):
        color = colors[((part_5 + 4) % 3)]
        hexagon_5 = Hexagons(762 - (part_5 * 78), 765 - (part_5 * 45), 90)
        pygame.draw.polygon(screen, color, hexagon_5.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_5.points)
        gamestate.recorded_centers_of_hexagons.update({f'{part_5}hex': [(450 - part_5 * 78), 945 - (part_5 * 45)]})
    for part_6 in range(11):
        color = colors[((part_6 + 5) % 3)]
        hexagon_6 = Hexagons(840 - (part_6 * 78), 720 - (part_6 * 45), 90)
        pygame.draw.polygon(screen, color, hexagon_6.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_6.points)
    for part_7 in range(10):
        color = colors[((part_7 + 7) % 3)]
        hexagon_7 = Hexagons(840 - (part_7 * 78), 630 - (part_7 * 45), 90)
        pygame.draw.polygon(screen, color, hexagon_7.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_7.points)
    for part_8 in range(9):
        color = colors[((part_8) % 3)]
        hexagon_8 = Hexagons(840 - (part_8 * 78), 540 - (part_8 * 45), 90)
        pygame.draw.polygon(screen, color, hexagon_8.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_8.points)
    for part_9 in range(8):
        color = colors[((part_9 + 2) % 3)]
        hexagon_9 = Hexagons(840 - (part_9 * 78), 450 - (part_9 * 45), 90)
        pygame.draw.polygon(screen, color, hexagon_9.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_9.points)
    for part_10 in range(7):
        color = colors[((part_10 + 1) % 3)]
        hexagon_10 = Hexagons(840 - (part_10 * 78), 360 - (part_10 * 45), 90)
        pygame.draw.polygon(screen, color, hexagon_10.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_10.points)
    for part_11 in range(6):
        color = colors[((part_11) % 3)]
        hexagon_11 = Hexagons(840 - (part_11 * 78), 270 - (part_11 * 45), 90)
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