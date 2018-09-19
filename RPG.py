import random
import os

class Player: #Create a class for the player with different attributes
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 10
        self.gold = 0
        self.pots = 0

class Goblin: #simple enemy class has simple attributes
    def __init__(self, name):
        self.name = name
        self.maxhealth = 50
        self.health = self.maxhealth
        self.attack = 5
        self.goldgain = 10

GoblinIG=Goblin("Goblin")

class Zombie:#very similar to the Goblin class with different variables
    def __init__(self, name):
        self.name = name
        self.maxhealth = 70
        self.health = self.maxhealth
        self.attack = 7
        self.goldgain = 15
ZombieIG=Zombie("Zombie")


def Fight():#Not completed yet. IT only displays the names
    print(PlayerIG.name + " vs "+ enemy.name)
    while PlayerIG.health >= 1:
        PlayerIG = PlayerIG.health-enemy.attack
        enemy.health = enemy.health-PlayerIG.attack
        print(PlayerIG.health)
        print(enemy.health)


def Prefight():#Decids what ememy to fight
    global enemy
    enemynum = random.randint(1,2)
    if enemynum == 1:
        enemy=GoblinIG

    else:
        enemy= ZombieIG
    Fight()



def Store():#Still needs to be made
    pass

def start1():#Shows the player his stats
    print("Name: " + PlayerIG.name + "\nGold: " + str(PlayerIG.gold)+ "\nPotions: " + str(PlayerIG.pots) + "\nHealth: " + str(PlayerIG.health) + "/" + str(
        PlayerIG.maxhealth) + "\nAttack: " + str(PlayerIG.attack))
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



