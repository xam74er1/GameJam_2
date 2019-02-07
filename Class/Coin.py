import pygame

class Coin:

    def __init__(self, x=0, y=0, sizeX=40, sizeY=40):
        self.image = pygame.image.load('sprites/Coins/Coin.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (sizeX, sizeY))
        self.image.set_alpha(192)
        self.visible = 1
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, sizeX, sizeY)
#

