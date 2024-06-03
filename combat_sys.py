import random

class TempTurn:
    def __init__(self):
        # Randomly choose who starts the fight
        self.turn = random.choice(["player", "npc"])

def check_near_knight(matrix, player_position, knight_symbol):
    """
    Check if the player is near the knight in the matrix.
    """
    for dx in range(-7, 8):
        for dy in range(-7, 8):
            x = player_position[0] + dx
            y = player_position[1] + dy
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] == knight_symbol:
                return True
    return False


def attack(weapon):
    wp_min = weapon["min"]
    wp_max = weapon["max"]
    character_attack = random.randint(wp_min, wp_max)

    return {
        "character_attack": character_attack
    }

def block():
    blk = random.randint(1, 20)
    if blk >= 7:
        return {
            "block": True}
    else:
        return {
            "block": False}

def fend(weapon):
    blk = block()
    if not blk["block"]:
        atk = attack(weapon)
        atk["fend"] = True
        return atk
    else:
        return {
            "fend": False}

def handle_fighting(action, weapon):
    if action == "attack":
        return attack(weapon)

    elif action == "block":
        return block()

    elif action == "fend":
        return fend(weapon)

    else:
        return {"unknown_command": True}


def player_move(tk, command, player_weapon):
    player_action = command
    player_result = handle_fighting(player_action, player_weapon)
    if player_result.get("unknown_command"):
        player_action = None  # Reset player's action if unknown command
        return {"unknown_command": True}

    tk.print_message(f"Your move: {player_action}")

    if player_result.get("block"):
        if player_result["block"]:
            tk.print_message("You put block successfully")
        else:
            tk.print_message("Your attempt to block failed")

    elif player_result.get("fend"):
        if player_result["fend"]:
            tk.print_message("You fended successfully")
        else:
            tk.print_message("Your attempt to fend was unsuccessful")

    else:
        tk.print_message(f"You attacked dealing {player_result.get('character_attack', 0)} damage.")

    return player_result



def npc_move(tk, npc_weapon):
    npc_action = random.choices(["attack", "block", "fend"], weights=[0.6, 0.2, 0.2], k=1)[0]
    npc_result = handle_fighting(npc_action, npc_weapon)
    tk.print_message(f"Enemy move: {npc_action}")
    if npc_result.get("block"):
        if npc_result["block"]:
            tk.print_message("Enemy put block successfully")
        else:
            tk.print_message("Enemy's attempt to block failed")

    elif npc_result.get("fend"):
        if npc_result["fend"]:
            tk.print_message("Enemy fended successfully")
        else:
            tk.print_message("Enemy's attempt to fend was unsuccessful")

    else:
        tk.print_message(f"Enemy attacked dealing {npc_result.get('character_attack', 0)} damage.")

    return npc_result


def fight_process(tk, command, player, npc, temp_turn):
    player_weapon = {"min": 5, "max": 15}  # Sample player weapon stats
    npc_weapon = {"min": 3, "max": 12}  # Sample NPC weapon stats
    player_health = player.health
    npc_health = npc.health

    if player_health > 0 and npc_health > 0:

        if temp_turn == "npc":
            npc_result = npc_move(tk, npc_weapon)
            player_result = player_move(tk, command, player_weapon)
            if player_result.get("unknown_command"):
                tk.print_message("Unnown command: please insetr attack, block or fend")
                player_action = None  # Reset player's action if unknown command
                return
        elif temp_turn == "player":
            player_result = player_move(tk, command, player_weapon)
            if player_result.get("unknown_command"):
                tk.print_message("Unnown command: please insetr attack, block or fend")
                player_action = None  # Reset player's action if unknown command
                return
            npc_result = npc_move(tk, npc_weapon)
        player_damage = max(0, npc_result.get("character_attack", 0) - (player_result.get("block", False) * 5))
        npc_damage = max(0, player_result.get("character_attack", 0) - (npc_result.get("block", False) * 5))
        player_health -= player_damage
        npc_health -= npc_damage
        if player_health < 0:
            player_health = 0
        if npc_health < 0:
            npc_health = 0
        tk.print_message(f"Your health՝ {player_health}")
        tk.print_message(f"Enemy's health {npc_health}")
    if player_health <= 0:
        tk.print_message("You loose, the enemy killed you. Game Over")
    elif npc_health <= 0:
        tk.print_message("Congratulations! \nYou defeated the enemy")
    player.set_health(player_health)
    npc.set_health(npc_health)



