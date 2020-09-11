import pygame
from classes.paddle import Paddle
from classes.ball import Ball
from config import *

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.run = True         # if False game ends

    def setUp(self):
        # game objs
        self.paddle = Paddle(WIDTH - int(WIDTH/2) - 50, HEIGHT - int(HEIGHT/4), int(WIDTH*60/400), int(HEIGHT/60), BLUE)
        self.ball = Ball(int(WIDTH/2), int(HEIGHT - HEIGHT/3), int(WIDTH/40),RED, [3, 4])
        self.screen.fill(WHITE)
        pygame.display.update()
       # print("umm hello?")

    def mainloop(self):
        while self.run:
            self.events()
            self.screen.fill(WHITE)
            self.paddle.update(self.screen)
            self.ball.update(self.screen)


    def controls(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                # Horizontal movement
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.paddle.movementDirs[0] = -1 * self.paddle.speed
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.paddle.movementDirs[0] = self.paddle.speed
                # Vertical movement
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.paddle.movementDirs[1] = -1 * self.paddle.speed
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.paddle.movementDirs[1] = self.paddle.speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.paddle.movementDirs[0] = 0
                if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.paddle.movementDirs[1] = 0
    
    def collisionDetection(self):
        if pygame.sprite.collide_mask(self.paddle, self.ball):
            self.ball.movementDirs[0] -= self.paddle.movementDirs[0]
            self.ball.movementDirs[1] = -1 * self.ball.movementDirs[1]  

    def events(self):
        self.clock.tick(FPS)
        self.controls()
        self.collisionDetection()  
        pygame.display.update()
               
            