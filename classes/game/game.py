import pygame
from classes.game.paddle import Paddle
from classes.game.ball import Ball
from classes.game.block import Block 
from classes.effects.dust import Dust
from tkinter import *
from tkinter import messagebox

from config import *
pygame.mixer.init()

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.run = True         # if False game ends
        self.blocks = []
        self.lives = 5
        self.score = 0
        self.font = pygame.font.SysFont("comicsans", 30)
        self.dust = []          # dust contains particles
        self.dustSpread = False # tells program if it should draw particles
        self.levelCounter = 1
        # 0 Brick 1 Paddle
        self.sounds = [pygame.mixer.Sound("music/Brickbreak1.wav"), pygame.mixer.Sound("music/PaddleBounce1.wav")]   
        
        
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

        self.explosion = Dust((self.ball.rect.left, self.ball.rect.top))

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
            self.sounds[1].play()
        # for blocks
        for block in self.blocks:
            if pygame.sprite.collide_mask(self.ball, block):
                '''well it was actually fun with this mistake'''
              #  self.ball.movementDirs[0] -= self.paddle.movementDirs[0]
                self.ball.movementDirs[1] = -1 * self.ball.movementDirs[1]
                self.ball.movementDirs[0] = -1 * self.ball.movementDirs[0]
                self.blocks.remove(block)
                self.sounds[0].play()
                ballDestrPos = (self.ball.rect.left, self.ball.rect.top)
                self.createDust(ballDestrPos)
                self.score += 1

    # all stuff for game drawing & mechanicks        
    def events(self):
        self.update()
        self.controls()
        self.collisionDetection()
        self.drawScore()
        self.drawLives()
        if self.dustSpread == True:
            self.drawBlockExplosion()

        self.checkIfDecreaseLP()
        self.checkLives()
        if self.isClear():
            self.newLevel()

        pygame.display.update()  

    def newLevel(self):
        Tk().withdraw()  # it will hides normal tkinter window
        self.levelCounter += 1
        messagebox.showinfo("level compleated", f"you will now enter level {self.levelCounter} !!!")
        self.gainLife()
        self.setUp()

    # checking winning condition
    def isClear(self):
        if self.blocks == []:
            return True
        return False

    # checking loosing condition
    def checkLives(self):
        if self.lives <= 0:
            Tk().withdraw()
            messagebox.showinfo("Out of lives", "You will do better next time :D\nBack to main menu")
            self.run = False

    def drawLives(self):
        if self.lives < 2:
            livesLabel = self.font.render(f"Lives: {self.lives}",1, RED)
        else:
            livesLabel = self.font.render(f"Lives: {self.lives}",1, BLACK)
        
        self.screen.blit(livesLabel, (int(livesLabel.get_width()/10), 10))

    # checking position of the ball 
    def checkIfDecreaseLP(self):
        if self.ball.rect.bottom >= HEIGHT:
            self.looseLife()

    # kinda creepy
    def looseLife(self):
        self.lives -= 1
    
    # if you complete tje lvl
    def gainLife(self):
        self.lives += 1

               
    def drawScore(self):
        self.scoreLabel = self.font.render(f"Score: {self.score}", 1, BLACK)
        self.screen.blit(self.scoreLabel, (WIDTH - self.scoreLabel.get_width() - 10, 10))

    def createDust(self, pos):
        d= Dust(pos)
        self.dust.append(d)
        self.dustSpread = True
        

    def drawBlockExplosion(self):
        
        for d in self.dust:
            d.draw(self.screen)
            d.update()

        if self.dust == []:
            self.dustSpread = False



            