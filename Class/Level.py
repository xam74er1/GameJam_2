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
        self.color = 0
        self.gravity = 0
        self.alpha = 0

        self.generate()

        #piece qui tourne
        self.countPrintPiece = 0
        self.etaPrintPiece = 0
        self.UniqueCoin = True

        try:
            self.background = pygame.image.load("sprites/Background/Niveau "+str(self.numlevel)+".png").convert_alpha()
        except:
            self.background = pygame.image.load("sprites/Background/Niveau m.png").convert_alpha()

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
                       #ajout des coin en double
                        self.coins.append(Coin(coinX, coinY))
                    elif filezone == 'c':
                        self.color = (int(line[:3]),int(line[4:7]),int(line[8:11]))
                        self.alpha = int(line[12:15])

                    elif filezone == 'g':
                        self.gravity = (float(line[:4]), float(line[5:9]))


            if self.color and self.alpha:
                for w in lvlstruct:
                    w.color = self.color
                    w.surface.fill(self.color)
                    w.surface.set_alpha(self.alpha)
            self.walls = lvlstruct


    def rezieBacground(self,x,y):
        self.background = pygame.transform.scale(self.background,(x,y))

    def printLvl(self, window,wold):
        for wall in self.walls:
            window.blit(wall.surface, wall.pos)

        for coin in self.coins:
            window.blit(coin.image, (coin.x, coin.y))
        if wold  :
            self.countPrintPiece += 1
            if self.countPrintPiece >5:
                self.countPrintPiece = 0
                #print("A "+str(self.etaPrintPiece))
                for coin in self.coins:
                    coin.image = wold.listCoinImage[self.etaPrintPiece]
                self.etaPrintPiece += 1
                if self.etaPrintPiece > 4:
                    self.etaPrintPiece = 0
                    #print("reste piece ")
