import pyxel

class Player:
   """This class describes a Player"""
   def __init__(self, x: float, y: float, platforms):
       self.x = x
       self.y = y
       self.initial = y
       self.width = 10
       self.height = 10
       self.current_posY = 60
       self.platforms = platforms
       self.up = False


   def update(self, boomerang):
       """This method updates .... """

       self.current_posY = self.y
       if pyxel.btn(pyxel.KEY_RIGHT) and self.x < 240:
           self.x += 1
       if pyxel.btn(pyxel.KEY_LEFT) and self.x > 0:
           self.x -= 1
       if pyxel.btn(pyxel.KEY_UP) and self.y > 0:
           if self.jump():
               self.up = True

   def jump(self):
       for platform in self.platforms:
           if (round(self.y) + self.height + 15 >= platform.y-1 and  round(self.y) + self.height + 14 <= platform.y + 1) and (self.x>= platform.x and self.x +self.width <= platform.x + platform.width):
               self.initial = self.y - 40
               return True

   def draw(self):
       pyxel.blt(self.x, self.y, 0, 0, 0, 16, 24)
       pyxel.load("../finalProject/assets/sprites-jjsv-ndb.pyxres")



