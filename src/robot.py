import pygame
import numpy as np

class Robot:
    def __init__(self, x, y):
        self.position = np.array([x, y], dtype=float)
        self.color = (0, 255, 0)
        self.size = 5

    def move(self, velocity):
        self.position += velocity

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position[0]), int(self.position[1])), self.size)
