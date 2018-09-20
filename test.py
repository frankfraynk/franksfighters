import random
class Player: #Create a class for the player with different attributes
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 10
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
        self.health = 4

    def attackPlayer(self):
        print("Enemy is swinging!")
        hitchance = random.randint(1,20) + (self.lvl/2)
        if hitchance >= (12+PlayerIG.armor):
            PlayerIG.health = PlayerIG.health - self.dmg
def Fight(enemy):
    print(enemy.name + " has spawned! It has a size of " + str(enemy.size) +', and a speed of ' + str(enemy.speed))
    if enemy.speed <= PlayerIG.speed:
        turn = 0
    else:
        turn = 1

    while PlayerIG.health > 0 or enemy.health > 0:
        if turn == 0:
            uchoice = input("attack, or run?")
            if uchoice == 'attack' or uchoice == 'a':
                enemy.health = enemy.health - PlayerIG.attack
                print(PlayerIG.name + " has hit the " + enemy.name + "for " + str(PlayerIG.attack) + " damage!")
zombie = Enemy(3,7,'Slam','Zombie')
print("Welcome to Frank's battle simulator!")
print("Our contenders today are " + zombie.name + ", and " + PlayerIG.name +".")
print('Let the battle commence!')
Fight(zombie)