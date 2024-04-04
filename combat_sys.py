import random

def add_knight_to_map(size):
    """
    Add a knight symbol to the matrix at a random position.
    """
    matrix_size = size
    for _ in range (3):
        x = random.randint(0, matrix_size - 1)
        y = random.randint(0, matrix_size - 1)
        k = (x - 3, x + 3, y - 3, y + 3)

    return k

def check_near_knight(matrix, player_position, knight_symbol):
    """
    Check if the player is near the knight in the matrix.
    """
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            x = player_position[0] + dx
            y = player_position[1] + dy
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] == knight_symbol:
                return True
    return False

def handle_fight(player, knight):
    """
    Handle the fight between the player and the knight.
    """
    enemy_health = 10
    enemy_attack = random.randint(1, 3)
    enemy_defense = random.randint(0, 2)

    player_damage = max(0, player["attack"] - enemy_defense)
    enemy_damage = max(0, enemy_attack - player["defense"])

    player["health"] -= enemy_damage
    enemy_health -= player_damage

    return player, enemy_health


