
# Tic-Tac-Toe AI - Game Logic

def create_board():
    """Creates an empty 3x3 game board."""
    return [" " for _ in range(9)]


def display_board(board):
    """Displays the current game board."""
    print("\n")
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("---------")
    print("\n")


def available_moves(board):
    """Returns all empty positions."""
    return [i for i in range(9) if board[i] == " "]


def make_move(board, position, player):
    """Places X or O at the selected position."""
    if position in available_moves(board):
        board[position] = player
        return True
    return False


def check_winner(board):
    """Checks whether a player has won."""

    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combination in winning_combinations:
        a, b, c = combination

        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    return None


def is_draw(board):
    """Checks whether the game is a draw."""
    return check_winner(board) is None and len(available_moves(board)) == 0
