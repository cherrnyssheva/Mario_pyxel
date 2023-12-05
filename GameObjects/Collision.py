
def check_collision(player, platform):
    return(round(player.y) + player.height + 14 >= platform.y-1 and  round(player.y) + player.height + 14 <= platform.y + 3) and (player.x + player.width >= platform.x and player.x <= platform.x + platform.width)


def check_collision_above(player, platform):
    return(round(player.y) + player.height + 14 >= platform.y-1 and  round(player.y) + player.height + 14 <= platform.y + 1) and (player.x + player.width >= platform.x and player.x <= platform.x + platform.width)