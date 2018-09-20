import random
class Player: #Create a class for the player with different attributes
    def __init__(self, name):
        self.name = name
        self.maxhealth = 20
        self.health = self.maxhealth
        self.attack =random.randint(1,6)
        self.armor = 4
        self.gold = 0
        self.pots = 0
        self.speed = 4
        
PlayerIG = Player('Jim')

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



zombie = Enemy(3,random.randint(1,6),'Slam','Zombie')
print("Welcome to Frank's battle simulator!")
print("Our contenders today are " + zombie.name + ", and " + PlayerIG.name +".")
print('Let the battle commence!')
Fight(zombie)