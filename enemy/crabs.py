import pyxel


class Crabs:
    """This class describes an enemy turtle"""
    def __init__(self, x: float, y: float, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.speed = 2

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    def update(self, boomerang):
        self.x += self.speed - 0.75
        if self.x > 223:
            self.x = 1
        if self.x < 1:
            self.x = 223

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 40, 16, 16)
        pyxel.load("../finalProject/assets/sprites-jjsv-ndb.pyxres")