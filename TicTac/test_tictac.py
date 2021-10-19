"""Tests for tictactoe."""
import sys
import unittest
from tictac_release import GameClass


class TestGame(unittest.TestCase):
    """Test class."""

    def setUp(self):
        sys.stdout, self.temp = None, sys.stdout
        self.game = GameClass(3, 1)

    def test_rev_diag(self):
        """Check win on reverse diagonal."""
        self.game.field = [[0, 2, 1], [0, 1, 0], [1, 2, 0]]
        self.game.turn = 5
        self.assertEqual(self.game.check_winner(), 1)

    def test_main_diag(self):
        """Check win on main diagonal."""
        self.game.field = [[2, 1, 1], [0, 2, 1], [1, 2, 2]]
        self.game.turn = 8
        self.assertEqual(self.game.check_winner(), 2)

    def test_draw(self):
        """Check draw."""
        self.game.field = [[1, 2, 1], [2, 1, 1], [2, 1, 2]]
        self.game.turn = 9
        self.assertEqual(self.game.check_winner(), 3)

    def test_col_win(self):
        """Check win on column."""
        self.game.field = [[1, 2, 1], [1, 2, 0], [1, 0, 2]]
        self.game.turn = 7
        self.assertEqual(self.game.check_winner(), 1)

    def test_row_win(self):
        """Check win on row."""
        self.game.field = [[1, 1, 0], [2, 2, 2], [0, 0, 1]]
        self.game.turn = 6
        self.assertEqual(self.game.check_winner(), 2)

    def test_5_by_5(self):
        """Check 5x5 matrix."""
        game = GameClass(5, 1)
        game.field = [[1, 2, 2, 1, 2], [1, 2, 2, 1, 1], [2, 1, 2, 1, 1],
                      [2, 1, 2, 1, 2], [0, 2, 1, 1, 0]]
        game.turn = 23
        self.assertEqual(game.check_winner(), 1)

    def test_incorrect_coords(self):
        """Check big coords."""
        self.assertFalse(self.game.input_coords("4 2"))

    def test_incorrect_coords2(self):
        """Check small coords."""
        self.assertFalse(self.game.input_coords("-2 2"))

    def test_incorrect_coords3(self):
        """Check amount coords."""
        self.assertFalse(self.game.input_coords("2 2 2"))

    def test_incorrect_coords4(self):
        """Check amount coords."""
        self.assertFalse(self.game.input_coords("2"))

    def test_incorrect_coords5(self):
        """Check not digits."""
        self.assertFalse(self.game.input_coords("a b"))

    def test_correct_coords(self):
        """Check for correct input."""
        self.assertEqual(self.game.input_coords("2 2"), (1, 1))

    def tearDown(self):
        sys.stdout = self.temp


if __name__ == "__main__":
    unittest.main()
