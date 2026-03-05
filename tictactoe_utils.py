# tictactoe_utils.py
WINNING_COMBOS = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]

def is_winner(board, player):
    for a, b, c in WINNING_COMBOS:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def is_draw(board):
    return ' ' not in board

def get_successors(board, player):
    successors = []
    for i in range(9):
        if board[i] == ' ':
            new_board = list(board)
            new_board[i] = player
            successors.append(tuple(new_board))
    return successors
