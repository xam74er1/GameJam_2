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

    def generate(self):
        with open("levels/"+str(self.numlevel)+".lvl", "r") as lvlfile:
            lvlstruct = []
            lvlstruct.append(Walls((0, 0), (20, 750)))
            lvlstruct.append(Walls((0, 0), (750, 20)))
            lvlstruct.append(Walls((730, 0), (20, 750)))
            lvlstruct.append(Walls((0, 730), (750, 20)))
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
                        coinY = int(line[-4:])

                        self.coins.append(Coin(coinX, coinY))
                    elif filezone == 'c':
                        self.color = (int(line[:3]),int(line[4:7]),int(line[8:11]))

                    elif filezone == 'g':
                        self.gravity = (float(line[:3]), float(line[4:7]))


            if self.color:
                for w in lvlstruct:
                    w.color=self.color
            self.walls = lvlstruct


    def printLvl(self, window):
        """
        num_line = 0
        for line in self.struct:
            num_col = 0
            for sprite in line:
                x = num_col*env.sprite_size
                y = num_line*env.sprite_size
                window.blit(pygame.image.load('sprites/' + sprite + "_flat.png").convert_alpha(), (x, y))
                num_col += 1
            num_line += 1
        for coin in self.coins:
            window.blit(coin.img, (coin.x, coin.y))
        """
        """for rect in self.struct:
            pygame.draw.rect(window, (0, 0, 255), rect)"""
        for wall in self.walls:
            pygame.draw.rect(window, wall.color, wall.rect)


    def printWall(self,window):
        for wall in self.walls:
            pygame.draw.rect(window, wall.color, wall.rect)
    def printCoin(self,window):

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

