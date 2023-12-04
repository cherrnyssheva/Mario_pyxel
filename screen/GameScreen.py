
import random
import time
import pyxel


from Player import Player
from ScreenBoomerang import ScreenBoomerang
from screen.Screen import Screen
from GameObjects.Platform import Platform
from GameObjects.Collision import check_collision
from GameObjects.Collision import check_collision_above


class GameScreen(Screen):
   """"This class describes ... """
   def __init__(self):
       Screen.__init__(self)
       self.player = None
       self.platforms = []
       self.jump_count = 0
       self.is_ground = True
       self.__set_up()


   def __set_up(self):
       """This method sets up all of the objects on a screen"""


       # creating a player

       obj = Player(120, 10, 5, 5, self.is_ground)
       self.player = obj
       pl = [Platform(0, 111, 9, 160, 4), Platform(0, 85, 5, 60, 6), Platform(100, 85, 5, 60, 6),
             Platform(0, 63, 5, 30, 6), Platform(130, 63, 5, 30, 6), Platform(50, 58, 5, 60, 6),
             Platform(0, 30, 5, 65, 6), Platform(100, 30, 5, 65, 6)]
       self.platforms = pl
   def update(self, boomerang):
       #из-за этой функции наш игрок двигается тк мы обновляем экран
       if self.player is not None:
           boomerang = ScreenBoomerang()
           self.player.update(boomerang)
       #из-за этой функции игрок ходит по платформам и падает когда их нет
       if self.platforms is not None:
           for platform in self.platforms:
               platform.update(boomerang)
               if check_collision(self.player, platform):
                   self.player.y = platform.y-6
                   self.is_ground = True
               else:
                   self.player.y += 0.4
                   self.is_ground = False


       """if pyxel.btn(pyxel.KEY_MINUS):
           boomerang.screen = self.next_screen.get_instance(self.next_screen.next_screen)"""


   def draw(self):
       """This method draws a Game Screen"""
       pyxel.cls(0)
       for platform in self.platforms:
           platform.draw()
       self.player.draw()


   def get_instance(self, next_screen):
       """This method sets next screen and return the current one (game over screen)"""
       game_screen = GameScreen()
       game_screen.next_screen = next_screen
       return game_screen

