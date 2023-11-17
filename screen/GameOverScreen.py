import pyxel

from screen.Screen import Screen


class GameOverScreen(Screen):
    """"This class describes a Game Over screen"""
    def __init__(self):
        Screen.__init__(self)
        self.score = 0

    def update(self, boomerang):
        """This method updates screens by pressing on the "-" button.
        Game over screen changes to Menu Screen"""
        if pyxel.btn(pyxel.KEY_MINUS):
            boomerang.screen = self.next_screen.get_instance(self.next_screen.next_screen)

    def draw(self):
        """This method draws a Game Over screen"""
        pyxel.cls(12)
        pyxel.text(40, 70, "-GAME OVER-", pyxel.frame_count % 12)
        pyxel.rectb(25, 63, 70, 20, pyxel.frame_count % 12)
        pyxel.text(26, 135, """- PRESS  " - " TO -\n    START AGAIN""", pyxel.frame_count % 3)
        pyxel.text(39, 4, f"SCORE: {self.score:5}", 7)

    def set_score(self, score):
        """This method sets score of a Player"""
        self.score = score

    def get_instance(self, next_screen):
        """This method sets next screen and return the current one (game over screen)"""
        game_over_screen = GameOverScreen()
        game_over_screen.next_screen = next_screen
        return game_over_screen

