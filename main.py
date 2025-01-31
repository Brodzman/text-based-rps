from classes import *
from constants import *

import random
import os

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    player, weapon = game_start()
    enemies = level_1()
    init_battlefield(player, enemies)

def init_battlefield(player, enemies):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('A challenge appears!\n---------------------')
    for enemy in enemies:
        print(enemy.name, end='  ')
    print(f'\n\n{player.name}')

def game_start():
    player = create_player(input('Enter name: '), input('Enter role\n 1. Barbarian\n 2. Mage\n 3. Rogue\n'))
    weapon = starting_weapon(player)
    return player, weapon

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

def level_1():
    enemy_list = []
    enemy1 = enemy_spawner()
    enemy2 = enemy_spawner()
    enemy_list.append(enemy1)
    enemy_list.append(enemy2)
    return enemy_list


if __name__ == "__main__":
    main()