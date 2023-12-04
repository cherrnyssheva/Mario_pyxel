import pyxel

class Platform:
    def __init__(self, x, y, height, width, color):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color

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
        pyxel.rect(self.x, self.y, self.width, self.height, self.color)

