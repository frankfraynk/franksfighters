import random
from typing import List


class wMap:
    def __init__(self):
        self.r, self.c = 5, 5
        self.mcoords = [[0 for i in range(self.r)] for x in range(self.c)]
        self.player
    def coord_value(self):
        for i in range(self.r):
           for x in range(self.c):
                self.mcoords[i][x] = random.randint(1,3)
                self.player  = self.mcoords[self.c - 1][0] = 0

    def player_move(self, direction):
        if direction == 'north' or 'n':
            self.player = self.mcoords

    def draw_map(self):
        for x in range(self.c):
            print("\n")
            for i in range(self.r):
                if self.mcoords[x][i] == 0:
                    print('p', end="   ")
                else:
                    print('~', end="   ")
        direction = input("Which direction do you want to move?")





m = wMap()


m.coord_value()


m.draw_map()


