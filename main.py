from classes import *
from constants import *
import random

def main():
    player = create_player(input('Enter name: '), input('Enter role\n 1. Barbarian\n 2. Mage\n 3. Rogue\n'))
    weapon = starting_weapon(player)
    enemy = enemy_spawner()
    print(enemy.health)
    player.deal_damage(player.weapon_damage(player, weapon), enemy)
    print(enemy.health)

def create_player(name, role):
    if role == '1':
        player = Barbarian
    elif role == '2':
        player = Mage
    elif role == '3':
        player = Rogue
    else:
        create_player(name, input('Invalid input')) # Fix bug here
    player.name = name
    player.set_stats(player)
    return player

def starting_weapon(player):
    if player == Barbarian:
        weapon = Axe
    elif player == Mage:
        weapon = Staff
    elif player == Rogue:
        weapon = Daggers    
    weapon.set_attributes(weapon)
    return weapon

def enemy_spawner():
    slime = Enemy
    slime.name = 'slime'
    slime.damage = 50
    slime.health = 50
    return slime



if __name__ == "__main__":
    main()