import pygame
from config import *

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.run = True         # if False game ends
    
    def setUp(self):
        self.screen.fill(WHITE)
        print("umm hello?")

    def mainloop(self):
        while self.run:
            self.events()
            pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
