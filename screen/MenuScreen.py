import pyxel
from screen.Screen import Screen


class MenuScreen(Screen):
    """This class describes a Menu screen of a game"""
    def update(self, boomerang):
        """This method updates screens by pressing on the SPACE button.
                Menu screen changes to Game screen"""
        if pyxel.btn(pyxel.KEY_SPACE):
            boomerang.screen = self.next_screen.get_instance(self.next_screen.next_screen)
            print(boomerang.screen)

    def draw(self):
        pyxel.cls(0)
        pyxel.rectb(54, 37.5, 120, 60, pyxel.frame_count % 2)
        pyxel.rectb(57, 40.5, 114, 54, pyxel.frame_count % 3)
        pyxel.rectb(60, 43.5, 108, 48, pyxel.frame_count % 4)
        pyxel.text(92, 63, "MARIO BROS", 7)
        pyxel.text(80, 120, "- PRESS SPACE -", 7)

    def get_instance(self, next_screen):
        """This method sets next screen and return the current one (menu screen)"""
        menu_screen = MenuScreen()
        menu_screen.next_screen = next_screen
        return menu_screen
