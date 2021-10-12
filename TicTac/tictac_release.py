"""Tictac Game."""
from tictac_pygame import run_game


def check_winner(field, turn, size):
    """Check win or draw."""
    main_diag = field[0][0]
    rev_diag = field[0][size - 1]
    for main_ind in range(size):
        if main_diag != field[main_ind][main_ind]:
            main_diag = 0
        if rev_diag != field[main_ind][size - main_ind - 1]:
            rev_diag = 0
        row = field[0][main_ind]
        col = field[main_ind][0]
        for ind in range(size):
            if row != field[ind][main_ind]:
                row = 0
            if col != field[main_ind][ind]:
                col = 0
        if row != 0:
            return row
        if col != 0:
            return col
    if main_diag != 0:
        return main_diag
    if rev_diag != 0:
        return rev_diag
    if turn == size * size:
        return 3


def input_coords(line, size):
    """Corrects input of x and y."""
    answer = False
    line = line.split()
    if len(line) != 2:
        print("Incorrect input. Please try again")
    else:
        y, x = line
        if x.isdigit() and y.isdigit():
            x, y = int(x) - 1, int(y) - 1
            if x >= size or y >= size:
                print("One of your coordinats is more than field size.",
                      "Please try again")
            elif x < 0 or y < 0:
                print("One of your coordinats is less than 1.",
                      "Please try again")
            else:
                answer = (x, y)
        else:
            print("Incorrect input. Please try again")
    return answer


class GameClass():
    """Game class."""

    def __init__(self, size):
        """Initialise of game."""
        line = input("Game have 2 mods:\n" +
                     "Input 1 to play in console mode\n" +
                     "Input 2 to play in graphic mode\n")
        if line == "1":
            self.size = size
            game_end = False
            while not game_end:
                self.start()
                self.game_loop()
                game_end = self.end()
        elif line == "2":
            run_game(size)

    def start(self):
        """Start configuration of game."""
        self.field = [[0] * self.size for _ in range(self.size)]
        self.turn = 0
        self.game_over = False

    def end(self):
        """End events in game."""
        if self.game_over == 1:
            text = "First player wins."
        elif self.game_over == 2:
            text = "Second player wins."
        elif self.game_over == 3:
            text = "Draw."
        line = input(text + " To end game input 1.\n" +
                     "To restart input something another: ")
        return line == "1"

    def output_matrix(self):
        """Matrix output."""
        for line in self.field:
            print(*line)

    def game_loop(self):
        """Loop which operates user's turns."""
        while not self.game_over:
            print("Current configuration:")
            self.output_matrix()
            print(f"Turn of Player {self.turn % 2}")
            correct_input = False
            while not correct_input:
                line = input("Input x and y of matrix " +
                             "(left upper conner have " +
                             "x=1, y=1 coords): ")
                correct_input = input_coords(line, self.size)
            x, y = correct_input
            if self.field[x][y] != 0:
                print("This cell is taken. Please input coords of empty cell")
                continue
            self.field[x][y] = self.turn % 2 + 1
            self.turn += 1
            self.game_over = check_winner(self.field, self.turn, self.size)
        return self.game_over


if __name__ == "__main__":
    print("Greetings, players!")
    size = input("Input width from 3 to 6 of your tictac " +
                 "field or press Enter for choosing default: ")
    if not size.isdigit() or size < "3":
        size = 3
    elif size > "6":
        size = 6
    size = int(size)
    GameClass(size)
