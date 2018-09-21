import random
import os
clear = lambda: os.system('cls')
class Player: #Create a class for the player with different attributes
    def __init__(self, name):
        self.name = name
        self.maxhealth = 1001
        self.health = self.maxhealth
        self.armor = 4
        self.attack = 10
        self.gold = 0
        self.pots = 0
        self.speed = 4
healthDashes = 20
def do_health():
  dashConvert = int(PlayerIG.maxhealth/healthDashes)
  currentDashes = int(PlayerIG.health/dashConvert)
  remainingHealth = healthDashes - currentDashes

  healthDisplay = ''.join(['-' for i in range(currentDashes)])
  remainingDisplay = ''.join([' ' for i in range(remainingHealth)])
  percent = str(int((PlayerIG.health/PlayerIG.maxhealth)*100)) + "%"

  print("|" + healthDisplay + remainingDisplay + "|")
  print("         " + percent)

class Enemy:
    def __init__(self,lvl,dmg,dtype,name):
        self.lvl = lvl
        self.dmg = dmg
        self.dtype = dtype
        self.name = name
        self.speed = random.randint(2,3)
        self.size = 2
        self.health = 20

    def attackPlayer(self):
        print("Enemy is swinging!")
        hitchance = random.randint(1,20) + (self.lvl/2)
        if hitchance >= (12+PlayerIG.armor):
            PlayerIG.health = PlayerIG.health - self.dmg
            print('The ' + self.name + ' hit you for ' + str(self.dmg) + ' using ' + self.dtype + '!')
        else:
            print("The " + self.name + ' missed!')
def Fight(enemy):
    print(enemy.name + " has spawned! It has a size of " + str(enemy.size) +', and a speed of ' + str(enemy.speed))
    if enemy.speed <= PlayerIG.speed:
        turn = 0
    else:
        turn = 1

    while PlayerIG.health >= 1 and enemy.health >= 1:

        if turn == 0:
            uchoice = input("attack, or run?")
            if uchoice == 'attack' or uchoice == 'a':
                enemy.health = enemy.health - PlayerIG.attack
                print(PlayerIG.name + " has hit the " + enemy.name + ' for ' + str(PlayerIG.attack) + " damage!")
                turn = turn + 1
            elif uchoice == "run" or uchoice == 'r':
                print("Cowardly, you run from the " + enemy.name + "! It taunts you as you flee.")
                break
            else:
                print
        elif turn == 1:
            enemy.attackPlayer()
            turn = turn - 1
    if PlayerIG.health >= 0:
        print('Congratulations, you beat the ' + enemy.name + "! Don't you feel proud?")
        PlayerIG.health = PlayerIG.maxhealth
    else:
        print('The ' + enemy.name + " killed you. Sorry about that!")



def Prefight():#Decids what ememy to fight
    global enemy
    ZombieIG = Enemy(3, random.randint(1, 6), 'Slam', 'Zombie')
    enemynum = random.randint(1,2)
    if enemynum == 1:
        enemy=ZombieIG

    else:
        enemy= ZombieIG
    Fight(enemy)



def Store():#Still needs to be made
    pass

def start1():#Shows the player his stats
    clear()
    do_health()
    print("Name: " + PlayerIG.name + "\nGold: " + str(PlayerIG.gold)+ "\nPotions: " + str(PlayerIG.pots) + "\nAttack: " + str(PlayerIG.attack))
    option = input("1.) Fight\n2.) Store\n3.) Load\n4.)Exit\n")
    if option == "1":
        Prefight()
    elif option == "2":
        Store()
    elif option == "3":
        pass
    elif option =="4":
        exit()
    else:
        start1()



def start():#asking player name and starting the code
    print("Hello what is your name?")
    option = input("-->")
    global PlayerIG
    PlayerIG = Player(name=option)
    start1()



def main():#Gives options to the player. Still need a save feature
    print("Welcome to my game!\n")
    print("1.)Start\n2.)Load\n3.)Exit")
    option = input("-> ")
    if option == "1":
        start()
    elif option == "2":
        pass
    elif option == "3":
        exit()
    else:
        main()

main()#Starts the game



