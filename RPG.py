import random
import os
import time
from src import rpgplayer,items,fight
clear = lambda: os.system('cls')



def start1():#Shows the player his stats
    clear()
    rpgplayer.player_health(PlayerIG)
    print("Name: " + PlayerIG.name + "\nGold: " + str(PlayerIG.gold)+ "\nPotions: " + str(PlayerIG.pots) + "\nAttack: " + str(PlayerIG.attack))
    option = input("1.) Fight\n2.) Shop\n3.) Inventory\n4.) Load\n5.)Exit\n")
    if option == "1":
        fight.Prefight(PlayerIG)
    elif option == "2":
        items.items.Store(PlayerIG)
        start1()
    elif option == "3":
        items.inventory()
        start1()
    elif option == "4":
        pass
    elif option =="5":
        exit()
    else:
        start1()



def start():#asking player name and starting the code
    print("Hello what is your name?")
    option = input("-->")
    global PlayerIG
    PlayerIG = rpgplayer.Player(name=option)
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
