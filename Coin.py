import pygame
from pygame.locals import *

class Coin:
    visible=0
    img=0
    def __init__(self):
        self.img = pygame.image.load('sprites/coin.png').convert_alpha()

    def isVisible(self):
        return bool(self.visible)

    def setVisible(self,b):
        self.visible=b
