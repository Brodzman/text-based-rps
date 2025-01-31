from classes import *
from constants import *
import random

def main():
    player = create_player(input('Enter name: '), input('Enter role\n 1. Barbarian\n 2. Mage\n 3. Rogue\n'))
    enemy = enemy_spawner()
    print(player.damage)
    print(player.health)

def create_player(name, role):
    if role == '1':
        player = Barbarian
    elif role == '2':
        player = Mage
    elif role == '3':
        player = Rogue
    else:
        create_player(name, input('Invalid input'))
    player.name = name
    player.set_stats(player)
    return player

def enemy_spawner():
    slime = Enemy
    slime.name = 'slime'
    slime.damage = random.randint(1, 50)
    slime.health = random.randint(50,100)
    return slime



if __name__ == "__main__":
    main()