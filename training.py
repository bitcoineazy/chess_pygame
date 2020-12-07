import chess
#import chess.svg

#print(chess.svg.piece(chess.Piece.from_symbol("R")))
board = chess.Board()





move1 = chess.Move.from_uci('a2a3')

print(board.legal_moves)
'''print(move in board.legal_moves)'''
'''if move in board.legal_moves:
    board.push(move)'''
if move1 in board.legal_moves:
    board.push(move1)

move2 = chess.Move.from_uci('a7a6')
print(board.is_legal(move2))
if move2 in board.legal_moves:
    board.push(move2)
print(board)
print(board.legal_moves)

print(board.is_valid())



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
print(type(board))

