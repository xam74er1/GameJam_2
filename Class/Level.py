import pygame
from pygame.locals import *
from Class.Coin import *
from Class.Walls import *
import env_var as env

class Level:

    def __init__(self, numlevel):
        self.walls = 0
        self.numlevel = numlevel
        self.coins = []
        self.generate()
        self.color = 0
        self.gravity = 0
        self.generate()
        try:
            self.background = pygame.image.load("sprites/Niveau "+str(self.numlevel)+" background.png").convert_alpha()
        except:
            self.background = pygame.image.load("sprites/Niveau 1 background.png").convert_alpha()

    def generate(self):
        with open("levels/"+str(self.numlevel)+".lvl", "r") as lvlfile:
            lvlstruct = []
            lvlstruct.append(Walls((0, 0), (20, 750)))
            lvlstruct.append(Walls((20, 0), (730, 20)))
            lvlstruct.append(Walls((730, 20), (20, 730)))
            lvlstruct.append(Walls((20, 730), (710, 20)))
            filezone=''
            for line in lvlfile:
                if line != '\n' and line != '' and line[0]!='#':
                    if line[:6] == 'Level:':
                        filezone='l'
                    elif line[:6] == 'Coins:':
                        filezone='p'
                    elif line[:6] == 'Color:':
                        filezone='c'
                    elif line[:8] == 'Gravity:':
                        filezone='g'
                    elif filezone == 'l':
                        x = int(line[:3])

                        y = int(line[4:7])
                        size_x = int(line[8:11])
                        size_y = int(line[12:15])
                        wall = Walls((x, y), (size_x, size_y))
                        lvlstruct.append(wall)
                    elif filezone == 'p':
                        coinX = int(line[:3])
                        coinY = int(line[4:7])

                        self.coins.append(Coin(coinX, coinY))
                    elif filezone == 'c':
                        self.color = (int(line[:3]),int(line[4:7]),int(line[8:11]))

                    elif filezone == 'g':
                        self.gravity = (float(line[:4]), float(line[5:9]))


            if self.color:
                for w in lvlstruct:
                    w.color = self.color
                    w.surface.fill(self.color)
            self.walls = lvlstruct

    def rezieBacground(self,x,y):
        self.background = pygame.transform.scale(self.background,(x,y))

    def printLvl(self, window):
        for wall in self.walls:
            window.blit(wall.surface, wall.pos)
        for coin in self.coins:
            window.blit(coin.image, (coin.x, coin.y))

    def resetLvl(self, window):
        if self.struct:
            for line in self.struct:
                for sprite in line:
                    sprite='0'
            self.printLvl(self, window)
            return 0
        else:
            return 'No level structure'

