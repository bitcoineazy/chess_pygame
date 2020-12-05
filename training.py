import chess
import chess.svg

#print(chess.svg.piece(chess.Piece.from_symbol("R")))
board = chess.Board()
board.turn
bq = len(board.pieces(chess.KING, chess.BLACK))
#chess.KING.piece_symbol()
print(chess.Move(chess.A2, chess.A3).uci()) #(chess.A2, chess.A3)
chess.parse_square('a6')
chess.SQUARE_NAMES.index('a6')
new = chess.Move.from_uci("a2a3")
board.push(new)
print(board.legal_moves)
print(board)
print(board.is_legal(new))
print(board.is_valid())
