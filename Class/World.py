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
        self.timer = 179
        

    def addWall(self, wall):
        self.listWall.append(wall)

    def initLevels(self):
        for i in range(0, env.max_levels):
            self.levels.append(Level(i+1))


    def nextLevel(self):
        self.level.rezieBacground(self.maxX,self.maxY)
        if self.level.numlevel < env.max_levels:
            self.level = self.levels[self.level.numlevel]
            self.gravity = self.level.gravity
            return True
        else:
           return False

    def aplyTime(self):
        self.timer -=1
    def getTimeFormated(self):
        min = int(self.timer/60)
        sec = self.timer%60
        if(sec>9):
            return str(min)+":"+str(sec)
        else:
            return str(min) + ":0" + str(sec)