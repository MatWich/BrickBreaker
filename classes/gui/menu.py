import pygame
from config import *
from classes.gui.button import Button

class Menu:
    def __init__(self, screen):
        self.run = True
        self.screen = screen
        self.buttons = []

    def setUp(self):
        self.startButton = Button(WIDTH - int(WIDTH/3), HEIGHT - int(HEIGHT/3), 200, 25, GREEN, "START")
    
    def drawBg(self):
        self.screen.fill(WHITE)

    def drawMenu(self):
        self.setUp()
        while self.run:
            self.drawBg()
            self.drawButtons()

    def drawButtons(self):
        self.startButton.draw(self.screen)