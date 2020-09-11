from classes.game.game import Game

def play():
    game = Game()
    game.setUp()
    game.mainloop()

if __name__ == "__main__":
    play()