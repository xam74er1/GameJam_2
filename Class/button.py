import pygame
from pygame.locals import *

class Bouton:
    def __init__(self,image_path,x=0,y=0,sizex = 100,sizey=100):
        #charge limage
        self.image = pygame.image.load(image_path).convert_alpha()
        #la redimentione

        self.image = pygame.transform.scale(self.image,(sizex,sizey))

        self.rect =  self.image.get_rect()
        #on le place
        self.rect = self.rect.move(x,y)

        self.x = x
        self.y =y
        self.sizex = sizex
        self.sizey = sizey

        #si une image est dessu
        self.imageOver = 0

        #definir une actin as null

        self.action = 0

    def isInZone(self,x,y):
        return (self.rect.x<=x & x<=(self.rect.x+self.sizex)) & (self.rect.y<=y & y<=(self.rect.y+self.sizey))

#definir laction as realise dans le print
    def setButtonAction(self,action):
        self.action = action

    def actionB(self):

        if self.action()!=0:
             self.action()
        else:
            print("aucune action defini")


    def setImageOver(self,path):
        print(self.sizey)
        self.imageOver = pygame.image.load(path).convert_alpha()
        self.imageOver =pygame.transform.scale(self.imageOver,(self.sizex,self.sizey+20))


    def getImage(self):
        if self.imageOver and self.rect.collidepoint( pygame.mouse.get_pos() ):
            return self.imageOver
        else:
            return self.image