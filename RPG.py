import random
import os
import time
clear = lambda: os.system('cls')
class Player: #Create a class for the player with different attributes
    def __init__(self, name):
        self.name = name
        self.maxhealth = 1001
        self.health = self.maxhealth
        self.armor = 4
        self.attack = 10
        self.gold = 100
        self.pots = 0
        self.speed = 4
health_dashes = 20
def player_health():
  dash_convert = int(PlayerIG.maxhealth/health_dashes)
  current_dashes = int(PlayerIG.health/dash_convert)
  remaining_health = health_dashes - current_dashes

  health_display = ''.join(['-' for i in range(current_dashes)])
  remaining_display = ''.join([' ' for i in range(remaining_health)])
  percent = str(int((PlayerIG.health/PlayerIG.maxhealth)*100)) + "%"

  print("|" + health_display + remaining_display + "|")
  print("         " + percent)

class Enemy:
    def __init__(self,lvl,dmg,dtype,name,goldgain):
        self.lvl = lvl
        self.dmg = dmg
        self.dtype = dtype
        self.name = name
        self.goldgain= goldgain
        self.speed = random.randint(2,3)
        self.size = 2
        self.health = 20

    def attackPlayer(self):
        print("Enemy is swinging!")
        hit_chance = random.randint(5,25) + (self.lvl/2)
        if hit_chance >= (12+PlayerIG.armor):
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
                pass
        elif turn == 1:
            enemy.attackPlayer()
            turn = turn - 1
    if PlayerIG.health >= 0:
        print('Congratulations, you beat the ' + enemy.name + "! Don't you feel proud?")
        PlayerIG.gold=PlayerIG.gold+enemy.goldgain
        time.sleep(2)
        start1()
    else:
        print('The ' + enemy.name + " killed you. Sorry about that!")



def Prefight():#Decids what ememy to fight
    global enemy
    ZombieIG = Enemy(3, random.randint(1, 6), 'Slam', 'Zombie',50)
    enemy_num = random.randint(1,2)
    if enemy_num == 1:
        enemy=ZombieIG

    else:
        enemy= ZombieIG
    Fight(enemy)


class items :
    def __init__(self,desc, name, price,dmg,lvl):
        self.desc=desc
        self.name = name
        self.price = price
        self.dmg =dmg
        self.lvl= lvl
    def Store():
        clear()
        player_health()
        print("Shopkeep Johnson: You looking to buy something? or maybe you have some wares I might like to aquire")
        choice=input("1.)Buy\n2.)Sell\n3.)Exit")
        if choice == "1":
            if PlayerIG.gold < 20:
                clear()
                print("Shopkeep Johnson: You don't have enough money for my wares, get out of here!")
                time.sleep(2)
                start1()
            else:
                clear()
                print("Shopkeep Johnson: This is what I got up for sale, see anything you like?")
                purchaseables=[hmr,hmr,smlcmp,flex_tape,smlcmp,smlcmp]
                q=random.randint(0,1)
                w=random.randint(2,3)
                e=random.randint(4,5)
                print("\n" + purchaseables[q].name + " Price:" + str(purchaseables[q].price) + "\n\n"+ purchaseables[w].name + " Price:" + str(purchaseables[e].price) + "\n\n" + purchaseables[e].name + " Price:" + str(purchaseables[e].price))
                info=input()
                if info == purchaseables[q].name:
                    r=q
                elif info == purchaseables[w].name:
                    r=w
                elif info == purchaseables[e].name:
                    r=e
                print("Shopkeep Johnson: Nice choice! One of my finest wares\nDesc: "+ purchaseables[r].desc)
                item_buy = input("Shopkeep Johnson: Would you like to buy "+purchaseables[r].name+"? It is only "+ str(purchaseables[r].price) +" Gold.")
                if item_buy== "yes":
                    PlayerIG.gold-= purchaseables[r].price
                    Inventory.append(purchaseables[r])
                    print("Shopkeep Johnson: Thanks for the purchase. Have a great day!")
                    start1()
                elif item_buy == "no":
                    print("What are you wasting my time for then. Get out of here!")
                    start1()
        elif choice == "2":
            pass
        else:
            start1(1)





hmr=items(desc="This hammer heavy blow is sure to leave the enemy mangled", name="Hammer", price= 50,dmg = 6,lvl=1)
flex_tape = items(desc="Stops alot of damage", name="Flex Tape", price=25, dmg=12 ,lvl=7)
smlcmp = items(desc="This hammer heavy blow is sure to leave the enemy mangled", name="Small Camp", price=50, dmg=6,lvl=7)

Inventory=[smlcmp]
def inventory():
    clear()
    player_health()
    print("Here is what you have")
    l=len(Inventory)
    s=0
    while s <l:
        print(Inventory[s].name)
        s=s+1

    Item_use= input()
    if Item_use ==("Use "+ smlcmp.name):
        Inventory.remove(smlcmp)
        PlayerIG.health= PlayerIG.maxhealth
        count = 8
        while count > 0:
            print(str(count)+" hours left" )
            count = count - 1
            time.sleep(1)
            encounter= random.randint(0,8)
            if encounter == 1:
                print("You were woken up during the middle of the night by an enemy")
                Prefight()
            else:
                pass
        print("You wake up the next morning well rested and ready to continue on your adventure.")
        time.sleep(2)
        start1()
    else:
        start1()








def start1():#Shows the player his stats
    clear()
    player_health()
    print("Name: " + PlayerIG.name + "\nGold: " + str(PlayerIG.gold)+ "\nPotions: " + str(PlayerIG.pots) + "\nAttack: " + str(PlayerIG.attack))
    option = input("1.) Fight\n2.) Shop\n3.) Inventory\n4.) Load\n5.)Exit\n")
    if option == "1":
        Prefight()
    elif option == "2":
        items.Store()
    elif option == "3":
        inventory()
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



