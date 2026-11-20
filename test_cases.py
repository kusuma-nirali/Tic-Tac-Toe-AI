
# Tic-Tac-Toe AI - Test Cases

import unittest

from game_logic import (
    create_board,
    available_moves,
    make_move,
    check_winner,
    is_draw
)

from minimax import find_best_move


class TestTicTacToeAI(unittest.TestCase):

    def test_empty_board(self):
        board = create_board()
        self.assertEqual(len(board), 9)
        self.assertEqual(len(available_moves(board)), 9)

    def test_valid_move(self):
        board = create_board()
        result = make_move(board, 0, "X")

        self.assertTrue(result)
        self.assertEqual(board[0], "X")

    def test_invalid_move(self):
        board = create_board()
        make_move(board, 0, "X")

        result = make_move(board, 0, "O")

        self.assertFalse(result)
        self.assertEqual(board[0], "X")

    def test_horizontal_winner(self):
        board = ["X", "X", "X",
                 " ", " ", " ",
                 " ", " ", " "]

        self.assertEqual(check_winner(board), "X")

    def test_vertical_winner(self):
        board = ["O", " ", " ",
                 "O", " ", " ",
                 "O", " ", " "]

        self.assertEqual(check_winner(board), "O")

    def test_diagonal_winner(self):
        board = ["X", " ", " ",
                 " ", "X", " ",
                 " ", " ", "X"]

        self.assertEqual(check_winner(board), "X")

    def test_draw(self):
        board = ["X", "O", "X",
                 "X", "O", "O",
                 "O", "X", "X"]

        self.assertTrue(is_draw(board))

    def test_ai_winning_move(self):
        board = ["O", "O", " ",
                 "X", "X", " ",
                 " ", " ", " "]

        best_move = find_best_move(board)

        self.assertEqual(best_move, 2)

    def test_ai_blocks_human(self):
        board = ["X", "X", " ",
                 " ", "O", " ",
                 " ", " ", " "]

        best_move = find_best_move(board)

        self.assertEqual(best_move, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
