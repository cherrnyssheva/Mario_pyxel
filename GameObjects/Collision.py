import pyxel

def check_collision(player, platform):
    return (player.x < platform.x+5 + platform.width) and (player.x-5 + player.width > platform.x) and (
                player.y < platform.y + platform.height) and (player.y + player.height > platform.y)


def check_collision_above(player, platform):
    return (player.x < platform.x + 5 + platform.width) and (player.x - 5 + player.width > platform.x) and (
            player.y < platform.y + platform.height) and (player.y + player.height > platform.y)