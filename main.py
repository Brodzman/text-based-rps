from classes import *
import random

def main():
    player = create_player(input('Enter name: '))
    enemy = enemy_spawner()
    print(enemy.damage)
    print(player.name)

def create_player(name):
    player = Player
    player.name = name
    player.damage = 25
    player.health = 100
    return player

def enemy_spawner():
    slime = Enemy
    slime.name = 'slime'
    slime.damage = random.randint(1, 50)
    slime.health = random.randint(50,100)
    return slime



if __name__ == "__main__":
    main()