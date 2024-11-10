import pygame
import numpy as np

class Obstacle:
    def __init__(self, x, y, width, height):
        self.position = np.array([x, y])
        self.width = width
        self.height = height
        self.color = (255, 0, 0)  # Color rojo para los obstáculos

    def draw(self, screen):
        """Dibuja el obstáculo en la pantalla."""
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], self.width, self.height))

    def is_colliding(self, position):
        """Verifica si una posición dada está dentro del obstáculo."""
        return (self.position[0] <= position[0] <= self.position[0] + self.width and
                self.position[1] <= position[1] <= self.position[1] + self.height)
