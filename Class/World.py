from Class.Walls import *
import pygame

class World:
    def __init__(self,frame,maxX,maxY,gravity):
        self.frame = frame
        self.maxX = maxX
        self.maxY = maxY
        self.gravity = gravity
        self.listWall = []
        self.toUpdate =[]

    def addWall(self,wall):
        self.listWall.append(wall)

    def draw(self):
        self.printWall()

    def printWall(self):

        for w in self.listWall:
            pygame.draw.rect(self.frame,w.color,w.rect)