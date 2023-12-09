import random
import time
import pyxel

from Player import Player
from ScreenBoomerang import ScreenBoomerang
from screen.Screen import Screen
from GameObjects.Platform import Platform
from GameObjects.pow import Pow
from GameObjects.Collision import check_collision
from GameObjects.Collision import check_collision_above
from enemy.crabs import Crabs
from enemy.turtle import Turtle
from enemy.flie import Flies
from GameObjects.coin import Coin

class GameScreen(Screen):
   """"This class describes ... """
   def __init__(self):
       Screen.__init__(self)
       self.player = None
       self.pow = None
       self.platforms = []
       self.objects = []
       self.__set_up()


   def __set_up(self):
       """This method sets up all of the objects on a screen"""
       pl = [Platform(0, 165, 10, 240, 6),Platform(0 * 240 / 160, 90, 6, 30 * 240 / 160, 6),Platform(0, 125, 6, 90, 6), Platform(155, 125, 6, 100, 6), Platform(130 * 240 / 160, 90, 6, 30 * 240 / 160, 6),Platform(50 * 240 / 160, 87, 6, 60 * 240 / 160, 6),Platform(0 * 240 / 160, 45, 7, 65 * 240 / 160, 6),Platform(100 * 240 / 160, 45, 7, 65 * 240 / 160, 6)
]
       self.platforms = pl
       obj = Player(120, 10, 15, 15,self.platforms)
       self.player = obj
       botton = Pow(115, 105, 15, 15)
       self.pow = botton

       self.add_object(Crabs(50, 100, 16, 16))
       self.add_object(Turtle(100, 150, 16, 16))
       self.add_object(Flies(75, 50, 16, 16))
       self.add_object(Coin(120, 100, 8, 8))

   def update(self, boomerang):
       #из-за этой функции наш игрок двигается тк мы обновляем экран
       if self.player is not None:
           boomerang = ScreenBoomerang()
           self.player.update(boomerang)

       if self.objects is not None:
           for obj in self.objects:
               boomerang = ScreenBoomerang()
               obj.update(boomerang)

       #из-за этой функции игрок ходит по платформам и падает когда их нет

       if self.platforms is not None:
           for platform in self.platforms:
               platform.update(boomerang)
               if check_collision_above(self.player, self.pow) and self.pow != None:
                   if self.pow.count > 0:
                       self.pow.count -= 1

               if check_collision(self.player, platform):
                   self.player.y = platform.y-self.player.height - 16

               elif self.player.up:
                   if self.player.y <= self.player.initial or check_collision_above(self.player, platform) or (self.pow != None and check_collision_above(self.player, self.pow)):
                       self.player.up = False
                       #не работает для средней платформы
                   self.player.y -= 0.5

               elif not check_collision(self.player, platform) and not self.player.up:
                   self.player.y += 0.5

       """for touch in range(self.pow.count):
           if """

   def draw(self):
       """This method draws a Game Screen"""
       pyxel.cls(0)
       for platform in self.platforms:
           platform.draw()
       self.player.draw()
       if self.pow.count != 0:
            self.pow.draw()
       for obj in self.objects:
           obj.draw()

   def get_instance(self, next_screen):
       """This method sets next screen and return the current one (game over screen)"""
       game_screen = GameScreen()
       game_screen.next_screen = next_screen
       return game_screen

   def add_object(self, obj):
       self.objects.append(obj)