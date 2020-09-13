import pygame
from classes.game.paddle import Paddle
from classes.game.ball import Ball
from classes.game.block import Block 
from classes.gui.button import Button 
from config import *

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.run = True         # if False game ends
        self.blocks = []
        self.score = 0
        self.font = pygame.font.SysFont("comicsans", 30)
        
    # creating game objects    
    def setUp(self):
        # game objs
        self.paddle = Paddle(WIDTH - int(WIDTH/2) - 50, HEIGHT - int(HEIGHT/4), int(WIDTH*60/400), int(HEIGHT/60), BLUE)
        self.ball = Ball(int(WIDTH/2), int(HEIGHT - HEIGHT/3), int(WIDTH/40),RED, [3, 4])
        
        BLOCK_WIDTH = int(WIDTH/8)
        BLOCK_HEIGHT =int(BLOCK_WIDTH/2)
        # BLOCKS
        for y in range(3):
            for x in range(10, int(WIDTH), int(BLOCK_WIDTH) + 10):
                self.blocks.append(Block(x, BLOCK_HEIGHT * (y + 1) + 2, int(WIDTH*35/400), int(HEIGHT*22/400), GREEN))

        self.screen.fill(WHITE)
        pygame.display.update()
       # print("umm hello?")

    # function to call after setUp
    def mainloop(self):
        while self.run:
            self.clock.tick(FPS)
            self.events()
            pygame.display.update()
            
    # Redrawing all objects in game
    def update(self):
        self.screen.fill(WHITE)
        self.drawScore()
        self.paddle.update(self.screen)
        for block in self.blocks:
            block.draw(self.screen)
        self.ball.update(self.screen)

    # for paddle movement 
    def controls(self):

        for event in pygame.event.get():
            # Menu buttons
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

            pygame.display.update()

    
    def collisionDetection(self):
        # for paddle
        if pygame.sprite.collide_mask(self.paddle, self.ball):
            self.ball.movementDirs[0] -= self.paddle.movementDirs[0]
            self.ball.movementDirs[1] = -1 * self.ball.movementDirs[1]
        # for blocks
        for block in self.blocks:
            if pygame.sprite.collide_mask(self.ball, block):
                '''well it was actually fun with this mistake'''
              #  self.ball.movementDirs[0] -= self.paddle.movementDirs[0]
                self.ball.movementDirs[1] = -1 * self.ball.movementDirs[1]
                self.ball.movementDirs[0] = -1 * self.ball.movementDirs[0]
                self.blocks.remove(block)
                self.score += 1

    # all stuff for game drawing & mechanicks        
    def events(self):
        self.update()
        self.controls()
        self.collisionDetection()
        self.drawScore()
        pygame.display.update()  

               
    def drawScore(self):
        self.scoreLabel = self.font.render(f"Score: {self.score}", 1, BLACK)
        self.screen.blit(self.scoreLabel, (WIDTH- self.scoreLabel.get_width() - 10, 10))

            