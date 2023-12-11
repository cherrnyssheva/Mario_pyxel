import pyxel

class Pipes:
    def __init__(self, x, y, height, width):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        pass

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 64, 176, 48, 24)
        pyxel.blt(192, 20, 0, 0, 176, 48, 24)
        pyxel.blt(0, 140, 0, 48, 184, 32, 24)
        pyxel.blt(208, 140, 0, 48, 184, -32, 24)
        pyxel.load("../finalProject-main/assets/sprites-jjsv-ndb.pyxres")