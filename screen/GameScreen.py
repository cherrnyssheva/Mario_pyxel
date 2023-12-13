import time
import pyxel

from Player import Player
from ScreenBoomerang import ScreenBoomerang
from screen.Screen import Screen
from GameObjects.Platform import Platform
from GameObjects.pow import Pow
from GameObjects.Collision import check_collision
from GameObjects.Collision import check_collision_above
from GameObjects.Collision import check_left_right_collision
from GameObjects.Collision import check_left_right_collision_enemy
from GameObjects.Collision import check_collision_enemy
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
       self.coins = []
       self.rotated_enemies = []
       self.motion = True
       self.rotated = None
       self.health = 3
       self.score = 0
       self.current_time = time.time()
       self.is_player_dead = False
       self.__set_up()
       Screen.__init__(self)


   def __set_up(self):
       """This method sets up all of the objects on a screen"""
       if len(self.platforms) == 0:
            pl = [Platform(0, 165, 10, 240, 6),Platform(0 * 240 / 160, 90, 6, 30 * 240 / 160, 6),Platform(0, 125, 6, 90, 6), Platform(155, 125, 6, 100, 6), Platform(130 * 240 / 160, 90, 6, 30 * 240 / 160, 6),Platform(50 * 240 / 160, 87, 6, 60 * 240 / 160, 6),Platform(0 * 240 / 160, 45, 7, 65 * 240 / 160, 6),Platform(100 * 240 / 160, 45, 7, 65 * 240 / 160, 6)
]
            self.platforms = pl

       if self.player is None:
            obj = Player(120, 10, self.platforms)
            self.player = obj

       button = Pow(115, 105, 15, 15)
       self.add_object(button)

       coins = [Coin(40, 60, 8, 16), Coin(165, 60, 8, 16), Coin(65, 100, 8, 16), Coin(95, 100, 8, 16),
                Coin(95, 20, 8, 16), Coin(165, 140, 8, 16), Coin(83, 140, 8, 16)]
       self.coins = coins

       pipes = Pipes(0, 20, 48, 24)
       self.add_object(pipes)

       turtle = Turtle(240, 25, 16, 16)
       flie = Flies(240, 25, 16, 16)
       crab = Crabs(60, 25, 16, 16)

       self.add_enemy(turtle)
       self.add_enemy(flie)
       self.add_enemy(crab)


   def update(self, boomerang):

       # завершения игры если игрок умирает, переключение экрана
       if self.is_game_over():
           self.is_player_dead = False
           tmp_screen = self.next_screen.get_instance(self.next_screen.next_screen)
           tmp_screen.set_score(self.score)
           boomerang.screen = tmp_screen

       #обновление движения игрока
       if self.player is not None:
           boomerang = ScreenBoomerang()
           self.player.update(boomerang)

       # коллизия игрока с платформами
       if self.platforms is not None:
           for platform in self.platforms:
               if check_collision(self.player, platform):
                   self.player.y = platform.y-self.player.height - 16

               # логика прыжка игрока
               elif self.player.up:
                   if self.player.y <= self.player.initial or check_collision_above(self.player, platform) or (self.pow != None and check_collision_above(self.player, self.pow)):
                       self.player.up = False
                   self.player.y -= 0.5
               elif not check_collision(self.player, platform) and not self.player.up:
                   self.player.y += 0.5

       # проверка жизней игрока
       if self.health <= 0:
           self.is_player_dead = True
           print("game over, score: " + str(self.score))

       # обновление движения врагов
       for enemy in self.enemies:
            if enemy.motion == True:
                boomerang = ScreenBoomerang()
                enemy.update(boomerang)

            # если враг доходит до нижнего левого или правого угла то возраждается снова
            if (enemy.x >= 223 or enemy.x <= 1) and (enemy.y >= 150.75):
                enemy.y = 25

            # враг идет по платформам, если платформы нет - он падает
            for platform in self.platforms:
                if check_collision_enemy(enemy, platform):
                    enemy.y = platform.y - enemy.height
                if not check_collision_enemy(enemy, platform):
                    enemy.y += 0.25

       #проверка коллизии игрока и платформы над ним
       for platform in self.platforms:
            for enemy in self.enemies:
                if check_collision_above(self.player, platform):
                    #если коллизия есть, и есть на этой платформе враг, то враг переворачивается
                    if enemy.x >= self.player.x-9 and enemy.x + enemy.width <= self.player.x + self.player.width +9 and enemy.y < self.player.y:
                        self.current_time = time.time()
                        self.rotated_enemies.append(enemy)
            self.rotation_enemies(self.rotated_enemies)

       #deleting coins
       if len(self.coins) != 0:
            for coin in self.coins:
                if check_left_right_collision(self.player, coin):
                    self.coins.remove(coin)
                    self.score += 10

        #hitting player logic
       for enemy in self.enemies:
           if time.time() - enemy.time_crash >= 2:
               enemy.crash = True

           if check_left_right_collision_enemy(self.player, enemy) and enemy.crash == True and enemy.rotated == False:
               self.health -= 1
               enemy.crash = False
               enemy.time_crash = time.time()

       # реализация кнопки для одновременного переворачивания всех игрков
       if len(self.objects) != 0 and type(self.objects[0]) == type(Pow(115, 105, 15, 15)):
           if check_collision_above(self.player, self.objects[0]):
               if self.objects[0].count > 0:
                   self.objects[0].count -= 1
                   for enemy in self.enemies:
                       self.current_time = time.time()
                       self.rotated_enemies.append(enemy)
                   self.rotation_enemies(self.rotated_enemies)
           if self.objects[0].count == 0:
                self.remove_object(self.objects[0])

   #функция переворота врага,враг лежит перевернутый 3 секунды
   def rotation_enemies(self, enemies):
       for rotated_enemy in enemies:
           if time.time() - self.current_time <= 3:
               rotated_enemy.motion = False
               rotated_enemy.rotated = True
               # если враг был убит, то он возраждается в инишиал позишин
               if check_collision_enemy(self.player, rotated_enemy):
                   rotated_enemy.motion = True
                   rotated_enemy.rotated = False
                   rotated_enemy.x = 240
                   rotated_enemy.y = 25
                   enemies.remove(rotated_enemy)
           else:
               rotated_enemy.motion = True
               rotated_enemy.rotated = False
               enemies.remove(rotated_enemy)

   def draw(self):
       """This method draws a Game Screen"""
       self.player.draw()
       pyxel.text(39, 4, f"SCORE {self.score:5}", 7)
       pyxel.text(155, 4, f"HEALTH {self.health:5}", 7)

       for enemy in self.enemies:
           enemy.draw()

       for obj in self.objects:
          obj.draw()

       for coin in self.coins:
           coin.draw()

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

   def is_game_over(self):
       return pyxel.btnp(pyxel.KEY_EQUALS) or self.is_player_dead
