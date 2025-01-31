from constants import *

# Base Character class
class Character:
    def __init__(self, name, health, damage, speed):
        self.name = name
        self.health = int(health)
        self.damage = int(damage)
        self.speed = int(speed)

    def deal_damage(damage, target):
        target.health -= damage

    def weapon_damage(self, weapon):
        total_damage = self.damage * weapon.multiplyer
        return total_damage
        
class Player(Character):
    def __init__(self, name, health, damage, speed):
        super().__init__(name, health, damage, speed)

    def set_stats(self):
        pass

# Each role declaration
class Barbarian(Player):
    def __init__(self, name, health, damage, speed):
        super().__init__(name, health, damage, speed)

    def set_stats(self):
        self.health = BARBARIAN_START_HEALTH
        self.damage = BARBARIAN_START_DAMAGE
        self.speed = BARBARIAN_START_SPEED

class Mage(Player):
    def __init__(self, name, health, damage, speed):
        super().__init__(name, health, damage, speed)

    def set_stats(self):
        self.health = MAGE_START_HEALTH
        self.damage = MAGE_START_DAMAGE
        self.speed = MAGE_START_SPEED

class Rogue(Player):
    def __init__(self, name, health, damage, speed):
        super().__init__(name, health, damage, speed)

    def set_stats(self):
        self.health = ROGUE_START_HEALTH
        self.damage = ROGUE_START_DAMAGE
        self.speed = ROGUE_START_SPEED


class Enemy(Character):
    def __init__(self, name, health, damage, speed):
        super().__init__(name, health, damage, speed)

class Weapon:
    def __init__(self, name, multiplyer, type):
        self.name = name
        self.multiplyer = multiplyer
        self.type = type
    
    def set_attributes():
        pass

class Axe(Weapon):
    def __init__(self, name, multiplyer, type):
        super().__init__(name, multiplyer, type)

    def set_attributes(self):
        self.multiplyer = 2

class Staff(Weapon):
    def __init__(self, name, multiplyer, type):
        super().__init__(name, multiplyer, type)

    def set_attributes(self):
        self.multiplyer = 1.5

class Daggers(Weapon):
    def __init__(self, name, multiplyer, type):
        super().__init__(name, multiplyer, type)

    def set_attributes(self):
        self.multiplyer = 1
