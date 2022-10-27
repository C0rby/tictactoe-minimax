#!/usr/bin/env python3
import copy
import time

EMPTY = '.'
P1 = 'x'
P2 = 'o'

EMPTY_BOARD = [[EMPTY, EMPTY, EMPTY],
               [EMPTY, EMPTY, EMPTY],
               [EMPTY, EMPTY, EMPTY]]
SCORE_MAP = {
    P1: 1,
    EMPTY: 0,
    P2: -1,
}


def evaluate(board):
    """
    [[0 1 2]
    [0 1 2]
    [0 1 2]]
    """
    for i in range(3):
        # check horizontal
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return True, board[i][0]
        # check vertical
        elif board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return True, board[0][i]

    # check diagonal top left to bottom right
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return True, board[0][0]
    # check diagonal top left to bottom right
    elif board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return True, board[0][2]

    if EMPTY not in board[0] and \
       EMPTY not in board[1] and \
       EMPTY not in board[2]:
        return True, EMPTY

    return False, EMPTY


def next_states(board, player):
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                try:
                    board[i][j] = player
                    yield board
                finally:
                    board[i][j] = EMPTY


def print_board(board):
    for i in range(3):
        print(' '.join(board[i]))
    print()


def _min(board, alpha, beta):
    is_terminal, winner = evaluate(board)
    if is_terminal:
        return SCORE_MAP[winner]

    score = 2
    for s in next_states(board, P2):
        ss = _max(board, alpha, beta)
        if ss < score:
            score = ss
        if ss <= alpha:
            return score
        if ss < beta:
            beta = ss
    return score


def _max(board, alpha, beta):
    is_terminal, winner = evaluate(board)
    if is_terminal:
        return SCORE_MAP[winner]

    score = -2
    for s in next_states(board, P1):
        ss = _min(board, alpha, beta)
        if ss > score:
            score = ss
        if ss >= beta:
            return score
        if ss > alpha:
            alpha = ss
    return score


b = copy.deepcopy(EMPTY_BOARD)

currentPlayer = P1
while not evaluate(b)[0]:
    start = time.perf_counter()
    if currentPlayer == P1:
        score = -2
        for s in next_states(b, P1):
            ss = _min(s, -2, 2)
            if score < ss:
                score = ss
                b = copy.deepcopy(s)
        currentPlayer = P2
    else:
        currentPlayer = P1
        x, y = map(int, input('Position:').split(','))
        b[x][y] = P2
    stop = time.perf_counter()
    print(f"Thinking time: {stop - start:0.4f} seconds")
    print_board(b)

_, winner = evaluate(b)
if winner == P1:
    print("The Computer won")
elif winner == P2:
    print("Congrats you won!")
else:
    print("Draw!")
