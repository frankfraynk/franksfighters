import random
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

    def attackPlayer(self,player):
        print("Enemy is swinging!")
        hit_chance = random.randint(5,25) + (self.lvl/2)
        if hit_chance >= (12+player.armor):
            player.health = player.health - self.dmg
            print('The ' + self.name + ' hit you for ' + str(self.dmg) + ' using ' + self.dtype + '!')
        else:
            print("The " + self.name + ' missed!')
