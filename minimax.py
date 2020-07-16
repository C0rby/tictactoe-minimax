#!/usr/bin/env python3

# Symbols
EMPTY = '.'
X = 'X' 
O = 'O' 

def print_board(board):
    rows = [board[i: i+3] for i in range(0, 7, 3)]
    for row in rows:
        print(' '.join(map(str, row)))

board1 = [EMPTY, EMPTY, EMPTY,
          EMPTY, EMPTY, EMPTY,
          EMPTY, EMPTY, EMPTY]
#print_board(board1)
#print(board1)

def isMovesLeft(board):
    return 0 in board

#print(isMovesLeft(board))

full_board = [X, X, X,
              X, X, X,
              X, X, X]
#print(not isMovesLeft(full_board))

def hasSameSymbols(board, idx1, idx2, idx3):
    return board[idx1] != 0 and \
           board[idx1] == board[idx2] == board[idx3]

def has3Connections(board):
    return hasSameSymbols(board, 0, 1, 2) or \
           hasSameSymbols(board, 0, 4, 8) or \
           hasSameSymbols(board, 0, 3, 6) or \
           hasSameSymbols(board, 1, 4, 7) or \
           hasSameSymbols(board, 2, 4, 6) or \
           hasSameSymbols(board, 3, 4, 5) or \
           hasSameSymbols(board, 2, 5, 8) or \
           hasSameSymbols(board, 6, 7, 8)

def isTerminalState(board):
    """
    [0,1,2,
     3,4,5,
     6,7,8]
    """
    return not isMovesLeft(board) or \
           has3Connections(board) 

def board_value(board):
    return int(has3Connections(board))

def minimax(board, depth, isMaxPlayer):
    if isTerminalState(board):
        if not has3Connections(board):
            return 0
        
        v = board_value(board)
        if isMaxPlayer:
            return v
        else:
            return -v

some_board = [X, X, O, O, O, O, X, X, O]
print(minimax(some_board, 0, False))        
print_board(some_board)
