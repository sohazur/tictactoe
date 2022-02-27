"""
Tic Tac Toe Player
"""

from copy import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Checking if the game is over
    if terminal(board):
        return None
    # Checking if the board is in initial state or number of X is less than/equal to O
    elif board == initial_state() or sum(row.count(X) for row in board) <= sum(row.count(O) for row in board):
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Checking if the game is over
    if terminal(board):
        return None
    possible_actions = set()
    # Looking the Empty cells for possible actions
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Checking for valid move
    if (action in actions(board)) == False:
        raise Exception("Invalid Move")
    # Copying the board
    copy_board = board[:]
    # Putting the player in the cell
    copy_board[action[0]][action[1]] = player(board)
    return copy_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
