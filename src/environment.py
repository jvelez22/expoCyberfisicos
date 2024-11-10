import pygame
from obstacle import Obstacle

class Environment:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("PSO Robot Exploration with Obstacles")
        self.clock = pygame.time.Clock()
        self.background_color = (0, 0, 0)
        
        # Lista de obstáculos
        self.obstacles = [
            Obstacle(200, 150, 100, 50),
            Obstacle(400, 300, 150, 50),
            Obstacle(600, 450, 50, 100)
        ]

    def update(self):
        """Actualiza la pantalla y dibuja los obstáculos."""
        pygame.display.flip()
        self.screen.fill(self.background_color)
        for obstacle in self.obstacles:
            obstacle.draw(self.screen)
        self.clock.tick(60)

    def close(self):
        """Cierra la ventana de Pygame."""
        pygame.quit()
