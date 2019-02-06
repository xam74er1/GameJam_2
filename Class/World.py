from Class.Walls import *
import pygame
import Class.Coin
import Class.Level
from Class.Level import *
import env_var as env

class World:
    def __init__(self, frame, maxX, maxY):
        self.frame = frame
        self.maxX = maxX
        self.maxY = maxY
        self.gravity = 0
        self.listWall = []
        self.toUpdate = []
        self.level = 0
        self.levels = []

    def addWall(self, wall):
        self.listWall.append(wall)

    def draw(self):
        self.printWall()

    def printWall(self):

        for w in self.listWall:
            pygame.draw.rect(self.frame, w.color, w.rect)

    def initLevels(self):
        for i in range(0, env.max_levels):
            self.levels.append(Level(i+1))

    def nextLevel(self):
        self.level=self.levels[self.level]

