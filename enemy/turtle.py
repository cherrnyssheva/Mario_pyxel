import pyxel

from enemy.enemy_parents import EnemyParent

class Turtle(EnemyParent):
    """This class describes an enemy turtle"""
    def __init__(self, x, y, height, width, motion:bool, rotated:bool):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.motion = motion
        self.rotated = rotated
        EnemyParent.__init__(self, self.x, self.y, 2, 4, 2)


    def update(self, boomerang):
        """This method updates movements of the turtle"""
        self.x -= self.speed - 1

        if self.x > 223:
            self.x = 1
        if self.x < 1:
            self.x = 223
        if self.x < 1 and self.y < 20:
            self.x = 223
            self.y = 20

    def draw(self):
        if not self.rotated:
            pyxel.blt(self.x, self.y, 0, 0, 24, 16, 16)
            pyxel.load("../finalProject/assets/sprites-jjsv-ndb.pyxres")
        else:
            pyxel.blt(self.x, self.y, 0, 0, 24, 16, -16)
            pyxel.load("../finalProject/assets/sprites-jjsv-ndb.pyxres")