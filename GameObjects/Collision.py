
def check_collision(player, platform):
    return(round(player.y) + player.height + 14 >= platform.y-1 and  round(player.y) + player.height + 14 <= platform.y + 3) and (player.x + player.width >= platform.x and player.x <= platform.x + platform.width)

def check_collision_enemy(player, platform):
    return(round(player.y) + player.height >= platform.y-1 and  round(player.y) + player.height <= platform.y + 3) and (player.x + player.width >= platform.x and player.x <= platform.x + platform.width)

def check_collision_above(player, platform): #эта функция вернет True если произойдет удар головы марио с платформой
    return(player.y >= platform.y + platform.height - 2 and player.y <= platform.y + platform.height) and (player.x + player.width + 5>= platform.x and player.x <= platform.x + platform.width)

def check_left_right_collision(player, coin):
    player_right = player.x + player.width
    coin_right = coin.x + coin.width

    player_left = player.x
    coin_left = coin.x
    y_range = player.y - coin.y
    if y_range > -10 and y_range < 10:
        return (player_right >= coin_left and player_right <= coin_left + 3 or player_left <= coin_right and player_left >= coin_right + 3)

def check_left_right_collision_enemy(player, enemy):
        player_right = player.x + player.width
        enemy_right = enemy.x + enemy.width

        player_left = player.x
        enemy_left = enemy.x
        y_range = player.y - enemy.y

        if y_range > -10 and y_range < 10:
            return (player_right >= enemy_left and player_right <= enemy_left + 3 or player_left <= enemy_right and player_left >= enemy_right + 3)
