import numpy as np

pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']

a = np.array([[pieces[i] for i in range(8)] for z in range(8)])
#print(a)
b = np.array(pieces)
print(b)