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
    def attack():
        global enemy
        
PlayerIG = Player('Jim')

class Enemy:
    def __init__(self,lvl,dmg,dtype,name):
        self.lvl = lvl
        self.dmg = dmg
        self.dtype = dtype
        self.name = name
        self.speed = random.randint(2,5)
    def enemySpawn():
        print(name + " has spawned! It has a size of " + size +'.')
    def attackPlayer():
        print("Enemy is swinging!")
        hitchance = random.randint(1,20) + (lvl/2)
        if hitchance >= (12+PlayerIG.armor):
            PlayerIG.health = PlayerIG.health - self.dmg
class Fight:
    def __init__(player,enemy):
        Player.__init__(self,name)
        Enemy.__init__(self,name)
        self.player = p
        self.enemy = e
    def detFirst():
        if player.speed

zombie = Enemy(3,7,'Slam','Zombie')
print("Welcome to Frank's battle simulator!")
print("Our contenders today are " + zombie.name + ", and " + PlayerIG.name +".")
print(Let the battle commence
