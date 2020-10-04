import pygame
from config import *
from classes.gui.button import Button
from classes.game.game import Game
from classes.effects.dust import Dust
from classes.db.database import Database

class Menu:
    def __init__(self):
        self.run = True
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(TITLE)
        ICON_IMG = pygame.image.load("imgs/Ikonka.png")
        pygame.display.set_icon(ICON_IMG)
        self.clock = pygame.time.Clock()
        self.buttons = []
        self.font = pygame.font.SysFont("arial", 60)
        self.infoFont = pygame.font.SysFont("comicsans", 30)
        self.dust = []

    # Creating Menu buttons
    def setUp(self):
        self.db = Database()

        for y in range(0, 4):
            self.startButton = Button(int(WIDTH/2) - int(BTN_WIDTH/2), int(HEIGHT*100/400) + 0 * (BTN_HEIGHT + BTN_OFFSET), BTN_WIDTH, BTN_HEIGHT, GREEN, "START")
            self.controlsButton = Button(int(WIDTH/2) - int(BTN_WIDTH/2), int(HEIGHT*100/400) + 1 * (BTN_HEIGHT + BTN_OFFSET), BTN_WIDTH, BTN_HEIGHT, GREEN, "Controls")
            self.highscoreButton = Button(int(WIDTH/2) - int(BTN_WIDTH/2), int(HEIGHT*100/400) + 2 * (BTN_HEIGHT + BTN_OFFSET), BTN_WIDTH, BTN_HEIGHT, GREEN, "Scores")
            self.quitButton = Button(int(WIDTH/2) - int(BTN_WIDTH/2), int(HEIGHT*100/400) + 3 * (BTN_HEIGHT + BTN_OFFSET), BTN_WIDTH, BTN_HEIGHT, GREEN, "QUIT")

        self.buttons.append(self.startButton)
        self.buttons.append(self.quitButton)
        self.buttons.append(self.highscoreButton)
        self.buttons.append(self.controlsButton)


    # To start the game when exit go back to menu
    def playGame(self):
        self.game = Game(self.screen)
        self.game.setUp()
        self.game.mainloop()

    """Menu"""
    # Menu Tops
    def tops(self):
        self.topsLabel = self.font.render(MENU_LABEL, 1, BLACK)
        self.screen.blit(self.topsLabel, (int(WIDTH/2) - int(self.topsLabel.get_width()/2) - 10, 10))


    def drawBg(self):
        self.screen.fill(LIGHT_YELLOW)

    # method to call in main()
    def drawMenu(self):
        self.setUp()
        while self.run:
            self.clock.tick(FPS)
            self.drawBg()
            self.tops()
            self.drawButtons()
            self.controls()
            self.drawDust()
            pygame.display.update()

    # Displaying All Buttons
    def drawButtons(self):
        for button in self.buttons:
            button.draw(self.screen)

    # Menu controls
    def controls(self):
        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

            # On clicks for buttons
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    d= Dust(pygame.mouse.get_pos())
                    self.dust.append(d)

                
                # Buttons onclicks
                if self.startButton.isOver(pos):
                    self.playGame()        

                if self.quitButton.isOver(pos):
                    self.run = False

                if self.highscoreButton.isOver(pos):
                    self.highScores()
            
                if self.controlsButton.isOver(pos):
                    self.controlsPage()
            # for button to highlight
            if event.type == pygame.MOUSEMOTION:
                for button in self.buttons:
                    if button.isOver(pos):
                        button.highLight()
                    else:
                        button.deHighLight()
        

    
    """Controls"""
    def controlsPage(self):
        while self.run:
            self.clock.tick(FPS)
            self.drawBg()
            self.drawContorlsTops()
            self.drawControlsPageContent()
            self.highScoresControl()       # "don't repeat yourself"
            pygame.display.update()


    def drawContorlsTops(self):
        self.creditsTops = self.font.render(CONTROLS_LABEL, 1, BLACK)
        self.screen.blit(self.creditsTops, (int(WIDTH/2) - int(self.topsLabel.get_width()/2) - 10, 10) )

    def drawControlsPageContent(self):
        infoBar = self.infoFont.render(MOVEMENT_INFO, 1, BLACK)
        infoBar2 = self.infoFont.render(SOME_MORE_TEXT_TO_CONTOROLS, 1, BLACK)
        self.screen.blit(infoBar, (int(WIDTH/2) - int(infoBar.get_width()/2) - 50, int(HEIGHT*100/400)) )
        self.screen.blit(infoBar2, (int(WIDTH/2) - int(infoBar2.get_width()/2) - 50, int(HEIGHT*150/400)) )
        
    
    """HighScores"""
    # Highscores Menu Options
    def highScores(self):
        while self.run:
            self.clock.tick(FPS)
            self.drawBg()
            self.drawHighScoresTops()
            self.createHighScores()
            self.drawHighScores()
            self.highScoresControl()
            pygame.display.update()
    
    # highscores Tops
    def drawHighScoresTops(self):
        self.highScorestops = self.font.render(HIGHSCORE_LABEL, 1, BLACK)
        self.screen.blit(self.highScorestops, (int(WIDTH/2) - int(self.highScorestops.get_width()/2) - 10, 10) )

    # contorls for highscores option
    def highScoresControl(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.drawMenu()

    def createHighScores(self):
        self.db.update()
        highscores = self.db.loopfor10()
        self.texts = []
        for info in highscores:
            print(info["pName"], info["score"])
            text = info["pName"] + " scored" + ":   " + str(info["score"])
            self.texts.append(text)
        
    def drawHighScores(self):
        counter = 1
        infoStr = "PLAYER       SCORE"
        line = self.infoFont.render(infoStr, 1, BLACK)
        self.screen.blit(line, (int(WIDTH/2) - int(line.get_width()/2) - 50, int(HEIGHT*80/400) ))

        for text in self.texts:
            line = self.infoFont.render(text, 1, BLACK)
            self.screen.blit(line, (int(WIDTH/2) - int(line.get_width()/2) - 50, int(HEIGHT*100/400 + 25 * counter) ))
            counter+= 1
    


    def drawDust(self):
        for d in self.dust:
            d.draw(self.screen)
            d.update()
        