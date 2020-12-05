import chess
#import chess.svg

#print(chess.svg.piece(chess.Piece.from_symbol("R")))
board = chess.Board()
print(board.turn)
print(board.fullmove_number)

move = chess.Move.from_uci("g1f3")
move1 = chess.Move.from_uci('a7a6')

print(board.legal_moves)
print(move in board.legal_moves)
if move in board.legal_moves:
    board.push(move)
if move1 in board.legal_moves:
    board.push(move1)
print(board)
print(board.legal_moves)
print(board.is_legal(move1))
print(board.is_valid())
print(board.fullmove_number)
print(board.turn)
'''
>>> board = chess.Board()
>>> board.legal_moves.count()
20
>>> bool(board.legal_moves)
True
>>> move = chess.Move.from_uci("g1f3")
>>> move in board.legal_moves
True
'''

