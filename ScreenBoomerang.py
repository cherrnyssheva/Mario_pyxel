class ScreenBoomerang:
    """This class is used for transmission of information
     between objects on the screen and the screen."""
    def __init__(self):
        self.add_list = []
        self.delete_list = []

    def add_object(self, obj):
        self.add_list.append(obj)

    def remove_object(self, obj):
        self.delete_list.append(obj)

    def is_add_list_empty(self):
        return len(self.add_list) == 0

    def is_delete_list_empty(self):
        return len(self.delete_list) == 0

    def get_add_list(self):
        return self.add_list

    def get_delete_list(self):
        return self.delete_list


class AppBoomerang:
    """This class is used for transmission of information
     between screens and the game."""
    def __init__(self):
        self.__screen = None

    @property
    def screen(self):
        return self.__screen

    @screen.setter
    def screen(self, screen):
        self.__screen = screen

