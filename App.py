import pyxel
from ScreenBoomerang import AppBoomerang
from screen.GameScreen import GameScreen

class App:
    """This class is used to store the whole app"""
    def __init__(self, curr_screen, height, width):
        self.height = height
        self.width = width
        pyxel.init(self.height, self.width)
        self.curr_screen = curr_screen

        game_screen = GameScreen()
        self.platforms = game_screen.platforms

    def update(self):
        """This method updates screens of a game"""
        boomerang = AppBoomerang()
        self.curr_screen.update(boomerang)
        next_screen = boomerang.screen

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        elif next_screen is not None:
            self.curr_screen = next_screen

    def draw(self):
        """This method draws current screen"""
        pyxel.cls(0)
        for platform in self.platforms:
            platform.draw()
        self.curr_screen.draw()

    def run(self):
        pyxel.run(self.update, self.draw)
