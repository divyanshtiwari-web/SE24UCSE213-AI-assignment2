from collections import deque
from tictactoe_utils import *

def bfs_tictactoe(start_board):
    queue = deque([(start_board, 'X')])
    visited = set()

    while queue:
        board, player = queue.popleft()

        if is_winner(board, 'X'):
            return board, "X Wins (BFS)"

        if is_winner(board, 'O') or is_draw(board):
            continue

        visited.add(board)
        next_player = 'O' if player == 'X' else 'X'

        for successor in get_successors(board, player):
            if successor not in visited:
                queue.append((successor, next_player))

    return None, "No Solution (BFS)"
