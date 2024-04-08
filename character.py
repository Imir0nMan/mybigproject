

class Character:
    def __init__(self, health = 10):
        self.health = health

    def change_health(self, damage):
        if self.health > damage:
            self.health -= damage
        else:
            self.health = 0


###########

class Character2:
    def __init__(self, health, weapon):
        self.health = health
        self.weapon = weapon
    def attack(self, weapon):
        j = rd.randint(1, 20)
        if j == 20:
            k = weapon + j
        elif j >= 7:
            k = weapon
        else:
            k = weapon - j
        if k <= 4:
            k = 5
        return k

    def block(self):
        l = rd.randint(1, 20)
        if l >= 7:
            return 0
        else:
            return 1

    def fend(self, weapon):
        m = self.block()
        m = 1 if m == 0 else 0
        n = self.attack(weapon)
        o = m * n
        return o











def storytelling(action, types):
    if types == 1:
        if action >= 27:
            print(f"attack was sucssesfull, damage is {action}")
        else:
            print(f"attack was weak, damage is {action}")
    elif types == 2:
        if action:
            print("block was sucssesfull")
        else:
            print("opponend broke your block")
    elif types == 3:
        if action:
            print("succsess in fend")
        else:
            print("failure in fend")
    else:
        print("wrong parameter")















def npc_storytelling(action, types):
    if types == 1:
        if action >= 27:
            print(f"attack was sucssesfull, damage is {action}")
        else:
            print(f"attack was weak, damage is {action}")
    elif types == 2:
        if action:
            print("block was sucssesfull")
        else:
            print("opponend broke your block")
    elif types == 3:
        if action:
            print("succssess in fend")
        else:
            print("failure in fend")
    else:
        print("wrong parameter")


def start():
    print("there are 3 actions: attack, block, fend \n")
    print("you met aggresive knight who want to fight with you")
    challenge_answer = input("will you accept yes/no\n")
    if challenge_answer.lower() == "no":
        print("you such a loser")
        print("Game over")
        return "lose"
    k = rd.choice(['player', 'npc'])
    return (k)


def npc_text(status, damage):
    if status > 0:
        print(f"enemy attacked with {damage} damage")
    else:
        print("enemy put block")


















def player_move(player):
    player_action = input("input action \n")
    current_dict = {}
    if player_action == "attack":
        damage_dealt = player.attack()
        temp_status = 2
        current_dict[temp_status] = damage_dealt
        storytelling(damage_dealt, 1)
    elif player_action == "block":
        block_result = player.block()
        temp_status = 1
        current_dict[temp_status] = block_result
        storytelling(block_result, 2)
    elif player_action == "fend":
        fend_result = player.fend()
        temp_status = 3
        current_dict[temp_status] = fend_result
        storytelling(fend_result, 3)
    else:
        print("Invalid action. Please choose attack, block, or fend.")
        return 0, 0
    return temp_status, current_dict


def npc_move(player, npc, npc_action, temp_status, current_dict):
    attk = npc.attack()
    npc_text(npc_action, attk)
    if npc_action == 0:
        blk = npc.block()
        blk = 1 if blk == 0 else 0
        current_choice = current_dict[temp_status]
        temp_status = 2 if temp_status > 1 else 1
        npc.health -= (temp_status - 1) * current_choice * blk
    else:
        if temp_status == 1:
            player.health -= current_dict[temp_status] * attk
        elif temp_status == 2:
            npc.health -= current_dict[temp_status]
            player.health -= attk
        elif temp_status == 3:
            k = current_dict[temp_status]
            if k == 0:
                player.health -= attk
            else:
                npc.health -= k


def fight(npc, player):
    temp_move = start()
    if temp_move == "lose":
        return (0)
    while npc.health > 0 and player.health > 0:
        print("\nPlayer Health:", player.health)
        print("NPC Health:", npc.health)
        if temp_move == 'player':
            player_action_result = player_move(player)
            if player_action_result == (0, 0):
                continue
            temp_status, current_dict = player_action_result
            npc_action = rd.randint(0, 3)
            npc_move(player, npc, npc_action, temp_status, current_dict)
            temp_move = 'npc'
        elif temp_move == 'npc':
            npc_action = rd.randint(0, 3)
            player_action_result = player_move(player)
            if player_action_result == (0, 0):
                continue
            temp_status, current_dict = player_action_result
            npc_move(player, npc, npc_action, temp_status, current_dict)
            temp_move = 'player'
    if player.health <= 0:
        print("\nGame over! You lose!")
    else:
        print("\nCongratulations! You defeated the NPC!")


def mn():
    anasun = Character2("npc", 170)
    qyal = Character2("Vaspur", 120)
    fight(anasun, qyal)

