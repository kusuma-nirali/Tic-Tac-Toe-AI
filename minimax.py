
# Tic-Tac-Toe AI - Minimax Algorithm

from game_logic import check_winner, available_moves

AI_PLAYER = "O"
HUMAN_PLAYER = "X"


def minimax(board, is_maximizing):
    """
    Minimax algorithm to find the best possible move.
    """

    winner = check_winner(board)

    # AI wins
    if winner == AI_PLAYER:
        return 10

    # Human wins
    if winner == HUMAN_PLAYER:
        return -10

    # Draw
    if len(available_moves(board)) == 0:
        return 0

    if is_maximizing:
        best_score = float("-inf")

        for move in available_moves(board):
            board[move] = AI_PLAYER

            score = minimax(board, False)

            board[move] = " "
            best_score = max(score, best_score)

        return best_score

    else:
        best_score = float("inf")

        for move in available_moves(board):
            board[move] = HUMAN_PLAYER

            score = minimax(board, True)

            board[move] = " "
            best_score = min(score, best_score)

        return best_score


def find_best_move(board):
    """Finds the best move for the AI."""

    best_score = float("-inf")
    best_move = None

    for move in available_moves(board):
        board[move] = AI_PLAYER

        score = minimax(board, False)

        board[move] = " "

        if score > best_score:
            best_score = score
            best_move = move

    return best_move
