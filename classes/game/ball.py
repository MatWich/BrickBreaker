import pygame
from config import *
from classes.game.dust import Dust 

class Ball:
    def __init__(self, x, y, size, color, movementDirs=[0, 0]):
        self.image = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        pygame.draw.circle(self.image, color, (int(self.rect.width/2), int(self.rect.height/2)), int(size/2))

        self.maxSpeed = 10
        self.movementDirs = movementDirs
        self.color = color

    def update(self, screen):
        self.move()
        self.rect = self.rect.move(self.movementDirs)
        self.boundsCheck()
        self.draw(screen)

    def move(self):
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.movementDirs[1] = -1 * self.movementDirs[1]
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.movementDirs[0] = -1 * self.movementDirs[0]


        # paddle will be able to change ball velocity 
        if self.movementDirs[1] > self.maxSpeed:
            self.movementDirs[1] = self.maxSpeed - 1
        
        if self.movementDirs[0] > self.maxSpeed:
            self.movementDirs[0] = self.maxSpeed -1 

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
