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
    elif board == initial_state() or sum(row.count(X) for row in board) == sum(row.count(O) for row in board):
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
    # if (action not in actions(board)):
    #     raise Exception("Invalid Move")
    # Copying the board
    copy_board = [row[:] for row in board]
    # Putting the player in the cell
    copy_board[action[0]][action[1]] = player(board)
    return copy_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Checking rows
    for row in board:
        if len(set(row)) == 1:
            if row[0] == X or row[0] == O:
                return row[0]
    # Checking columns
    transpose_board = map(list, zip(*board))
    for row in transpose_board:
        if len(set(row)) == 1:
            if row[0] == X or row[0] == O:
                return row[0]
    # Checking diagonals
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        if board[0][0] == X or board[0][0] == O:
            return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        if board[0][len(board)-1] == X or board[0][len(board)-1] == O:
            return board[0][len(board)-1]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Checking if all the cells are filled
    if sum(row.count(EMPTY) for row in board) == 0:
        return True
    # Checking if already a winner exists
    elif winner(board) == X or winner(board) == O:
        return True
    else:
        return False


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
    if terminal(board):
        return None
    elif player(board) == X:
        v = -1
        for action in actions(board):
            if min_value(result(board, action)) >= v:
                v = min_value(result(board, action))
                optimal_action = action
    elif player(board) == O:
        v = 1
        for action in actions(board):
            if max_value(result(board, action)) <= v:
                v = max_value(result(board, action))
                optimal_action = action
    return optimal_action


# function for max_value
def max_value(board):
    if terminal(board):
        return utility(board)
    v = float("-inf")
    # optimal_action = None
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
        # Alpha-Beta Pruning
        if v == 1:
            break
    return v


# function for min_value
def min_value(board):
    if terminal(board):
        return utility(board)
    v = float("inf")
    # optimal_action = None
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
        # Alpha-Beta Pruning
        if v == -1:
            break
    return v