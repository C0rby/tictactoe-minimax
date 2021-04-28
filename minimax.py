#!/usr/bin/env python3

import time
import random

# Symbols
EMPTY = '.'
X = 'X'
O = 'O'

EMPTY_BOARD = [EMPTY, EMPTY, EMPTY,
               EMPTY, EMPTY, EMPTY,
               EMPTY, EMPTY, EMPTY]

class Board:

    def __init__(self, fields = None):
        self._fields = fields or EMPTY_BOARD

    def __str__(self):
        rows = [self._fields[i: i+3] for i in range(0, 7, 3)]
        b = []
        for row in rows:
            b.append(' '.join(map(str, row)))
        return '\n'.join(b) + '\n'

    def isMovesLeft(self):
        return EMPTY in self._fields

    def evaluate(self):
        if self.hasSameSymbol(1, 4, 7) or \
           self.hasSameSymbol(0, 4, 8) or \
           self.hasSameSymbol(2, 4, 6) or \
           self.hasSameSymbol(3, 4, 5):
            if self.cell_at(4) == X:
                return 10
            else:
                return -10
        elif self.hasSameSymbol(0, 1, 2) or \
             self.hasSameSymbol(0, 3, 6):
            if self.cell_at(0) == X:
                return 10
            else:
                return -10
        elif self.hasSameSymbol(2, 5, 8) or \
             self.hasSameSymbol(6, 7, 8):
            if self.cell_at(8) == X:
                return 10
            else:
                return -10

        return 0

    def hasSameSymbol(self, idx1,idx2,idx3):
        return self._fields[idx1] != EMPTY and \
               self._fields[idx1] == self._fields[idx2] == self._fields[idx3]

    def isTerminalState(self):
        return not self.isMovesLeft() or self.evaluate() != 0

    def board_value(self):
        return int(self.has3Connections())

    def cell_at(self, idx):
        return self._fields[idx]

    def set_cell(self, idx, symbol):
        self._fields[idx] = symbol

    def empty_cell(self, idx):
        self.set_cell(idx, EMPTY)

    def show_move(self, idx, symbol):
        self._fields[idx] = symbol
        print(self)
        self._fields[idx] = EMPTY

def findBestMoveO(board):
    bestScore = 1001 
    bestMove = -1
    for i in range(9):
        if board.cell_at(i) == EMPTY:
            board.set_cell(i, O)
            score = minimax(board, 0, True, -1000, 1000)
            board.empty_cell(i)
            if bestScore > score:
                bestScore = score
                bestMove = i
    return bestMove

def findBestMoveX(board):
    bestScore = -1001 
    bestMove = -1
    for i in range(9):
        if board.cell_at(i) == EMPTY:
            board.set_cell(i, X)
            score = minimax(board, 0, False, -1000, 1000)
            board.empty_cell(i)
            if bestScore < score:
                bestScore = score
                bestMove = i
    return bestMove



def minimax(board, depth, isMaxPlayer, alpha, beta):
    if board.isTerminalState():
        score = board.evaluate()
        if score == 0:
            return score
        
        if isMaxPlayer:
            return score - depth
        else:
            return score + depth

    if isMaxPlayer:
        score = -1000
        for i in range(9):
            if board.cell_at(i) == EMPTY:
                board.set_cell(i, X)
                score = max(score, minimax(board, depth+1, False, alpha, beta))
                board.empty_cell(i)
                alpha = max(alpha, score)
                if alpha >= beta:
                    break
        return score
    else:
        score = 1000
        for i in range(9):
            if board.cell_at(i) == EMPTY:
                board.set_cell(i, O)
                score = min(score, minimax(board, depth+1, True, alpha, beta))
                board.empty_cell(i)
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return score


#board = Board([X, O, X, O, O, X, EMPTY, EMPTY, EMPTY])
board = Board()

first_pos = random.randrange(9)

board.set_cell(first_pos, X)

turn = O
while not board.isTerminalState():
    print(board)
    # time.sleep(1.5)
    if turn == X:
        com_pos = findBestMoveX(board)
        board.set_cell(com_pos, X)
        turn = O
    elif turn == O:
        pos = int(input("Position: "))
        if board.cell_at(pos) != EMPTY:
            print("Position is not empty")
            continue
        #pos = findBestMoveO(board) 
        board.set_cell(pos, turn) 
        turn = X

print(board)    
score = board.evaluate()
print(score)

