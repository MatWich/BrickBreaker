import pygame

from config import *

class Block:
    def __init__(self, x, y, width, height, color):
        self.image = pygame.Surface((width, height), pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.image.fill(color)
        self.image.convert_alpha()

        self.rect.left = x
        self.rect.top = y
        self.color = color


    def draw(self, screen):
        screen.blit(self.image, self.rect)
    

