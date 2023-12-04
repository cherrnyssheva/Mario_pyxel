import pyxel
import math
import time
from GameObjects.Collision import check_collision
from GameObjects.Platform import Platform


class Player:
   """This class describes a Player"""
   def __init__(self, x: float, y: float, radius: float, color: int, isGround:bool):
       self.x = x
       self.y = y
       self.radius = radius
       self.width = 10
       self.height = 10
       self.color = color
       self.current_posY = 60
       self.is_jumping = False
       self.jump_count = 0
       self.gravity = 10
       self.is_ground = isGround
       self.counter = 0
       self.currentPlatform = None

   def update(self, boomerang):
       """This method updates .... """
       self.current_posY = self.y
       if pyxel.btn(pyxel.KEY_RIGHT) and self.x + self.radius < 160:
           self.x += 1
       if pyxel.btn(pyxel.KEY_LEFT) and self.x - self.radius > 0:
           self.x -= 1


       if pyxel.btn(pyxel.KEY_UP) and self.y - self.radius > 0:
           step = self.jump()
           self.y -= step

       #он должен быть на земле что бы прыгать
       if pyxel.btn(pyxel.KEY_DOWN) and self.y + self.radius < 120:
           self.y += 1

   def jump(self):
       if self.is_ground:
           return 10
       return 0

   def draw(self):
       pyxel.circ(self.x, self.y, self.radius, self.color)
