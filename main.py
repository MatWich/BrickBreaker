from classes.gui.menu import Menu
import pygame
pygame.init()

def menu():
    menu = Menu()
    menu.drawMenu()

if __name__ == "__main__":
    menu() 