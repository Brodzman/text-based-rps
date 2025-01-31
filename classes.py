class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = int(health)
        self.damage = int(damage)

    def take_damage(self, incoming_dmg):
        self.health -= incoming_dmg
        
class Player(Character):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

class Enemy(Character):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

class Weapon:
    def __init__(self, name, multiplyer, type):
        self.name = name
        self.multiplyer = multiplyer
        self.type = type

