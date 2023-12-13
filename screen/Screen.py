class Screen:
    """This is an abstract class for the three screens:
    Menu, Game and Game Over"""
    def __init__(self):
        self.next_screen = None

    @property
    def next_screen(self):
        return self.__next_screen

    @next_screen.setter
    def next_screen(self, next_screen):
        self.__next_screen = next_screen

    def get_instance(self, next_screen):
        raise Exception

    def update(self, boomerang):
        raise Exception

    def draw(self):
        raise Exception