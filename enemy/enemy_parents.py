class EnemyParent:
    """This is a parent class for enemies"""
    def __init__(self, x: float, y: float, radius: float, color: int, speed: float):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed

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

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed