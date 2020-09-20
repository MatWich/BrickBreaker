import pygame
from config import *
from classes.effects.particle import Particle

class Dust:
    def __init__(self, pos):
        self.pos = pos
        self.particles = [Particle(self.pos) for i in range(PARTICLE_AMOUNT)]

    def draw(self, screen):
        for p in self.particles:
            p.draw(screen)

    def update(self):
        for p in self.particles:
            p.update()
            if p.radius <= 0:
                self.particles.remove(p)