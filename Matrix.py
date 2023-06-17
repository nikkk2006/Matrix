import pygame
import random


class MatrixSymbols:
    def __init__(self, app):
        self.app = app
        self.GREEN = (0, 255, 0)
        self.SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
        self.FONTSIZE = 15
        self.font = pygame.font.SysFont("arial", self.FONTSIZE, bold=True)

        # количество колонок
        self.columns = app.WIDTH // self.FONTSIZE
        self.drops = [1 for _ in range(0, self.columns)]

    def draw(self):
        for i in range(0, len(self.drops)):
            random_symbol = random.choice(self.SYMBOLS)

            # отрисовка символа
            char_render = self.font.render(random_symbol, False, self.GREEN)
            position = i * self.FONTSIZE, (self.drops[i] - 1) * self.FONTSIZE

            self.app.surface.blit(char_render, position)

            if self.drops[i] * self.FONTSIZE > app.HEIGHT and random.uniform(0, 1) > 0.975:
                self.drops[i] = 0
            self.drops[i] = self.drops[i] + 1



    def run(self):
        self.draw()

class Matrix:
    def __init__(self):
        """Инициализация приложения"""

        # размеры экрана
        self.WIDTH = 1000
        self.HEIGHT = 700

        # инициализация pygame
        pygame.init()

        # создание экрана
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.surface = pygame.Surface((self.WIDTH, self.HEIGHT), pygame.SRCALPHA)

        # время
        self.clock = pygame.time.Clock()

        # экземпляр класса MatrixLetters
        self.matrixLetters = MatrixSymbols(self)

    def draw(self):
        """Отрисовка экрана"""

        self.surface.fill((0, 0, 0, 10))
        self.matrixLetters.run()
        self.screen.blit(self.surface, (0, 0))

    def run(self):
        """Главный цикл программы"""

        while True:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            pygame.display.update()
            self.clock.tick(30)

if __name__ == '__main__':
    app = Matrix()
    app.run()