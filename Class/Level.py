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

    def generate(self):
        with open("levels/"+str(self.numlevel)+".lvl", "r") as lvlfile:
            lvlstruct = []
            lvlstruct.append(Walls((0, 0), (20, 750), (242, 0, 255)))
            lvlstruct.append(Walls((0, 0), (750, 20), (242, 0, 255)))
            lvlstruct.append(Walls((730, 0), (20, 750), (242, 0, 255)))
            lvlstruct.append(Walls((0, 730), (750, 20), (242, 0, 255)))
            filezone=''
            for line in lvlfile:
                if line != '\n' and line != '':
                    if line[:6] == 'Level:':
                        filezone='l'
                    elif line[:6] == 'Coins:':
                        filezone='c'
                    elif filezone == 'l':
                        x = int(line[:3])
                        y = int(line[4:7])
                        size_x = int(line[8:11])
                        size_y = int(line[12:15])
                        wall = Walls((x, y), (size_x, size_y), (int(line[16:19]), int(line[20:23]), int(line[24:27])))
                        lvlstruct.append(wall)

                    elif filezone == 'c':
                        coinX = int(line[:3])
                        coinY = int(line[-3:])
                        self.coins.append(Coin(coinX, coinY))

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

    def resetLvl(self, window):
        if self.struct:
            for line in self.struct:
                for sprite in line:
                    sprite='0'
            self.printLvl(self, window)
            return 0
        else:
            return 'No level structure'

