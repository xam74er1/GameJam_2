import pygame
from pygame.locals import *

class Bouton:
    def __init__(self,image_path,x=0,y=0,sizex = 0,sizey=0):
        #charge limage
        self.image = pygame.image.load(image_path).convert_alpha()
        #la redimentione

        self.image = pygame.transform.scale(self.image,(sizex,sizey))

        self.rect =  self.image.get_rect()
        self.x = x
        self.y =y
        self.sizex = sizex
        self.sizey = sizey



