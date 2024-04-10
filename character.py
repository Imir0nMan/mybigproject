
class Character:
    def __init__(self, health = 100):
        self.health = health

    def change_health(self, damage):
        if self.health > damage:
            self.health -= damage
        else:
            self.health = 0

    def set_health(self, health):
        self.health = health
