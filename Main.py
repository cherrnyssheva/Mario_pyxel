from App import App
from screen.MenuScreen import MenuScreen
"""
from screen.GameScreen import GameScreen
from screen.GameOverScreen import GameOverScreen
"""
menu_screen = MenuScreen()

"""game_screen = GameScreen()
game_over_screen = GameOverScreen()

# set up menu screen
menu_screen.next_screen = game_screen

# set up game screen
game_screen.next_screen = game_over_screen

# set up game over screen
game_over_screen.next_screen = menu_screen"""

# set up app screen
app = App(menu_screen, 160, 120)
app.run()