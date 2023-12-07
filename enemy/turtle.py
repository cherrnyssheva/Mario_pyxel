import pyxel

from enemy.enemy_parents import EnemyParent

class Turtle(EnemyParent):
    """This class describes an enemy turtle"""
    def __init__(self):
        EnemyParent.__init__(self, 90, 60, 2, 4, 2)


    def update(self):
        """This method updates movements of the turtle"""
        self.x += self.speed

        if self.x > 160:
            self.x = 0

        elif self.x > 160 and self.y == 0:
            self.x = 0
            self.y = 110

    def draw(self):
        pyxel.circ(self.x, self.y, self.radius, self.color)