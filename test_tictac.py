"""Tests for tictactoe."""
import unittest
from tictac import TicTac


class TestGame(unittest.TestCase):
    """Test class."""

    def test_rev_diag(self):
        """Check win on reverse diagonal."""
        field = [[0, 2, 1], [0, 1, 0], [1, 2, 0]]
        turn = 4
        self.assertEqual(TicTac.check_winner(field, turn, 3), 1)

    def test_main_diag(self):
        """Check win on main diagonal."""
        field = [[2, 1, 1], [0, 2, 1], [1, 2, 2]]
        turn = 7
        self.assertEqual(TicTac.check_winner(field, turn, 3), 2)

    def test_draw(self):
        """Check draw."""
        field = [[1, 2, 1], [2, 1, 1], [2, 1, 2]]
        turn = 9
        self.assertEqual(TicTac.check_winner(field, turn, 3), 3)

    def test_col_win(self):
        """Check win on column."""
        field = [[1, 2, 1], [1, 2, 0], [1, 0, 2]]
        turn = 6
        self.assertEqual(TicTac.check_winner(field, turn, 3), 1)

    def test_row_win(self):
        """Check win on row."""
        field = [[1, 1, 0], [2, 2, 2], [0, 0, 1]]
        turn = 5
        self.assertEqual(TicTac.check_winner(field, turn, 3), 2)

    def test_5_by_5(self):
        """Check 5x5 matrix."""
        field = [[1, 2, 2, 1, 2], [1, 2, 2, 1, 1], [2, 1, 2, 1, 1],
                 [2, 1, 2, 1, 2], [0, 2, 1, 1, 0]]
        turn = 22
        self.assertEqual(TicTac.check_winner(field, turn, 5), 1)


if __name__ == "__main__":
    unittest.main()
