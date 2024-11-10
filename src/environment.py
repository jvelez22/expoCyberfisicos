import pygame

class Environment:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("PSO Robot Exploration")
        self.clock = pygame.time.Clock()
        self.background_color = (0, 0, 0)

    def update(self):
        pygame.display.flip()
        self.screen.fill(self.background_color)
        self.clock.tick(60)

    def close(self):
        pygame.quit()
