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
        self.chess_table.turn = True






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