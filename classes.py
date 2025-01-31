from constants import *

# Base Character class
class Character:
    def __init__(self, name, health, damage, speed):
        self.name = name
        self.health = int(health)
        self.damage = int(damage)
        self.speed = int(speed)

    def take_damage(self, incoming_dmg):
        self.health -= incoming_dmg
        
class Player(Character):
    def __init__(self, name, health, damage, speed):
        super().__init__(name, health, damage, speed)

    def set_stats(self, health, damage, speed):
        pass

class Barbarian(Player):
    def __init__(self, name, health, damage, speed):
        super().__init__(name, health, damage, speed)

    def set_stats(self):
        self.health = BARBARIAN_START_HEALTH
        self.damage = BARBARIAN_START_DAMAGE
        self.speed = BARBARIAN_START_SPEED


class Enemy(Character):
    def __init__(self, name, health, damage, speed):
        super().__init__(name, health, damage, speed)

class Weapon:
    def __init__(self, name, multiplyer, type):
        self.name = name
        self.multiplyer = multiplyer
        self.type = type

