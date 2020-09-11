from PIL.ImageChops import screen
import pygame
from config import *

class Paddle:
    def __init__(self, x, y, width, height, color):
        self.image = pygame.Surface((width, height), pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.image.fill(color)
        self.image.convert_alpha()

        self.rect.left = x
        self.rect.top = y

        self.movementDirs = [0, 0]
        self.speed = 8
        self.color = color

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def boundsCheck(self):
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH


    def update(self, screen):
        self.rect = self.rect.move(self.movementDirs)
        self.boundsCheck()
        self.draw(screen)