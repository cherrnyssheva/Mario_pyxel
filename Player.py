import pyxel
import math

class Player:
    """This class describes a Player"""
    def __init__(self, x: float, y: float, radius: float, color: int):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.current_posY = 60

    def update(self, boomerang):
        """This method updates Players movements after pressing onto
        the buttons up, down, right and left"""
        if pyxel.btn(pyxel.KEY_RIGHT) and self.x + self.radius < 160:
            self.x += 1
        if pyxel.btn(pyxel.KEY_LEFT) and self.x - self.radius > 0:
            self.x -= 1
        if pyxel.btn(pyxel.KEY_UP) and self.y - self.radius > 0:
            self.y -= 1
        if pyxel.btn(pyxel.KEY_DOWN) and self.y + self.radius < 120:
            self.y += 1

        self.current_posY = self.y

    def draw(self):
        pyxel.circ(self.x, self.y, self.radius, self.color)