import random


def attack(player_stats, enm):
    enemy_health = enm.health
    enemy_attack = random.randint(1, 3)
    enemy_defense = random.randint(0, 2)

    player_damage = max(0, player_stats["attack"] - enemy_defense)
    enemy_damage = max(0, enemy_attack - player_stats["defense"])

    player_stats["health"] -= enemy_damage
    if player_damage < enemy_health:
        enemy_health -= player_damage
    else:
        enemy_health = 0
    enm.change_health(player_damage)

    return {
        "player_stats": player_stats,
        "enemy_health": enemy_health,
        "player_damage": player_damage,
        "enemy_damage": enemy_damage
    }

def block(player_stats):
    l = random.randint(1, 20)
    if l >= 7:
        return {
            "player_stats": player_stats,
            "block": True}
    else:
        return {
            "player_stats": player_stats,
            "block": False}

def fend(player_stats, enm):
    m = block(player_stats)
    m = 1 if m["block"] == False else 0
    n = attack(player_stats, enm)
    if m:
        return {
            "fend": True,
            "player_stats": n["player_stats"],
            "enemy_health": n["enemy_health"],
            "player_damage": n["player_damage"],
            "enemy_damage": n["enemy_damage"]
        }
    else:
        return {"fend": False,
                "player_stats": n["player_stats"],
                "enemy_health": n["enemy_health"],
                "player_damage": n["player_damage"],
                "enemy_damage": n["enemy_damage"]
                }

def handle_fighting(action, player_stats, enm):
    if action == "attack":
        return attack(player_stats, enm)

    elif action == "block":
        return block(player_stats)

    elif action == "fend":
        return fend(player_stats, enm)

    else:
        return {"unknown_command": True}

