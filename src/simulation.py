import pygame
import numpy as np
import pyswarms as ps
from robot import Robot
from environment import Environment

class Simulation:
    def __init__(self, n_robots=10):
        self.env = Environment()
        self.robots = [Robot(np.random.randint(100, 700), np.random.randint(100, 500)) for _ in range(n_robots)]
        self.positions = np.array([robot.position for robot in self.robots])
        
        # Inicializar `best_position` a un valor válido dentro del entorno
        self.best_position = np.array([self.env.width / 2, self.env.height / 2])
        
    def objective_function(self, positions):
        if self.best_position is None:
            raise ValueError("best_position no ha sido inicializado correctamente")
        distances = np.linalg.norm(positions - self.best_position, axis=1)
        return distances


    def optimize(self):
        optimizer = ps.single.GlobalBestPSO(
            n_particles=len(self.robots),
            dimensions=2,
            options={'c1': 0.5, 'c2': 0.3, 'w': 0.9},
            bounds=(np.zeros(2), np.array([self.env.width, self.env.height]))
        )
        best_cost, best_position = optimizer.optimize(self.objective_function, iters=100)
        self.best_position = best_position

    def run(self):
        running = True
        self.optimize()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.env.update()

            for robot in self.robots:
                robot.move(np.random.uniform(-1, 1, 2))
                robot.draw(self.env.screen)

        self.env.close()
