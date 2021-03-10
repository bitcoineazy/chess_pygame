import pygame
import numpy as np
import chess
import os

height = 990
width = 900
fps = 30
images = {}


def loadimage():
    figures = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for role in figures:
        images[role] = pygame.transform.scale(pygame.image.load('images_cardinal/'+role+'.svg'), (85, 85))

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
        #self.board = np.array([black_pieces,black_pawns,blank,blank,blank,blank,white_pawns,white_pieces])
        self.board = [hex_1, hex_2, hex_3, hex_4, hex_5, hex_6, hex_7, hex_8, hex_9, hex_10, hex_11]
        self.move_log = []
        #self.moves_by_nearest_hex = []
        self.chess = []
        self.recorded_centers_of_hexagons = {}
        self.chess_table = chess.Board()
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


    def make_move(self, start, end):
        #board = chess.Board()
        #print(board, start, end)
        #uci_move_1 = chess.Move.from_uci(self.notation(start, end))
        print(self.notation(start, end))
        self.move_log.append(self.notation(start, end))
        self.whiteToMove = not self.whiteToMove
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


    def notation_to_board(self, nearest_loc):
        all_notation_dicts = [[self.notation_to_board_dict_1], [self.notation_to_board_dict_2], [self.notation_to_board_dict_3],
                              [self.notation_to_board_dict_4], [self.notation_to_board_dict_5], [self.notation_to_board_dict_6],
                              [self.notation_to_board_dict_7], [self.notation_to_board_dict_8], [self.notation_to_board_dict_9],
                              [self.notation_to_board_dict_10], [self.notation_to_board_dict_11]]
        '''проходимся по всем эл-м массива со словарями 11-линий отрисовки поля (ключ=строка, значение=столбец)
        строка и столбец после хода 2-ух игроков попадает в функцию self.make_move и изменяет матрицу поля self.board
        с заменой эл-ов массива () . Фигуры рисуются по значениям в матрице поле и любые изменения в массиве поменяют само
        поле.           
        '''
        i = 0
        column = 0
        row = 0
        for key in all_notation_dicts[0:11]:
            if nearest_loc in key[0].values():#узнаем в каком массиве из матрицы ближ шестиугольник к клику (номер столбца)
                column += i
                for key, value in key[0].items():#узнаем ключ эл-ма по значению, ключ в этом случае - номер по списку (номер строки)
                    if value == nearest_loc:
                        row += key
            i += 1
        print(f"column: {column},row: {row}")

    def notation(self, start, end):
        board_dict = {'a1': [60, 720], 'b1': [138, 765], 'c1': [216, 810], 'd1': [294, 855], 'e1': [372, 900], 'f1': [450, 945], 'g1': [528, 900], 'h1': [606, 855], 'i1': [684, 810], 'k1': [762, 765], 'l1': [840, 720],
                      'a2': [60, 630], 'b2': [138, 675], 'c2': [216, 720], 'd2': [294, 765], 'e2': [372, 810], 'f2': [450, 855], 'g2': [528, 810], 'h2': [606, 765], 'i2': [684, 720], 'k2': [762, 675], 'l2': [840, 630],
                      'a3': [60, 540], 'b3': [138, 585], 'c3': [216, 630], 'd3': [294, 675], 'e3': [372, 720], 'f3': [450, 765], 'g3': [528, 720], 'h3': [606, 675], 'i3': [684, 630], 'k3': [762, 585], 'l3': [840, 540],
                      'a4': [60, 450], 'b4': [138, 495], 'c4': [216, 540], 'd4': [294, 585], 'e4': [372, 630], 'f4': [450, 675], 'g4': [528, 630], 'h4': [606, 585], 'i4': [684, 540], 'k4': [762, 495], 'l4': [840, 450],
                      'a5': [60, 360], 'b5': [138, 405], 'c5': [216, 450], 'd5': [294, 495], 'e5': [372, 540], 'f5': [450, 585], 'g5': [528, 540], 'h5': [606, 495], 'i5': [684, 450], 'k5': [762, 405], 'l5': [840, 360],
                      'a6': [60, 270], 'b6': [138, 315], 'c6': [216, 360], 'd6': [294, 405], 'e6': [372, 450], 'f6': [450, 495], 'g6': [528, 450], 'h6': [606, 405], 'i6': [684, 360], 'k6': [762, 315], 'l6': [840, 270],
                      'b7': [138, 225], 'c7': [216, 270], 'd7': [294, 315], 'e7': [372, 360], 'f7': [450, 405], 'g7': [528, 360], 'h7': [606, 315], 'i7': [684, 270], 'k7': [762, 225],
                      'c8': [216, 180], 'd8': [294, 225], 'e8': [372, 270], 'f8': [450, 315], 'g8': [528, 270], 'h8': [606, 225], 'i8': [684, 180],
                      'd9': [294, 135], 'e9': [372, 180], 'f9': [450, 225], 'g9': [528, 180], 'h9': [606, 135],
                      'e10': [372, 90], 'f10': [450, 135], 'g10': [528, 90],
                      'f11': [450, 45],
                      }

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

    def get_nearest_value(self, n_value, n_list): #получение ближайшего значения к n_value из списка n_list
        list_of_diffs = [abs(n_value - x) for x in n_list]
        result_index = list_of_diffs.index(min(list_of_diffs))
        return n_list[result_index]

    def define_nearest_hex(self, coords): #получение координат ближайшего шестиугольника от клика мышки
        x_coords = [] #x_координаты центров всех шестиугольников
        y_coords = [] #y_координаты центров всех шестиугольников
        for each in self.recorded_centers_of_hexagons.values():
            x_coords.append(each[0])
            y_coords.append(each[1])
        #print(coords)
        x_nearest = self.get_nearest_value(coords[0], x_coords)
        y_nearest = self.get_nearest_value(coords[1], y_coords)
        hexogonal_selected = [x_nearest, y_nearest]
        return hexogonal_selected


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
                    sq_selected = (column, row)
                    moves.append(gamestate.define_nearest_hex(location)) #добавляем 1 и 2 координаты шестиугольника, ближайшего к курсору мыши
                    #gamestate.moves_by_nearest_hex = []
                    #gamestate.moves_by_nearest_hex.append(gamestate.define_nearest_hex(location))
                    gamestate.notation_to_board(gamestate.define_nearest_hex(location))
                print('Кол-во шестиугольников: ', len(gamestate.recorded_centers_of_hexagons))
                print(sq_selected, moves)
                #print(gamestate.notation_to_board_dict)

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
        hexagon_1 = Hexagons(450-(part_1*78), 945 - (part_1*45), 90) #90-размер
        pygame.draw.polygon(screen, color, hexagon_1.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_1.points)
        gamestate.recorded_centers_of_hexagons.update({f'{part_1+1}hex':[(450-(part_1*78)), 945 - (part_1*45)]})
        gamestate.notation_to_board_dict_1.update({part_1:gamestate.define_nearest_hex([hexagon_1.xc,hexagon_1.yc])})
        piece = gamestate.board[0][part_1]
        if piece != '--':
            screen.blit(images[piece], pygame.Rect((gamestate.recorded_centers_of_hexagons[f'{part_1+1}hex'][0]-42,
                                                    gamestate.recorded_centers_of_hexagons[f'{part_1+1}hex'][1]-47, 0, 0)))
    for part_2 in range(7):
        color = colors[((part_2 + 1) % 3)]
        hexagon_2 = Hexagons(528 - (part_2 * 78), 900 - (part_2 * 45), 90)
        pygame.draw.polygon(screen, color, hexagon_2.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_2.points)
        gamestate.recorded_centers_of_hexagons.update({f'{part_2+7}hex': [(528 - (part_2 * 78)), 900 - (part_2 * 45)]})
        gamestate.notation_to_board_dict_2.update({part_2: gamestate.define_nearest_hex([hexagon_2.xc, hexagon_2.yc])})
        piece = gamestate.board[1][part_2]
        if piece != '--':
            screen.blit(images[piece], pygame.Rect((gamestate.recorded_centers_of_hexagons[f'{part_2 + 7}hex'][0] - 42,
                                                    gamestate.recorded_centers_of_hexagons[f'{part_2 + 7}hex'][1] - 47,0,0)))

    for part_3 in range(8):
        color = colors[((part_3 + 2) % 3)]
        hexagon_3 = Hexagons(606 - (part_3 * 78), 855 - (part_3 * 45), 90)
        pygame.draw.polygon(screen, color, hexagon_3.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_3.points)
        gamestate.recorded_centers_of_hexagons.update({f'{part_3+14}hex': [(606 - (part_3 * 78)), 855 - (part_3 * 45)]})
        gamestate.notation_to_board_dict_3.update({part_3: gamestate.define_nearest_hex([hexagon_3.xc, hexagon_3.yc])})
        piece = gamestate.board[2][part_3]
        if piece != '--':
            screen.blit(images[piece], pygame.Rect((gamestate.recorded_centers_of_hexagons[f'{part_3 + 14}hex'][0] - 42,
                                                    gamestate.recorded_centers_of_hexagons[f'{part_3 + 14}hex'][1] - 47,0,0)))
    for part_4 in range(9):
        color = colors[((part_4 + 3) % 3)]
        hexagon_4 = Hexagons(684 - (part_4 * 78), 810 - (part_4 * 45), 90)
        pygame.draw.polygon(screen, color, hexagon_4.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_4.points)
        gamestate.recorded_centers_of_hexagons.update({f'{part_4+22}hex': [(684 - part_4 * 78), 810 - (part_4 * 45)]})
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
        gamestate.recorded_centers_of_hexagons.update({f'{part_5+31}hex': [(762 - part_5 * 78), 765 - (part_5 * 45)]})
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
        gamestate.recorded_centers_of_hexagons.update({f'{part_6+41}hex': [(840 - part_6 * 78), 720 - (part_6 * 45)]})
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
        gamestate.recorded_centers_of_hexagons.update({f'{part_7+52}hex': [(840 - part_7 * 78), 630 - (part_7 * 45)]})
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
        gamestate.recorded_centers_of_hexagons.update({f'{part_8+62}hex': [(840 - part_8 * 78), 540 - (part_8 * 45)]})
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
        gamestate.recorded_centers_of_hexagons.update({f'{part_9+71}hex': [(840 - part_9 * 78), 450 - (part_9 * 45)]})
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
        gamestate.recorded_centers_of_hexagons.update({f'{part_10+79}hex': [(840 - part_10 * 78), 360 - (part_10 * 45)]})
        gamestate.notation_to_board_dict_10.update({part_10: gamestate.define_nearest_hex([hexagon_10.xc, hexagon_10.yc])})
        piece = gamestate.board[9][part_10]
        if piece != '--':
            screen.blit(images[piece], pygame.Rect((gamestate.recorded_centers_of_hexagons[f'{part_10 + 79}hex'][0] - 42,
                                                    gamestate.recorded_centers_of_hexagons[f'{part_10 + 79}hex'][1] - 42,
                                                    0, 0)))
    for part_11 in range(6):
        color = colors[((part_11) % 3)]
        hexagon_11 = Hexagons(840 - (part_11 * 78), 270 - (part_11 * 45), 90)
        pygame.draw.polygon(screen, color, hexagon_11.points)
        pygame.draw.aalines(screen, pygame.Color('black'), True, hexagon_11.points)
        gamestate.recorded_centers_of_hexagons.update({f'{part_11+86}hex': [(840 - part_11 * 78), 270 - (part_11 * 45)]})
        gamestate.notation_to_board_dict_11.update({part_11: gamestate.define_nearest_hex([hexagon_11.xc, hexagon_11.yc])})
        piece = gamestate.board[10][part_11]
        if piece != '--':
            screen.blit(images[piece],
                        pygame.Rect((gamestate.recorded_centers_of_hexagons[f'{part_11 + 86}hex'][0] - 42,
                                     gamestate.recorded_centers_of_hexagons[f'{part_11 + 86}hex'][1] - 42,
                                     0, 0)))


if __name__ == '__main__':
    main()