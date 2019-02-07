from Class.Walls import *
import pygame
import Class.Coin
import Class.Level
import time
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
        self.timeMax = 180
        self.timer = self.timeMax
        self.debutTime = 0
        #load des sound
        self.sonCoin = pygame.mixer.Sound("Sounds/Coin.wav")
        self.sonNextLeve = pygame.mixer.Sound("Sounds/Nextlevel.wav")

    def addWall(self, wall):
        self.listWall.append(wall)

    def initLevels(self):

        for i in range(0, env.max_levels):
            self.levels.append(Level(i+1))

    def startTimer(self):
        self.debutTime = time.time()

    def nextLevel(self):
        self.level.rezieBacground(self.maxX,self.maxY)
        if self.level.numlevel < env.max_levels:
            self.sonNextLeve.play()
            self.level = self.levels[self.level.numlevel]
            self.gravity = self.level.gravity
            return True
        else:
           return False

    def aplyTime(self):

        self.timer =self.timeMax - int(time.time()-self.debutTime)
    def getTimeFormated(self):
        min = int(self.timer/60)
        sec = self.timer%60
        if(sec>9):
            return str(min)+":"+str(sec)
        else:
            return str(min) + ":0" + str(sec)