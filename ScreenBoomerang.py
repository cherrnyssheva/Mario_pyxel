class ScreenBoomerang:
    """This class is used for transmission of information
     between objects on the screen and the screen."""
    def __init__(self):
        self.add_list = []
        self.delete_list = []
        """self.player_bullets_add = []
        self.player_bullets_delete = []
        self.enemy_bullets_add = []
        self.enemy_bullets_delete = []"""

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


""" # player shooting controller

 def get_player_bullets_add(self):
     return self.player_bullets_add

 def get_player_bullets_delete(self):
     return self.player_bullets_delete

 def add_player_bullet(self, obj):
     self.player_bullets_add.append(obj)

 def remove_player_bullet(self, obj):
     self.player_bullets_delete.append(obj)

 def is_player_bullets_add_empty(self):
     return len(self.player_bullets_add) == 0

 def is_player_bullet_delete_empty(self):
     return len(self.player_bullets_delete) == 0

 # enemy shooting controller

 def get_enemy_bullets_add(self):
     return self.enemy_bullets_add

 def get_enemy_bullets_delete(self):
     return self.enemy_bullets_delete

 def add_enemy_bullet(self, obj):
     self.enemy_bullets_add.append(obj)

 def remove_enemy_bullet(self, obj):
     self.enemy_bullets_delete.append(obj)

 def is_enemy_bullets_add_empty(self):
     return len(self.enemy_bullets_add) == 0

 def is_enemy_bullet_delete_empty(self):
     return len(self.enemy_bullets_delete) == 0
"""

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

