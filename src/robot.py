import pygame
import numpy as np

class Robot:
    def __init__(self, x, y):
        self.position = np.array([x, y], dtype=float)
        self.color = (0, 255, 0)
        self.size = 5

    def move(self, velocity, obstacles):
        """Actualiza la posición del robot, evitando colisiones con obstáculos."""
        new_position = self.position + velocity
        for obstacle in obstacles:
            if obstacle.is_colliding(new_position):
                return  # No moverse si hay colisión
        self.position = new_position

    def draw(self, screen):
        """Dibuja el robot en la pantalla."""
        pygame.draw.circle(screen, self.color, (int(self.position[0]), int(self.position[1])), self.size)
