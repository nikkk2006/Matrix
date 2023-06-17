import pygame


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
        self.surface = pygame.Surface((self.WIDTH, self.HEIGHT))

        # время
        self.clock = pygame.time.Clock()

    def draw(self):
        """Отрисовка экрана"""

        self.surface.fill(pygame.Color("black"))
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