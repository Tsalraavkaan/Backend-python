"""Tictac Game."""
import pygame
import sys

WIN_WIDTH = WIN_HEIGHT = 1000
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARK_BLUE = (72, 61, 139)
DARK_ORANGE = (255, 140, 0)
DARK_RED = (139, 0, 0)


class TicTac:
    """Game class."""

    start_color = (0, 255, 255)
    start_text_color = (255, 63, 63)
    background_color = BLACK
    tictac_color = DARK_RED
    end_color = GREEN
    end_text_color = RED
    geetings_and_rules = ["Welcome to TicTac game!",
                          "Press Enter to Continue"]
    srif_size = 48

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

    def __init__(self, surface, size=3):
        """Write initial window and start."""
        self.surface = surface
        self.size = size
        self.surface.fill(TicTac.start_color)
        f = pygame.font.SysFont('arial', TicTac.srif_size)
        ind = 0
        for line in TicTac.geetings_and_rules:
            text = f.render(line, False, TicTac.start_text_color)
            self.surface.blit(text,
                              (WIN_WIDTH * 0.2,
                               WIN_HEIGHT * 0.3 + ind * TicTac.srif_size))
            ind += 1
        pygame.display.update()

        while True:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        self.start()
        self.game_loop()

    def mouse_click(self):
        """React on mouse events."""
        x, y = pygame.mouse.get_pos()
        col = int(x // (WIN_WIDTH / self.size))
        row = int(y // (WIN_HEIGHT / self.size))
        if not self.field[row][col]:
            self.field[row][col] = 1 + self.turn % 2
            self.turn += 1

    def start(self):
        """Create start parameters."""
        self.field = [[0] * self.size for _ in range(self.size)]
        self.turn = 0
        self.game_over = False
        self.write_message = True
        self.surface.fill(TicTac.background_color)
        pygame.display.update()

    def draw_x(self, x, y, color):
        """Draw x on screen."""
        pygame.draw.line(self.surface, color, (x + 2, y + 2),
                         (x + WIN_WIDTH / self.size - 2,
                          y + WIN_HEIGHT / self.size - 2), 10)
        pygame.draw.line(self.surface, color,
                         (x + 2, y + WIN_HEIGHT / self.size - 2),
                         (x + WIN_WIDTH / self.size - 2, y + 2), 10)

    def draw_o(self, x, y, color):
        """Draw o on screen."""
        pygame.draw.circle(self.surface, color,
                           (x + (WIN_WIDTH / self.size) // 2,
                            y + (WIN_HEIGHT / self.size) // 2),
                           (min(WIN_WIDTH, WIN_HEIGHT) / self.size)
                           // 2 - 3, 10)

    def game_loop(self):
        """Operate main Loop."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_click()
                if not self.write_message:
                    if event.type == pygame.KEYDOWN and \
                            event.key == pygame.K_SPACE:
                        self.start()
                if event.type == pygame.KEYDOWN and \
                        event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if not self.game_over:
                for row in range(self.size):
                    for col in range(self.size):
                        x = col * (WIN_WIDTH / self.size)
                        y = row * (WIN_HEIGHT / self.size)
                        if self.field[row][col] == 1:
                            self.draw_x(x, y, TicTac.tictac_color)
                        elif self.field[row][col] == 2:
                            self.draw_o(x, y, TicTac.tictac_color)
                self.game_over = TicTac.check_winner(self.field,
                                                     self.turn, self.size)
                pygame.display.update()
            elif self.write_message:
                self.surface.fill(TicTac.end_color)
                font = pygame.font.SysFont('arial', TicTac.srif_size)
                next_text = "Press Space to restart or ESC to leave"
                if self.game_over == 1:
                    text = "First player wins"
                elif self.game_over == 2:
                    text = "Second player wins"
                elif self.game_over == 3:
                    text = "Draw"
                text = font.render(text, True, TicTac.end_text_color)
                next_text = font.render(next_text, True,
                                        TicTac.end_text_color)
                self.surface.blit(text, (WIN_WIDTH * 0.1, WIN_HEIGHT * 0.3))
                self.surface.blit(next_text, (WIN_WIDTH * 0.1, WIN_HEIGHT * 0.3
                                              + TicTac.srif_size))
                self.write_message = False
                pygame.display.update()


def run_game(size):
    pygame.font.init()
    sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    TicTac(sc, size)


if __name__ == "__main__":
    size = input("Input width from 3 to 6 of your tictac " +
                 "field or press Enter for choosing default: ")
    if not size.isdigit() or size < "3":
        size = 3
    elif size > "6":
        size = 6
    size = int(size)
    run_game(size)
