import pygame
from config import *
from classes.gui.button import Button
from classes.game.game import Game

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

    # Creating Menu buttons
    def setUp(self):
        for y in range(0, 4):
            self.startButton = Button(int(WIDTH/2) - int(BTN_WIDTH/2), int(HEIGHT*100/400) + 0 * (BTN_HEIGHT + BTN_OFFSET), BTN_WIDTH, BTN_HEIGHT, GREEN, "START")
            self.creditsButton = Button(int(WIDTH/2) - int(BTN_WIDTH/2), int(HEIGHT*100/400) + 1 * (BTN_HEIGHT + BTN_OFFSET), BTN_WIDTH, BTN_HEIGHT, GREEN, "Credits")
            self.controlsButton = Button(int(WIDTH/2) - int(BTN_WIDTH/2), int(HEIGHT*100/400) + 2 * (BTN_HEIGHT + BTN_OFFSET), BTN_WIDTH, BTN_HEIGHT, GREEN, "Controls")
            self.quitButton = Button(int(WIDTH/2) - int(BTN_WIDTH/2), int(HEIGHT*100/400) + 3 * (BTN_HEIGHT + BTN_OFFSET), BTN_WIDTH, BTN_HEIGHT, GREEN, "QUIT")

        self.buttons.append(self.startButton)
        self.buttons.append(self.quitButton)
        self.buttons.append(self.creditsButton)
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
                if self.startButton.isOver(pos):
                    self.playGame()        

                if self.quitButton.isOver(pos):
                    self.run = False

                if self.creditsButton.isOver(pos):
                    self.credits()
            
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
            self.creditsControl()       # "don't repeat yourself"
            pygame.display.update()


    def drawContorlsTops(self):
        self.creditsTops = self.font.render(CONTROLS_LABEL, 1, BLACK)
        self.screen.blit(self.creditsTops, (int(WIDTH/2) - int(self.topsLabel.get_width()/2) - 10, 10) )

    def drawControlsPageContent(self):
        infoBar = self.infoFont.render(MOVEMENT_INFO, 1, BLACK)
        infoBar2 = self.infoFont.render(SOME_MORE_TEXT_TO_CONTOROLS, 1, BLACK)
        self.screen.blit(infoBar, (int(WIDTH/2) - int(infoBar.get_width()/2) - 50, int(HEIGHT*100/400)) )
        self.screen.blit(infoBar2, (int(WIDTH/2) - int(infoBar2.get_width()/2) - 50, int(HEIGHT*150/400)) )
        
    
    """Credits"""
    # Credits Menu Options
    def credits(self):
        while self.run:
            self.clock.tick(FPS)
            self.drawBg()
            self.drawCreditsTops()
            self.creditsControl()
            pygame.display.update()
    
    # Credits Tops
    def drawCreditsTops(self):
        self.creditsTops = self.font.render(CREDITS_LABEL, 1, BLACK)
        self.screen.blit(self.creditsTops, (int(WIDTH/2) - int(self.topsLabel.get_width()/2) - 10, 10) )

    # contorls for Credits option
    def creditsControl(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.drawMenu()

