import pygame
import random
from config import *

class Particle:
    def __init__(self, pos):
        self.x, self.y = pos
        self.vx, self.vy = random.randint(-2, 2), random.randint(-10, 0)
        self.radius = 5

    def draw(self, screen):
        pygame.draw.circle(screen, PARTICLE_COLOR, (self.x, self.y), self.radius)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        if random.randint(0, 100) < 40:
            self.radius -= 1
            