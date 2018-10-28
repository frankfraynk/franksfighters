from rpgplayer import Player
import random
p = Player('Ricardo')


class item:
    def __init__(self,name,cost,weight):
        self.name = name
        self.cost = cost
        self.weight = weight
        self.type = type

class weapon(item):
    def __init__(self,name,cost,weight,attack,type):
        self.name = name
        self.cost = cost
        self.weight = weight
        self.attack = attack
        self.type = type



class inventory:
    def __init__(self,player):
        self.wslot = weapon(None,None,None,None,None)
        self.aslot = [None]
        self.tslots = []
        self.storage = []
        self.player = player
        self.view()
    def view(self):
        print("Welcome to" + self.player.name + "'s' inventory, these are the items in their inventory: ")
        print("In storage: ")
        for item in self.storage:
            if type(item) is weapon:
                print(item.name, item.cost,item.weight,item.attack)
            else:
                print(item.name,item.cost,item.weight)
    def add(self,ita):
        self.storage.append(ita)
    def unequip(self,itu):
        if itu.name == self.wslot.name:
            self.storage.append(itu)
            self.wslot = None
    def equip(self,ifs):
        if self.wslot !=  None:
            self.unequip(self.wslot)
        if ifs in self.storage:
            if type(ifs) is weapon:
                self.wslot = ifs
                self.player.attacks.append(ifs.attack)
                self.storage.pop(self.storage.index(ifs))
i = inventory(p)
sword = weapon('sword',30,10,10,'p')
camp = item('camp',30,10)
i.add(sword)
i.add(camp)
i.view()
eou = input("do you want to equip or unequip? (e for equip u for unequip): ")
exit = False
while not exit:
    if eou == 'e':
        itte = input('what item to equip: ')
        if itte=='sword':
            i.equip(sword)
            print('Sword Equippied!')
