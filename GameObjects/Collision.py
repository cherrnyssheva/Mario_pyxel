
def check_collision(player, platform):
    return(round(player.y) + player.height + 14 >= platform.y-1 and  round(player.y) + player.height + 14 <= platform.y + 3) and (player.x + player.width >= platform.x and player.x <= platform.x + platform.width)

def check_collision_enemy(player, platform):
    return(round(player.y) + player.height >= platform.y-1 and  round(player.y) + player.height <= platform.y + 3) and (player.x + player.width >= platform.x and player.x <= platform.x + platform.width)


def check_collision_above(player, platform): #эта функция вернет True если произойдет удар головы марио с платформой
    return(player.y >= platform.y + platform.height - 2 and player.y <= platform.y + platform.height) and (player.x + player.width + 5>= platform.x and player.x <= platform.x + platform.width)