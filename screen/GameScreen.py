import random
import time
import pyxel

from Player import Player
from ScreenBoomerang import ScreenBoomerang
from screen.Screen import Screen

class GameScreen(Screen):
    """"This class describes ... """
    def __init__(self):
        Screen.__init__(self)
        self.player = None
        self.__set_up()

    def __set_up(self):
        """This method sets up all of the objects on a screen"""

        # creating a player
        obj = Player(120, 60, 5, 5)
        self.player = obj

    def update(self, boomerang):

        if self.player is not None:
            boomerang = ScreenBoomerang()
            self.player.update(boomerang)
        """if pyxel.btn(pyxel.KEY_MINUS):
            boomerang.screen = self.next_screen.get_instance(self.next_screen.next_screen)"""

    def draw(self):
        """This method draws a Game Screen"""
        pyxel.cls(0)
        """pyxel.rect(0, 0, pyxel.width, 40, 0)"""
        self.player.draw()

    def get_instance(self, next_screen):
        """This method sets next screen and return the current one (game over screen)"""
        game_screen = GameScreen()
        game_screen.next_screen = next_screen
        return game_screen
