import pygame


class UI(object):
    def __init__(self):
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.BLUE = (0, 0, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.SIZE = [500, 500]

    @staticmethod
    def display_loop(self):
        done = False
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode(self.SIZE)
        pygame.display.set_caption("Chess of all time")

        pygame.init()
        while not done:
            clock.tick(10)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            screen.fill(self.WHITE)

            pygame.display.flip()
        pygame.quit()
