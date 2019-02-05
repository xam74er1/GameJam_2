import pygame

class Coin:

    def __init__(self, x=0, y=0):
        self.image = pygame.image.load('sprites/coin.png').convert_alpha()
        self.visible = 1
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
#

