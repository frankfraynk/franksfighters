import random
import time
from .rpgenemy import Enemy
def Fight(player,enemy):
    print(enemy.name + " has spawned! It has a size of " + str(enemy.size) +', and a speed of ' + str(enemy.speed))
    if enemy.speed <= player.speed:
        turn = 0
    else:
        turn = 1

    while player.health >= 1 and enemy.health >= 1:

        if turn == 0:
            uchoice = input("attack, or run?")
            if uchoice == 'attack' or uchoice == 'a':
                enemy.health = enemy.health - player.attack
                print(player.name + " has hit the " + enemy.name + ' for ' + str(player.attack) + " damage!")
                turn = turn + 1
            elif uchoice == "run" or uchoice == 'r':
                print("Cowardly, you run from the " + enemy.name + "! It taunts you as you flee.")
                break
            else:
                pass
        elif turn == 1:
            enemy.attackPlayer(player)
            turn = turn - 1
    if player.health >= 0 and uchoice != 'r':
        print('Congratulations, you beat the ' + enemy.name + "! Don't you feel proud?")
        player.gold=player.gold+enemy.goldgain
        time.sleep(2)
        start1()
    else:
        print('The ' + enemy.name + " killed you. Sorry about that!")



def Prefight(player):#Decids what enemy to fight
    global enemy
    ugh = random.randint(1,6)
    ZombieIG = Enemy(3, ugh, 'Slam', 'Zombie',50)
    enemy_num = random.randint(1,2)
    if enemy_num == 1:
        enemy=ZombieIG

    else:
        enemy= ZombieIG
    Fight(player,enemy)
