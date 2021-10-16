import pygame
import numpy as np
import os

height = 990
width = 900
fps = 30
images = {}


def loadimage():
    figures = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for role in figures:
        images[role] = pygame.transform.scale(pygame.image.load('images_cardinal/' + role + '.svg'), (360, 360))


# [[row, column]]
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
        self.board_dict = {'a1': [60, 720], 'b1': [138, 765], 'c1': [216, 810], 'd1': [294, 855], 'e1': [372, 900],
                           'f1': [450, 945], 'g1': [528, 900], 'h1': [606, 855], 'i1': [684, 810], 'k1': [762, 765],
                           'l1': [840, 720],
                           'a2': [60, 630], 'b2': [138, 675], 'c2': [216, 720], 'd2': [294, 765], 'e2': [372, 810],
                           'f2': [450, 855], 'g2': [528, 810], 'h2': [606, 765], 'i2': [684, 720], 'k2': [762, 675],
                           'l2': [840, 630],
                           'a3': [60, 540], 'b3': [138, 585], 'c3': [216, 630], 'd3': [294, 675], 'e3': [372, 720],
                           'f3': [450, 765], 'g3': [528, 720], 'h3': [606, 675], 'i3': [684, 630], 'k3': [762, 585],
                           'l3': [840, 540],
                           'a4': [60, 450], 'b4': [138, 495], 'c4': [216, 540], 'd4': [294, 585], 'e4': [372, 630],
                           'f4': [450, 675], 'g4': [528, 630], 'h4': [606, 585], 'i4': [684, 540], 'k4': [762, 495],
                           'l4': [840, 450],
                           'a5': [60, 360], 'b5': [138, 405], 'c5': [216, 450], 'd5': [294, 495], 'e5': [372, 540],
                           'f5': [450, 585], 'g5': [528, 540], 'h5': [606, 495], 'i5': [684, 450], 'k5': [762, 405],
                           'l5': [840, 360],
                           'a6': [60, 270], 'b6': [138, 315], 'c6': [216, 360], 'd6': [294, 405], 'e6': [372, 450],
                           'f6': [450, 495], 'g6': [528, 450], 'h6': [606, 405], 'i6': [684, 360], 'k6': [762, 315],
                           'l6': [840, 270],
                           'b7': [138, 225], 'c7': [216, 270], 'd7': [294, 315], 'e7': [372, 360], 'f7': [450, 405],
                           'g7': [528, 360], 'h7': [606, 315], 'i7': [684, 270], 'k7': [762, 225],
                           'c8': [216, 180], 'd8': [294, 225], 'e8': [372, 270], 'f8': [450, 315], 'g8': [528, 270],
                           'h8': [606, 225], 'i8': [684, 180],
                           'd9': [294, 135], 'e9': [372, 180], 'f9': [450, 225], 'g9': [528, 180], 'h9': [606, 135],
                           'e10': [372, 90], 'f10': [450, 135], 'g10': [528, 90],
                           'f11': [450, 45],
                           }
        self.convert_dict = {(0, 0, 5): 'a1', (0, 1, 6): 'a2', (0, 2, 7): 'a3', (0, 3, 8): 'a4', (0, 4, 9): 'a5',
                             (0, 5, 10): 'a6',
                             (1, 0, 4): 'b1', (1, 1, 5): 'b2', (1, 2, 6): 'b3', (1, 3, 7): 'b4', (1, 4, 8): 'b5',
                             (1, 5, 9): 'b6', (1, 6, 10): 'b7',
                             (2, 0, 3): 'c1', (2, 1, 4): 'c2', (2, 2, 5): 'c3', (2, 3, 6): 'c4', (2, 4, 7): 'c5',
                             (2, 5, 8): 'c6', (2, 6, 9): 'c7', (2, 7, 10): 'c8',
                             (3, 0, 2): 'd1', (3, 1, 3): 'd2', (3, 2, 4): 'd3', (3, 3, 5): 'd4', (3, 4, 6): 'd5',
                             (3, 5, 7): 'd6', (3, 6, 8): 'd7', (3, 7, 9): 'd8', (3, 8, 10): 'd9',
                             (4, 0, 1): 'e1', (4, 1, 2): 'e2', (4, 2, 3): 'e3', (4, 3, 4): 'e4', (4, 4, 5): 'e5',
                             (4, 5, 6): 'e6', (4, 6, 7): 'e7', (4, 7, 8): 'e8', (4, 8, 9): 'e9', (4, 9, 10): 'e10',
                             (5, 0, 0): 'f1', (5, 1, 1): 'f1', (5, 2, 2): 'f3', (5, 3, 3): 'f4', (5, 4, 4): 'f5',
                             (5, 5, 5): 'f6', (5, 6, 6): 'f7', (5, 7, 7): 'f8', (5, 8, 8): 'f9', (5, 9, 9): 'f10',
                             (5, 10, 10): 'f11',
                             (6, 1, 0): 'g1', (6, 2, 1): 'g2', (6, 3, 2): 'g3', (6, 4, 3): 'g4', (6, 5, 4): 'g5',
                             (6, 6, 5): 'g6', (6, 7, 6): 'g7', (6, 8, 7): 'g8', (6, 9, 8): 'g9', (6, 10, 9): 'g10',
                             (7, 2, 0): 'h1', (7, 3, 1): 'h2', (7, 4, 2): 'h3', (7, 5, 3): 'h4', (7, 6, 4): 'h5',
                             (7, 7, 5): 'h6', (7, 8, 6): 'h7', (7, 9, 7): 'h8', (7, 10, 8): 'h9',
                             (8, 3, 0): 'i1', (8, 4, 1): 'i2', (8, 5, 2): 'i3', (8, 6, 3): 'i4', (8, 7, 4): 'i5',
                             (8, 8, 5): 'i6', (8, 9, 6): 'i7', (8, 10, 7): 'i8',
                             (9, 4, 0): 'k1', (9, 5, 1): 'k2', (9, 6, 2): 'k3', (9, 7, 3): 'k4', (9, 8, 4): 'k5',
                             (9, 9, 5): 'k6', (9, 10, 6): 'k7',
                             (10, 5, 0): 'l1', (10, 6, 1): 'l2', (10, 7, 2): 'l3', (10, 8, 3): 'l4', (10, 9, 4): 'l5',
                             (10, 10, 5): 'l6'}
        self.board = [hex_1, hex_2, hex_3, hex_4, hex_5, hex_6, hex_7, hex_8, hex_9, hex_10, hex_11]
        self.move_log_by_notation = []
        self.chess = []
        self.recorded_centers_of_hexagons = {}
        # self.chess_table = chess.Board()
        self.whiteToMove = True
        self.notation_to_board_dict_1 = {}
        self.notation_to_board_dict_2 = {}
        self.notation_to_board_dict_3 = {}
        self.notation_to_board_dict_4 = {}
        self.notation_to_board_dict_5 = {}
        self.notation_to_board_dict_6 = {}
        self.notation_to_board_dict_7 = {}
        self.notation_to_board_dict_8 = {}
        self.notation_to_board_dict_9 = {}
        self.notation_to_board_dict_10 = {}
        self.notation_to_board_dict_11 = {}
        self.board_move_log = []  # записанные ходы(строка, столбец) для изменения матрицы доски
        self.board_full_log = []  # полная история ходов
        self.converted_move = []
        self.notated_move = []
        self.piece_possible_moves = []
        self.board_move_log_attributes = []
        self.all_piece_moved = []

    def make_move(self, start, end):
        # board = chess.Board()
        # print(board, start, end)
        # uci_move_1 = chess.Move.from_uci(self.notation(start, end))
        # print(self.converted_move)

        try:
            if move.magic(self.converted_move[0], self.converted_move[1]) == 'ALL RIGHT':
                self.move_log_by_notation.append(self.notation(start, end))
                self.whiteToMove = not self.whiteToMove
                start_row = start[1]
                start_column = start[0]
                end_row = end[1]
                end_column = end[0]
                self.piece_captured = self.board[end_column][end_row]
                self.piece_moved = self.board[start_column][start_row]
                self.board[start_column][start_row] = '--'
                self.board[end_column][end_row] = self.piece_moved
                self.all_piece_moved.append([self.piece_moved, self.piece_captured])
                self.board_move_log_attributes.append([move.bord, move.ippl])
            else:
                print(move.magic(self.converted_move[0], self.converted_move[1]))
        except IndexError:
            print('БАГ')

    def undo_move(self):
        try:
            if self.board_full_log != 0:
                # print(self.board_full_log)
                end = self.board_full_log.pop()  # получение последнего хода
                start = self.board_full_log.pop()  # получение предпосл хода
                # print(move, 'move', move_1, 'move1')
                recovermove = self.board_move_log_attributes.pop()
                side_color = self.all_piece_moved.pop()

                move.bord = recovermove[0]
                move.ippl = recovermove[1]

                self.board[start[0]][start[1]] = side_color[0]
                self.board[end[0]][end[1]] = side_color[1]

                self.whiteToMove = not self.whiteToMove
        except IndexError:
            print('Дальше возвращаться нельзя, ходов нету')

    def notation_to_board(self, nearest_loc):
        all_notation_dicts = [[self.notation_to_board_dict_1], [self.notation_to_board_dict_2],
                              [self.notation_to_board_dict_3],
                              [self.notation_to_board_dict_4], [self.notation_to_board_dict_5],
                              [self.notation_to_board_dict_6],
                              [self.notation_to_board_dict_7], [self.notation_to_board_dict_8],
                              [self.notation_to_board_dict_9],
                              [self.notation_to_board_dict_10], [self.notation_to_board_dict_11]]
        '''проходимся по всем эл-м массива со словарями 11-линий отрисовки поля (ключ=строка, значение=столбец)
        строка и столбец после хода 2-ух игроков попадает в функцию self.make_move и изменяет матрицу поля self.board
        с заменой эл-ов массива () . Фигуры рисуются по значениям в матрице поле и любые изменения в массиве поменяют само
        поле.           
        '''
        # print(all_notation_dicts)
        i = 0
        column = 0
        row = 0
        for key in all_notation_dicts[0:11]:
            if nearest_loc in key[0].values():  # узнаем в каком массиве из матрицы ближ шестиугольник к клику (номер столбца)
                column += i
                for key, value in key[0].items():  # узнаем ключ эл-ма по значению, ключ в этом случае - номер по списку (номер строки)
                    if value == nearest_loc:
                        row += key
            i += 1

        # print(f"column: {column},row: {row}")
        self.board_move_log.append([column, row])
        self.board_full_log.append([column, row])

    def notation(self, start, end):
        move_start = ''
        move_end = ''
        for key, value in self.board_dict.items():
            if value == start:
                move_start += key
            elif value == end:
                move_end += key
        move = move_start + move_end

        return move

    def notation_2(self, move):  # нотация каждого хода в формате a-l1-11
        move_s = ''
        for key, value in self.board_dict.items():
            if value == move:
                move_s += key
        self.notated_move.append(move_s)

    def is_check(self):
        pass

    def get_nearest_value(self, n_value, n_list):  # получение ближайшего значения к n_value из списка n_list
        list_of_diffs = [abs(n_value - x) for x in n_list]
        result_index = list_of_diffs.index(min(list_of_diffs))
        return n_list[result_index]

    def define_nearest_hex(self, coords):  # получение координат ближайшего шестиугольника от клика мышки
        x_coords = []  # x_координаты центров всех шестиугольников
        y_coords = []  # y_координаты центров всех шестиугольников
        for each in self.recorded_centers_of_hexagons.values():
            x_coords.append(each[0])
            y_coords.append(each[1])
        x_nearest = self.get_nearest_value(coords[0], x_coords)
        y_nearest = self.get_nearest_value(coords[1], y_coords)
        hexogonal_selected = [x_nearest, y_nearest]
        return hexogonal_selected

    def convert_notation_to_coords(self, move):
        for key, value in self.convert_dict.items():
            if value == move:
                self.converted_move.append(key)

    def hex_backlight(self, move):
        self.piece_possible_moves = move.checkmv(move.bord.get(self.converted_move[0]), move.bord)[0]
        move_s = ''
        for key, value in self.board_dict.items():
            if value == move:
                move_s += key


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
    sq_selected = ()  # выбранная область по абсолютным координатам 900*990
    moves = []  # - координаты хода в виде ближ шестиугольника к клику мышки

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()  # (x,y)
                # print(gamestate.recorded_centers_of_hexagons)
                column = location[0]
                row = location[1]
                offset = pygame.Surface.get_offset(screen)

                if sq_selected == (row, column):  # если кликлун туда же
                    sq_selected = ()  # очистить выбор
                    moves = []  # очистить ходы
                else:
                    sq_selected = (column, row)
                    moves.append(gamestate.define_nearest_hex(
                        location))  # добавляем 1 и 2 координаты шестиугольника, ближайшего к курсору мыши
                    # gamestate.moves_by_nearest_hex = []
                    # gamestate.moves_by_nearest_hex.append(gamestate.define_nearest_hex(location))
                    gamestate.notation_to_board(gamestate.define_nearest_hex(location))
                    # print(gamestate.board_move_log)
                    gamestate.notation_2(gamestate.define_nearest_hex(location))
                    # gamestate.convert_notation_to_coords(gamestate.notated_move[0])
                    # print(gamestate.notation_2(gamestate.define_nearest_hex(location)))
                # print(sq_selected, moves)
                # print(gamestate.notation_to_board_dict)
                if len(moves) == 1:
                    print(gamestate.notated_move[0])
                    gamestate.convert_notation_to_coords(gamestate.notated_move[0])

                if len(moves) == 2:  # после полного хода
                    start = moves[0]
                    # print(f'{start[0]} s')
                    end = moves[1]
                    print(
                        f'Ход стороны {"Белые" if gamestate.whiteToMove else "Чёрные"} : {gamestate.notation(moves[0], moves[1])}')
                    gamestate.convert_notation_to_coords(gamestate.notated_move[1])
                    gamestate.make_move(gamestate.board_move_log[0], gamestate.board_move_log[1])
                    sq_selected = ()
                    moves = []
                    # print(gamestate.converted_move, 'converted')
                    gamestate.board_move_log = []
                    gamestate.converted_move = []
                    gamestate.notated_move = []
            elif event.type == pygame.KEYDOWN:
                gamestate.undo_move()

        draw_game(screen, gamestate)
        clock.tick(fps)
        pygame.display.flip()


def draw_game(screen, gamestate):
    draw_squares(screen, gamestate)


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
    colors = [pygame.Color('beige'), pygame.Color(255, 136, 0), pygame.Color('red')]
    for part_1 in range(6):
        color = colors[((part_1) % 3)]
        hexagon_1 = Hexagons(450 - (part_1 * 78), 945 - (part_1 * 45), 90)  # 90-размер
        pygame.draw.polygon(screen, color, hexagon_1.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_1.points)
        gamestate.recorded_centers_of_hexagons.update(
            {f'{part_1 + 1}hex': [(450 - (part_1 * 78)), 945 - (part_1 * 45)]})
        gamestate.notation_to_board_dict_1.update({part_1: gamestate.define_nearest_hex([hexagon_1.xc, hexagon_1.yc])})
        piece = gamestate.board[0][part_1]
        if piece != '--':
            screen.blit(images[piece], pygame.Rect((gamestate.recorded_centers_of_hexagons[f'{part_1 + 1}hex'][0] - 42,
                                                    gamestate.recorded_centers_of_hexagons[f'{part_1 + 1}hex'][1] - 47,
                                                    0, 0)))
    for part_2 in range(7):
        color = colors[((part_2 + 1) % 3)]
        hexagon_2 = Hexagons(528 - (part_2 * 78), 900 - (part_2 * 45), 90)
        pygame.draw.polygon(screen, color, hexagon_2.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_2.points)
        gamestate.recorded_centers_of_hexagons.update(
            {f'{part_2 + 7}hex': [(528 - (part_2 * 78)), 900 - (part_2 * 45)]})
        gamestate.notation_to_board_dict_2.update({part_2: gamestate.define_nearest_hex([hexagon_2.xc, hexagon_2.yc])})
        piece = gamestate.board[1][part_2]
        if piece != '--':
            screen.blit(images[piece], pygame.Rect((gamestate.recorded_centers_of_hexagons[f'{part_2 + 7}hex'][0] - 42,
                                                    gamestate.recorded_centers_of_hexagons[f'{part_2 + 7}hex'][1] - 47,
                                                    0, 0)))

    for part_3 in range(8):
        color = colors[((part_3 + 2) % 3)]
        hexagon_3 = Hexagons(606 - (part_3 * 78), 855 - (part_3 * 45), 90)
        pygame.draw.polygon(screen, color, hexagon_3.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_3.points)
        gamestate.recorded_centers_of_hexagons.update(
            {f'{part_3 + 14}hex': [(606 - (part_3 * 78)), 855 - (part_3 * 45)]})
        gamestate.notation_to_board_dict_3.update({part_3: gamestate.define_nearest_hex([hexagon_3.xc, hexagon_3.yc])})
        piece = gamestate.board[2][part_3]
        if piece != '--':
            screen.blit(images[piece], pygame.Rect((gamestate.recorded_centers_of_hexagons[f'{part_3 + 14}hex'][0] - 42,
                                                    gamestate.recorded_centers_of_hexagons[f'{part_3 + 14}hex'][1] - 47,
                                                    0, 0)))
    for part_4 in range(9):
        color = colors[((part_4 + 3) % 3)]
        hexagon_4 = Hexagons(684 - (part_4 * 78), 810 - (part_4 * 45), 90)
        pygame.draw.polygon(screen, color, hexagon_4.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_4.points)
        gamestate.recorded_centers_of_hexagons.update({f'{part_4 + 22}hex': [(684 - part_4 * 78), 810 - (part_4 * 45)]})
        gamestate.notation_to_board_dict_4.update({part_4: gamestate.define_nearest_hex([hexagon_4.xc, hexagon_4.yc])})
        piece = gamestate.board[3][part_4]
        if piece != '--':
            screen.blit(images[piece], pygame.Rect((gamestate.recorded_centers_of_hexagons[f'{part_4 + 22}hex'][0] - 42,
                                                    gamestate.recorded_centers_of_hexagons[f'{part_4 + 22}hex'][1] - 42,
                                                    0, 0)))
    for part_5 in range(10):
        color = colors[((part_5 + 4) % 3)]
        hexagon_5 = Hexagons(762 - (part_5 * 78), 765 - (part_5 * 45), 90)
        pygame.draw.polygon(screen, color, hexagon_5.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_5.points)
        gamestate.recorded_centers_of_hexagons.update({f'{part_5 + 31}hex': [(762 - part_5 * 78), 765 - (part_5 * 45)]})
        gamestate.notation_to_board_dict_5.update({part_5: gamestate.define_nearest_hex([hexagon_5.xc, hexagon_5.yc])})
        piece = gamestate.board[4][part_5]
        if piece != '--':
            screen.blit(images[piece], pygame.Rect((gamestate.recorded_centers_of_hexagons[f'{part_5 + 31}hex'][0] - 42,
                                                    gamestate.recorded_centers_of_hexagons[f'{part_5 + 31}hex'][1] - 42,
                                                    0, 0)))
    for part_6 in range(11):
        color = colors[((part_6 + 5) % 3)]
        hexagon_6 = Hexagons(840 - (part_6 * 78), 720 - (part_6 * 45), 90)
        pygame.draw.polygon(screen, color, hexagon_6.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_6.points)
        gamestate.recorded_centers_of_hexagons.update({f'{part_6 + 41}hex': [(840 - part_6 * 78), 720 - (part_6 * 45)]})
        gamestate.notation_to_board_dict_6.update({part_6: gamestate.define_nearest_hex([hexagon_6.xc, hexagon_6.yc])})
        piece = gamestate.board[5][part_6]
        if piece != '--':
            screen.blit(images[piece], pygame.Rect((gamestate.recorded_centers_of_hexagons[f'{part_6 + 41}hex'][0] - 42,
                                                    gamestate.recorded_centers_of_hexagons[f'{part_6 + 41}hex'][1] - 42,
                                                    0, 0)))
    for part_7 in range(10):
        color = colors[((part_7 + 7) % 3)]
        hexagon_7 = Hexagons(840 - (part_7 * 78), 630 - (part_7 * 45), 90)
        pygame.draw.polygon(screen, color, hexagon_7.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_7.points)
        gamestate.recorded_centers_of_hexagons.update({f'{part_7 + 52}hex': [(840 - part_7 * 78), 630 - (part_7 * 45)]})
        gamestate.notation_to_board_dict_7.update({part_7: gamestate.define_nearest_hex([hexagon_7.xc, hexagon_7.yc])})
        piece = gamestate.board[6][part_7]
        if piece != '--':
            screen.blit(images[piece], pygame.Rect((gamestate.recorded_centers_of_hexagons[f'{part_7 + 52}hex'][0] - 42,
                                                    gamestate.recorded_centers_of_hexagons[f'{part_7 + 52}hex'][1] - 42,
                                                    0, 0)))
    for part_8 in range(9):
        color = colors[((part_8) % 3)]
        hexagon_8 = Hexagons(840 - (part_8 * 78), 540 - (part_8 * 45), 90)
        pygame.draw.polygon(screen, color, hexagon_8.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_8.points)
        gamestate.recorded_centers_of_hexagons.update({f'{part_8 + 62}hex': [(840 - part_8 * 78), 540 - (part_8 * 45)]})
        gamestate.notation_to_board_dict_8.update({part_8: gamestate.define_nearest_hex([hexagon_8.xc, hexagon_8.yc])})
        piece = gamestate.board[7][part_8]
        if piece != '--':
            screen.blit(images[piece], pygame.Rect((gamestate.recorded_centers_of_hexagons[f'{part_8 + 62}hex'][0] - 42,
                                                    gamestate.recorded_centers_of_hexagons[f'{part_8 + 62}hex'][1] - 42,
                                                    0, 0)))
    for part_9 in range(8):
        color = colors[((part_9 + 2) % 3)]
        hexagon_9 = Hexagons(840 - (part_9 * 78), 450 - (part_9 * 45), 90)
        pygame.draw.polygon(screen, color, hexagon_9.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_9.points)
        gamestate.recorded_centers_of_hexagons.update({f'{part_9 + 71}hex': [(840 - part_9 * 78), 450 - (part_9 * 45)]})
        gamestate.notation_to_board_dict_9.update({part_9: gamestate.define_nearest_hex([hexagon_9.xc, hexagon_9.yc])})
        piece = gamestate.board[8][part_9]
        if piece != '--':
            screen.blit(images[piece], pygame.Rect((gamestate.recorded_centers_of_hexagons[f'{part_9 + 71}hex'][0] - 42,
                                                    gamestate.recorded_centers_of_hexagons[f'{part_9 + 71}hex'][1] - 42,
                                                    0, 0)))
    for part_10 in range(7):
        color = colors[((part_10 + 1) % 3)]
        hexagon_10 = Hexagons(840 - (part_10 * 78), 360 - (part_10 * 45), 90)
        pygame.draw.polygon(screen, color, hexagon_10.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_10.points)
        gamestate.recorded_centers_of_hexagons.update(
            {f'{part_10 + 79}hex': [(840 - part_10 * 78), 360 - (part_10 * 45)]})
        gamestate.notation_to_board_dict_10.update(
            {part_10: gamestate.define_nearest_hex([hexagon_10.xc, hexagon_10.yc])})
        piece = gamestate.board[9][part_10]
        if piece != '--':
            screen.blit(images[piece],
                        pygame.Rect((gamestate.recorded_centers_of_hexagons[f'{part_10 + 79}hex'][0] - 42,
                                     gamestate.recorded_centers_of_hexagons[f'{part_10 + 79}hex'][1] - 42,
                                     0, 0)))
    for part_11 in range(6):
        color = colors[((part_11) % 3)]
        hexagon_11 = Hexagons(840 - (part_11 * 78), 270 - (part_11 * 45), 90)
        pygame.draw.polygon(screen, color, hexagon_11.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_11.points)
        gamestate.recorded_centers_of_hexagons.update(
            {f'{part_11 + 86}hex': [(840 - part_11 * 78), 270 - (part_11 * 45)]})
        gamestate.notation_to_board_dict_11.update(
            {part_11: gamestate.define_nearest_hex([hexagon_11.xc, hexagon_11.yc])})
        piece = gamestate.board[10][part_11]
        if piece != '--':
            screen.blit(images[piece],
                        pygame.Rect((gamestate.recorded_centers_of_hexagons[f'{part_11 + 86}hex'][0] - 42,
                                     gamestate.recorded_centers_of_hexagons[f'{part_11 + 86}hex'][1] - 42,
                                     0, 0)))


class K:
    taypmv = "PD"
    lim = 1


class p:
    taypmv = 'p'
    f1 = 1
    lim = 10


class Q:
    taypmv = 'PD'
    lim = 10


class L:
    taypmv = 'P'
    lim = 10


class B:
    taypmv = "D"
    lim = 10


class H:
    taypmv = 'H'
    lim = 10


Kw = K()
Kw.pos = (6, 1, 0)
Kw.name = 'K1w'
Kb = K()
Kb.pos = (6, 10, 9)
Kb.name = "K1b"

Q1w = Q()
Q1w.name = 'Q1w'
Q1w.pos = (4, 0, 1)
Q1b = Q()
Q1b.name = 'Q1b'
Q1b.pos = (4, 9, 10)

b1w = B();
b1w.name = "b1w"
b1w.pos = (5, 0, 0)
b2w = B()
b2w.name = "b2w"
b2w.pos = (5, 1, 1)
b3w = B();
b3w.name = "b3w"
b3w.pos = (5, 2, 2)

b1b = B();
b1b.name = "b1b"
b1b.pos = (5, 10, 10)
b2b = B()
b2b.name = "b2b"
b2b.pos = (5, 9, 9)
b3b = B()
b3b.name = "b3b"
b3b.pos = (5, 8, 8)

l1w = L()
l1w.name = 'l1w'
l1w.pos = (8, 3, 0)
l2w = L()
l2w.name = 'l2w'
l2w.pos = (2, 0, 3)

l1b = L()
l1b.name = 'l1b'
l1b.pos = (8, 10, 7)
l2b = L()
l2b.name = 'l2b'
l2b.pos = (2, 7, 10)

h1w = H()
h1w.name = "h1w"
h1w.pos = (7, 2, 0)
h2w = H()
h2w.name = "h2w"
h2w.pos = (3, 0, 2)

h1b = H()
h1b.name = "h1b"
h1b.pos = (7, 10, 8)
h2b = H()
h2b.name = "h2b"
h2b.pos = (3, 8, 10)

p1w = p()
p1w.name = "p1w"
p1w.pos = (1, 0, 4)
p2w = p()
p2w.name = "p2w"
p2w.pos = (2, 1, 4)
p3w = p()
p3w.name = "p3w"
p3w.pos = (3, 2, 4)
p4w = p()
p4w.name = "p4w"
p4w.pos = (4, 3, 4)
p5w = p()
p5w.name = "p5w"
p5w.pos = (5, 4, 4)
p6w = p()
p6w.name = "p6w"
p6w.pos = (6, 4, 3)
p7w = p()
p7w.name = "p7w"
p7w.pos = (7, 4, 2)
p8w = p()
p8w.name = "p8w"
p8w.pos = (8, 4, 1)
p9w = p()
p9w.name = "p9w"
p9w.pos = (9, 4, 0)

p1b = p()
p1b.name = "p1b"
p1b.pos = (1, 6, 10)
p2b = p()
p2b.name = "p2b"
p2b.pos = (2, 6, 9)
p3b = p()
p3b.name = "p3b"
p3b.pos = (3, 6, 8)
p4b = p()
p4b.name = "p4b"
p4b.pos = (4, 6, 7)
p5b = p()
p5b.name = "p5b"
p5b.pos = (5, 6, 6)
p6b = p()
p6b.name = "p6b"
p6b.pos = (6, 7, 6)
p7b = p()
p7b.name = "p7b"
p7b.pos = (7, 8, 6)
p8b = p()
p8b.name = "p8b"
p8b.pos = (8, 9, 6)
p9b = p()
p9b.name = "p9b"
p9b.pos = (9, 10, 6)
chmanpos = [p1b, p2b, p3b, p4b, p5b, p6b, p7b, p8b, p9b, p1w, p2w, p3w, p4w, p5w, p6w, p7w, p8w, p9w, b1w, b2w, b3w,
            b1b, b2b, b3b,
            l1w, l2w, l1b, l2b, h1w, h1b, h2w, h2b, Q1w, Q1b, Kw, Kb]


class move:
    bord = {(0, 0, 5): '-', (0, 1, 6): '-', (0, 2, 7): '-', (0, 3, 8): '-', (0, 4, 9): '-', (0, 5, 10): '-',
            (1, 0, 4): '-', (1, 1, 5): '-', (1, 2, 6): '-', (1, 3, 7): '-', (1, 4, 8): '-', (1, 5, 9): '-',
            (1, 6, 10): '-',
            (2, 0, 3): '-', (2, 1, 4): '-', (2, 2, 5): '-', (2, 3, 6): '-', (2, 4, 7): '-', (2, 5, 8): '-',
            (2, 6, 9): '-', (2, 7, 10): '-',
            (3, 0, 2): '-', (3, 1, 3): '-', (3, 2, 4): '-', (3, 3, 5): '-', (3, 4, 6): '-', (3, 5, 7): '-',
            (3, 6, 8): '-', (3, 7, 9): '-', (3, 8, 10): '-',
            (4, 0, 1): '-', (4, 1, 2): '-', (4, 2, 3): '-', (4, 3, 4): '-', (4, 4, 5): '-', (4, 5, 6): '-',
            (4, 6, 7): '-', (4, 7, 8): '-', (4, 8, 9): '-', (4, 9, 10): '-',
            (5, 0, 0): '-', (5, 1, 1): '-', (5, 2, 2): '-', (5, 3, 3): '-', (5, 4, 4): '-', (5, 5, 5): '-',
            (5, 6, 6): '-', (5, 7, 7): '-', (5, 8, 8): '-', (5, 9, 9): '-', (5, 10, 10): '-',
            (6, 1, 0): '-', (6, 2, 1): '-', (6, 3, 2): '-', (6, 4, 3): '-', (6, 5, 4): '-', (6, 6, 5): '-',
            (6, 7, 6): '-', (6, 8, 7): '-', (6, 9, 8): '-', (6, 10, 9): '-',
            (7, 2, 0): '-', (7, 3, 1): '-', (7, 4, 2): '-', (7, 5, 3): '-', (7, 6, 4): '-', (7, 7, 5): '-',
            (7, 8, 6): '-', (7, 9, 7): '-', (7, 10, 8): '-',
            (8, 3, 0): '-', (8, 4, 1): '-', (8, 5, 2): '-', (8, 6, 3): '-', (8, 7, 4): '-', (8, 8, 5): '-',
            (8, 9, 6): '-', (8, 10, 7): '-',
            (9, 4, 0): '-', (9, 5, 1): '-', (9, 6, 2): '-', (9, 7, 3): '-', (9, 8, 4): '-', (9, 9, 5): '-',
            (9, 10, 6): '-',
            (10, 5, 0): '-', (10, 6, 1): '-', (10, 7, 2): '-', (10, 8, 3): '-', (10, 9, 4): '-', (10, 10, 5): '-'}
    ippl = "w"

    def __init__(self):
        self.chmanpos = chmanpos
        self.check = 0
        for i in range(-5, 6):
            for j in range(11 - abs(i)):
                if i < 0:
                    for k in range(len(chmanpos)):
                        if self.bord.get((5 + i, j, abs(i) + j)) == "-" and chmanpos[k].pos == (5 + i, j, abs(i) + j):
                            self.bord[(5 + i, j, abs(i) + j)] = chmanpos[k]
                else:
                    for k in range(len(chmanpos)):
                        if self.bord.get((5 + i, i + j, j)) == "-" and chmanpos[k].pos == ((5 + i, i + j, j)):
                            self.bord[(5 + i, i + j, j)] = chmanpos[k]

    def chekpos(self, p, bord):
        if bord.get(p) == '-':
            self.psm.append(p)
            return 1
        elif bord.get((p[0], p[1], p[2])) == None:
            return 0
        elif bord.get((p[0], p[1], p[2])).name == 'K1b' and self.ippl == "w":
            self.check = "b"
        elif bord.get((p[0], p[1], p[2])).name == 'K1w' and self.ippl == "b":
            self.check = "w"
            return 0
        elif bord.get((p[0], p[1], p[2])).name[2] != self.chman.name[2]:
            self.psm.append((p[0], p[1], p[2]))
            self.eda.append((p[0], p[1], p[2]))
            return 0
        elif bord.get((p[0], p[1], p[2])).name[2] == self.chman.name[2]:
            return 0
        else:
            return 0

    def checkmv(self, chman, bord):
        self.chman = chman
        p = list(chman.pos)
        taypmv = chman.taypmv
        lim = chman.lim
        self.psm = list()
        self.eda = list()
        check = 0
        # P - Движение по прямой
        # D - По диагонали
        # PD - Королева король
        # H - Коннь
        # p - Пешка
        if taypmv == "P" or taypmv == 'PD':
            # Поперек Left справа налево
            for i in range(1, lim + 1):
                if self.chekpos((p[0] + i, p[1] + i, p[2]), bord) == 1:
                    pass
                else:
                    break
            # Поперек Left слева направо
            for i in range(1, lim + 1):
                if self.chekpos((p[0] - i, p[1] - i, p[2]), bord) == 1:
                    pass
                else:
                    break
            # Поперек right справа налево
            for i in range(1, lim + 1):
                if self.chekpos((p[0] + i, p[1], p[2] - i), bord) == 1:
                    pass
                else:
                    break
            # Поперек right слева направо
            for i in range(1, lim + 1):
                if self.chekpos((p[0] - i, p[1], p[2] + i), bord) == 1:
                    pass
                else:
                    break
            # По x вверх
            for i in range(1, lim + 1):
                if self.chekpos((p[0], p[1] + i, p[2] + i), bord) == 1:
                    pass
                else:
                    break
            # По x вниз
            for i in range(1, lim + 1):
                if self.chekpos((p[0], p[1] - i, p[2] - i), bord) == 1:
                    pass
                else:
                    break
        if taypmv == "D" or taypmv == "PD":
            # Вправо вверх
            for i in range(1, lim + 1):
                if self.chekpos((p[0] + i, p[1] + 2 * i, p[2] + i), bord) == 1:
                    pass
                else:
                    break
            # Вправо вниз
            for i in range(1, lim + 1):
                if self.chekpos((p[0] + i, p[1] - i, p[2] - i * 2), bord) == 1:
                    pass
                else:
                    break
            # Влево вверх
            for i in range(1, lim + 1):
                if self.chekpos((p[0] - i, p[1] + i, p[2] + i * 2), bord) == 1:
                    pass
                else:
                    break
            # Влево вниз
            for i in range(1, lim + 1):
                if self.chekpos((p[0] - i, p[1] - i * 2, p[2] - i), bord) == 1:
                    pass
                else:
                    break
            # Вправо
            for i in range(1, lim + 1):
                if self.chekpos((p[0] + i * 2, p[1] + i, p[2] - i), bord) == 1:
                    pass
                else:
                    break
            # Влево
            for i in range(1, lim + 1):
                if self.chekpos((p[0] - i * 2, p[1] - i, p[2] + i), bord) == 1:
                    pass
                else:
                    break
        if taypmv == "H":
            self.chekpos((p[0] + 1, p[1] - 2, p[2] - 3), bord)
            self.chekpos((p[0] + 2, p[1] - 1, p[2] - 3), bord)
            self.chekpos((p[0] - 2, p[1] - 3, p[2] - 1), bord)
            self.chekpos((p[0] - 1, p[1] - 3, p[2] - 2), bord)
            self.chekpos((p[0] - 3, p[1] - 1, p[2] + 2), bord)
            self.chekpos((p[0] - 3, p[1] - 2, p[2] + 1), bord)
            self.chekpos((p[0] - 2, p[1] + 1, p[2] + 3), bord)
            self.chekpos((p[0] - 1, p[1] + 2, p[2] + 3), bord)
            self.chekpos((p[0] + 1, p[1] + 3, p[2] + 2), bord)
            self.chekpos((p[0] + 2, p[1] + 3, p[2] + 1), bord)
            self.chekpos((p[0] + 3, p[1] + 2, p[2] - 1), bord)
            self.chekpos((p[0] + 3, p[1] - 1, p[2] - 2), bord)
        if taypmv == "p":
            if chman.name[2] == "w":
                if self.bord.get((p[0], p[1] + 1, p[2] + 1)) == '-':
                    self.psm.append((p[0], p[1] + 1, p[2] + 1))
                    if chman.f1 == 1 and self.bord.get((p[0], p[1] + 2, p[2] + 2)) == '-':
                        self.psm.append((p[0], p[1] + 2, p[2] + 2))
                if self.bord.get((p[0] - 1, p[1], p[2] + 1)) != None:
                    if self.bord.get((p[0] - 1, p[1], p[2] + 1)) != "-" and \
                            self.bord.get((p[0] - 1, p[1], p[2] + 1)).name[2] != chman.name[2]:
                        self.eda.append((p[0] - 1, p[1], p[2] + 1))
                        self.psm.append((p[0] - 1, p[1], p[2] + 1))
                if self.bord.get((p[0] + 1, p[2] + 1, p[2])) != None:
                    if self.bord.get((p[0] + 1, p[2] + 1, p[2])) != "-" and \
                            self.bord.get((p[0] + 1, p[2] + 1, p[2])).name[2] != chman.name[2]:
                        self.eda.append((p[0] + 1, p[1] + 1, p[2]))
                        self.psm.append((p[0] + 1, p[1] + 1, p[2]))
            else:
                if self.bord.get((p[0], p[1] - 1, p[2] - 1)) == '-':
                    self.psm.append((p[0], p[1] - 1, p[2] - 1))
                    if chman.f1 == 1 and self.bord.get((p[0], p[1] - 2, p[2] - 2)) == '-':
                        self.psm.append((p[1], p[1] - 2, p[2] - 2))
                if self.bord.get((p[0] - 1, p[1] - 1, p[2])) != None:
                    if self.bord.get((p[0] - 1, p[1] - 1, p[2])) != "-" and \
                            self.bord.get((p[0] - 1, p[1] - 1, p[2])).name[2] != chman.name[2]:
                        self.eda.append((p[0] - 1, p[1] - 1, p[2]))
                        self.psm.append((p[0] - 1, p[1] - 1, p[2]))
                if self.bord.get((p[0] - 1, p[1], p[2] + 1)) != None:
                    if self.bord.get((p[0] - 1, p[1], p[2] + 1)) != "-" and \
                            self.bord.get((p[0] - 1, p[1], p[2] + 1)).name[2] != chman.name[2]:
                        self.eda.append((p[0] + 1, p[1], p[2] - 1))
                        self.psm.append((p[0] + 1, p[1], p[2] - 1))
        return self.psm, self.eda

    def magic(self, p1, p2):
        vmv = list()
        ch = []
        if self.bord.get(p1) == None: return "Error: Нет таких координат!"

        if self.bord.get(p1) == "-": return "Мимо"

        if self.bord.get(p1).name[2] != self.ippl: return "Не тот цвет"

        if self.check == "w" or self.check == "b":
            # Создаем поле проверки
            self.bord1 = self.bord.copy()
            self.bord1[p1] = "-"
            self.bord1[p2] = self.bord[p1]
            self.bord1[p2].pos = p2
            self.reippl = self.ippl
            # меняем сторону
            if self.ippl == "w":
                self.ippl = "b"
            else:
                self.ippl = "w"
            # обнуляем шах
            self.recheck = self.check
            self.check = 0
            # Проверяем сохранился ли шах
            for i in self.chmanpos:
                if i.name[2] == self.ippl:
                    self.checkmv(self.bord1.get(i.pos), self.bord1)
            # Если сохраился
            if self.check != 0:
                self.ippl = self.reipplv
                self.check = self.recheck
                self.bord1[p2].pos = p1
                self.bord1 = self.bord.copy()
                return "Ход невозм."
            # Иначе
            else:
                if self.bord1[p2].name[1] == 'p' and self.bord1[p2].f1 == 1:
                    self.bord1[p2].f1 = 0
                self.ippl = self.reippl
                # ret = self.checkmv(self.bord.get(p1), self.bord)
                self.bord = self.bord1.copy()
                # self.checkmv(self.bord1.get(p2), self.bord)
                for i in self.bord:
                    if self.bord[i] != "-":
                        ch.append(self.bord[i])
                self.chmanpos = ch
                if self.ippl == "w":
                    self.ippl = "b"
                else:
                    self.ippl = "w"

                return "ALL RIGHT"  # , ret
        else:
            """for i in chmanpos:
                if i.name[2] == self.ippl and i.name != f"K1{self.ippl}":
                    vmv.append(self.checkmv(i,self.bord)[0])"""
            # Проверка возможен ли ход
            if p2 in self.checkmv(self.bord.get(p1), self.bord)[0]:
                # Проверка на открытый шах
                self.bord1 = self.bord.copy()
                self.bord1[p1] = "-"
                self.bord1[p2] = self.bord[p1]
                self.bord1[p2].pos = p2
                self.reippl = self.ippl

                if self.ippl == "w":
                    self.ippl = "b"
                else:
                    self.ippl = "w"
                # Проверка на появление шаха
                for i in self.chmanpos:
                    if i.name[2] == self.ippl:
                        self.checkmv(self.bord1.get(i.pos), self.bord1)
                # Если шах есть то ход невозможен
                if self.check != 0:
                    self.bord1[p2].pos = p1
                    self.ippl = self.reippl
                    self.check = 0
                    self.bord1 = self.bord.copy()
                    return "Ход невозм."
                # Иначе
                else:
                    if self.bord1[p2].name[1] == 'p' and self.bord1[p2].f1 == 1:
                        self.bord1[p2].f1 = 0

                    self.ippl = self.reippl
                    # ret = self.checkmv(self.bord.get(p1),self.bord)
                    self.bord = self.bord1.copy()
                    # self.checkmv(self.bord1.get(p2),self.bord)

                    for i in self.bord:
                        if self.bord[i] != "-":
                            ch.append(self.bord[i])
                    self.chmanpos = ch
                    if self.ippl == "w":
                        self.ippl = "b"
                    else:
                        self.ippl = "w"

                    return "ALL RIGHT"  # , ret
            # Если ход не нашолся
            else:
                return "BAD MOVE"


move = move()

if __name__ == '__main__':
    main()
