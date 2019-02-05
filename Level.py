import pygame
from pygame.locals import *


class Level:
    struct = 0

    def __init__(self, numlevel):
        self.numlevel = numlevel

    def generate(self):
        with open('levels/'+self.numlevel+".lvl", "r") as lvlfile:
            lvlstruct = []
            for line in lvlfile:
                line=[]
                for sprite in line:
                    if sprite != '\n':
                        line.append(sprite)
                    lvlstruct.append(line)
                self.struct = lvlstruct

    def printlvl(self, window):
        num_line=0
        for line in self.struct:
            num_col=0
            for sprite in line:
                x=num_col*16
                y=num_line*16
                window.blit('sprites/'+sprite+'.png', (x, y))
            num_col+=1
        num_line+=1

    def resetlvl(self,window):
        for line in self.struct:
            for sprite in line:
                sprite='0'
        self.printlvl(self,window)
#