import random
from typing import List
from src import rpgplayer, fight, rpgenemy
import numpy


class wMap:
    def __init__(self,x,y,player):
        self.y = y
        self.x = x
        self.player = player
    def drawMap(self):
        map = numpy.array([[random.randint(1,3) for i in range(self.x)]for j in range(self.y)])
        self.map = map
        map[0][len(map)] = 0
        px,py = numpy.where(map == 0)
        self.px = px
        self.py = py
        print(px,py)
        for j in range(self.x):
            print()
            print()
            for i in range(self.y):
                if map[i][j] != 0:
                    print('~', end="     ")
                else:
                    print('V', end="     ")
    def movePlayer(direction):
        self.map[self.px][self.py] = '/'
        if direction == 'west' or direction == 'w':
            enc = self.map[self.px-1][self.py]
            self.map[self.px-1][self.py] = 0
        if direction == 'east' or direction == 'e':
            enc = self.map[self.px-1][self.py]
            self.map[self.px+1][self.py] = 0
        if direction == 'north' or direction == 'n':
            enc = self.map[self.px-1][self.py]
            self.map[self.px][self.py-1] = 0
        if direction == 'south' or direction == 's':
            enc = self.map[self.px-1][self.py]
            self.map[self.px][self.py+1] = 0
    def encounter(val):
        if val == 1:
            fight.Prefight()
        elif val == 2:
            Store()
        elif val == 3:
            pass

wMap(5,4,PlayerIG).drawMap()
