import numpy as np

white_pieces = ['wR', 'wN', 'bK', 'wQ', 'wK', 'bK', 'wN', 'wR']
white_pawns = ['wp' for i in range(8)]
black_pawns = ['bp' for i in range(8)]
blank = ['--' for i in range(8)]
black_pieces = ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR']
#a = np.array([[pieces[i] for i in range(8)] for z in range(8)])
#print(a)
b = np.array([[black_pieces],[black_pawns],[blank],[blank],[blank],[blank],[white_pawns],[white_pieces]])
print(b)