import random
import time
import pyxel

from Player import Player
from ScreenBoomerang import ScreenBoomerang
from screen.Screen import Screen
from GameObjects.Platform import Platform
from GameObjects.pow import Pow
from GameObjects.Collision import check_collision
from GameObjects.Collision import check_collision_enemy
from GameObjects.Collision import check_collision_above
from enemy.crabs import Crabs
from enemy.turtle import Turtle
from enemy.flie import Flies
from GameObjects.coin import Coin
from GameObjects.pipes import Pipes

class GameScreen(Screen):
   """"This class describes ... """
   def __init__(self):
       """Screen.__init__(self)"""
       self.player = None
       self.pow = None
       self.platforms = []
       self.objects = []
       self.enemies = []
       self.__set_up()
       Screen.__init__(self)


   def __set_up(self):
       """This method sets up all of the objects on a screen"""
       if len(self.platforms) == 0:
            pl = [Platform(0, 165, 10, 240, 6),Platform(0 * 240 / 160, 90, 6, 30 * 240 / 160, 6),Platform(0, 125, 6, 90, 6), Platform(155, 125, 6, 100, 6), Platform(130 * 240 / 160, 90, 6, 30 * 240 / 160, 6),Platform(50 * 240 / 160, 87, 6, 60 * 240 / 160, 6),Platform(0 * 240 / 160, 45, 7, 65 * 240 / 160, 6),Platform(100 * 240 / 160, 45, 7, 65 * 240 / 160, 6)
]
            self.platforms = pl

       if self.player is None:
            obj = Player(120, 10, 15, 15,self.platforms)
            self.player = obj

       buttom = Pow(115, 105, 15, 15)
       self.add_object(buttom)

       pipes = Pipes(0, 20, 48, 24)
       self.add_object(pipes)

       turtle = Turtle(240, 25, 16, 16)
       flie = Flies(240, 25, 16, 16)
       crab = Crabs(60, 25, 16, 16)

       self.add_enemy(turtle)
       self.add_enemy(flie)
       self.add_enemy(crab)


   def update(self, boomerang):
       #из-за этой функции наш игрок двигается тк мы обновляем экран
       if self.player is not None:
           boomerang = ScreenBoomerang()
           self.player.update(boomerang)

       for enemy in self.enemies:
            boomerang = ScreenBoomerang()
            enemy.update(boomerang)
            if (enemy.x >= 223 or enemy.x <= 1) and (enemy.y >= 150.75):
                enemy.y = 25
                """self.__set_up()"""

            for platform in self.platforms:
                """if platform.y == 45:
                    print("round(obj.y) + obj.height + 14",round(obj.y) + obj.height)
                    print("platform.y - 1",platform.y -1)"""

                if check_collision_enemy(enemy, platform):
                    enemy.y = platform.y - enemy.height
                if not check_collision_enemy(enemy, platform):
                    enemy.y += 0.25


       #из-за этой функции игрок ходит по платформам и падает когда их нет
       if len(self.objects) != 0 and type(self.objects[0]) == type(Pow(115, 105, 15, 15)):
           if check_collision_above(self.player, self.objects[0]):
               if self.objects[0].count > 0:
                   self.objects[0].count -= 1
               else:
                   self.remove_object(self.objects[0])

       if self.platforms is not None:
           for platform in self.platforms:
               if check_collision(self.player, platform):
                   self.player.y = platform.y-self.player.height - 16

               elif self.player.up:
                   if self.player.y <= self.player.initial or check_collision_above(self.player, platform) or (self.pow != None and check_collision_above(self.player, self.pow)):
                       self.player.up = False
                       #не работает для средней платформы
                   self.player.y -= 0.5

               elif not check_collision(self.player, platform) and not self.player.up:
                   self.player.y += 0.5

   def draw(self):
       """This method draws a Game Screen"""
       self.player.draw()
       """if self.pow.count != 0:
            self.pow.draw()"""
       for enemy in self.enemies:
           enemy.draw()
       for obj in self.objects:
          obj.draw()

   def get_instance(self, next_screen):
       """This method sets next screen and return the current one (game over screen)"""
       game_screen = GameScreen()
       game_screen.next_screen = next_screen
       return game_screen

   def add_object(self, obj):
       self.objects.append(obj)

   def remove_object(self, obj):
       self.objects.remove(obj)

   def add_enemy(self, enemy):
       self.enemies.append(enemy)

   def remove_enemy(self, enemy):
       self.enemies.remove(enemy)