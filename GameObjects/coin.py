import pyxel

class Coin:
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
        pyxel.blt(self.x, self.y, 0, 16, 208, 8, 16)
        pyxel.load("../finalProject/assets/sprites-jjsv-ndb.pyxres")