import pygame
from pygame.locals import *
from Class.Coin import *
import env_var as env

class Level:

    def __init__(self, numlevel):
        self.struct = 0
        self.numlevel = numlevel
        self.coins = []
        self.generate()

    def generate(self):
        with open('levels/'+self.numlevel+".lvl", "r") as lvlfile:
            lvlstruct = []
            filezone=''
            for line in lvlfile:
                if line != '\n' and line != '':
                    if line == 'Level:\n' :
                        filezone='l'
                    elif line == 'Coins:\n':
                        filezone='c'
                    elif filezone == 'l':
                        structline=[]
                        for sprite in line:
                            if sprite != '\n':
                                structline.append(sprite)
                            lvlstruct.append(structline)
                        self.struct = lvlstruct
                    elif filezone == 'c':
                        coinX = int(line[:3])
                        coinY = int(line[-3:])
                        self.coins.append(Coin(coinX, coinY))



    def printLvl(self, window):
        num_line = 0
        for line in self.struct:
            num_col = 0
            for sprite in line:
                x = num_col*env.sprite_size
                y = num_line*env.sprite_size
                window.blit(pygame.image.load('sprites/' + sprite + ".png").convert_alpha(), (x, y))
            num_col += 1
        num_line += 1
        for coin in self.coins:
            window.blit(coin.img, (coin.x, coin.y))

    def resetLvl(self, window):
        if self.struct:
            for line in self.struct:
                for sprite in line:
                    sprite='0'
            self.printLvl(self, window)
            return 0
        else:
            return 'No level structure'

