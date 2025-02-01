from classes import *
from constants import *

import random
import os

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    player, weapon = game_start()
    enemies = level_1()
    init_battlefield(player, enemies)
    turn_order = determine_turn_order(player, enemies)
    print(turn_order)
    selection = enemy_selection(enemies, player)
    for character in turn_order:
        if character != player:
            character.deal_damage(character.damage, player)
        elif character == player:
            character.deal_damage(character.damage, turn_order[selection - 1])
    for i in turn_order:
        print(f'after battle {i} health is: {i.health}')
    
def enemy_selection(enemies, player):
    i = 1
    for enemy in enemies:
        if enemy != player:
            print(f'{i}. {enemy.name}')
            i += 1
        else:
            pass
    selection = input('Who would you like to attack?')
    return int(selection)


def determine_turn_order(player, enemies):
    turn_order = []
    for enemy in enemies:
        if enemy.speed > player.speed:
            turn_order.append(enemy)
        elif enemy.speed < player.speed and player not in turn_order:
            turn_order.append(player)
    if player not in turn_order:
        turn_order.append(player)
    return turn_order

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
    slime.speed = 1
    return slime

def level_1():
    enemy_list = []
    enemy1 = enemy_spawner()
    enemy2 = Slime
    enemy2.set_stats(enemy2, 1)
    enemy_list.append(enemy1)
    enemy_list.append(enemy2)
    return enemy_list


if __name__ == "__main__":
    main()