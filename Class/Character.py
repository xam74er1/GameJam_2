import pygame
import Class.Coin
import env_var as env

class Character:
    def __init__(self,world, x=0, y=0, sizex=100, sizey=100):
        # charge limage
        self.image = pygame.image.load(env.perso).convert_alpha()
        # la redimentione

        self.image = pygame.transform.scale(self.image,(sizex,sizey))

        self.rect = self.image.get_rect()
        # on le place
        self.rect = self.rect.move(x, y)

        self.x = x
        self.y = y
        self.sizex = sizex
        self.sizey = sizey

        self.ax = 0
        self.ay = 0

        self.world = world

        self.coins = 0

        #pour les test
        self.fly = False

        self.tmp = False

        self.listAnimation = []
        self.anmationCount = 0
        self.generateAnimtation()

    def generateAnimtation(self):
        self.listAnimation.append(self.image)
        for i in range(1,4):

            try:
                img = pygame.image.load(
                    "sprites/Blob/Blopchon" + str(i) + ".png").convert_alpha()
            except:
                img = pygame.image.load("sprites/Blob/Blopchon.png").convert_alpha()

            img = pygame.transform.scale(img, (self.sizex, self.sizey))
            self.listAnimation.append(img)

    def animation(self):

            self.image = self.listAnimation[self.anmationCount]
            self.anmationCount+=1
            if self.anmationCount>3:
                self.anmationCount=0

    def addCoin(self):
        self.coins+=1

    def forceMove(self,x,y):

        #if(self.tmp):
            #self.tmp = False
            #print("new x " + str(x) + "new y " + str(y))


        self.rect = self.rect.move(x, y)
        self.x = self.rect.x
        self.y = self.rect.y

    def setAcceleration(self, x, y):
        self.ax = x
        self.ay =y

    def applyAcceleration(self, x, y):
        maxi = 15.0
        if self.ax>0:
            self.ax = min(self.ax+x,maxi)
        else:
            self.ax = max(self.ax + x, -1*maxi)
        if self.ay > 0:
            self.ay = min(self.ay + y, maxi)
        else:
            self.ay= max(self.ay + y, -1*maxi)
    def setPostion(self,x,y):
        self.rect.x = x
        self.rect.y = y
        self.x = self.rect.x
        self.y = self.rect.y

    def canMouve(self,w):
        nb = 5
        return self.fly or ((self.rect.left+nb > w.rect.right and self.rect.left < w.rect.right+nb))or (self.rect.right+nb > w.rect.left and self.rect.right < w.rect.left+nb) or ((self.rect.bottom+10 > w.rect.top and self.rect.bottom < w.rect.top+nb)or(self.rect.top +nb > w.rect.bottom and self.rect.top < w.rect.bottom + nb))

    def up(self,world):
        for w in world.level.walls:
            if self.world.gravity[1]==0 or self.canMouve(w):
                self.applyAcceleration(0,-8)
    def down(self,world):
        for w in world.level.walls:
            for w in world.level.walls:
                if self.world.gravity[1]==0 or self.canMouve(w):
                    self.applyAcceleration(0, 8)
    def left(self,world):
        for w in world.level.walls:
            if self.world.gravity[0]==0 or self.canMouve(w):
                self.applyAcceleration(-8, 0)
    def right(self,world):
        for w in world.level.walls:
            if self.world.gravity[0]==0 or self.canMouve(w):
                self.applyAcceleration(8, 0)

    def move(self):
        #print(" Debut ax " + str(self.ax) + " ay " + str(self.ay))
        self.forceMove(self.ax,self.ay)
        #Verifiaction rapide

        maxX = self.world.maxX
        maxY = self.world.maxY


        #le Max (sol )
        if(self.x+self.sizex>maxX):
            #print("Max x = " + str(maxX) + " x =" +  str(self.x) + " x ziez = " +  str(self.sizex) + " rect = " +  str(self.rect.x))
            self.forceMove(-1*(self.x+self.sizex-maxX),0)

            #rebon
            #self.ax =-self.ax

        if (self.y + self.sizey >= maxY):
            self.forceMove(0,-1 * (self.y + self.sizey - maxY))
            #self.ay =-self.ay

        #Le min

        if self.x<0:
            self.forceMove(-self.x,0)
            # rebon
            #self.ax = -self.ax
        if self.y<0:
            self.forceMove(0,-self.y)
           # self.ay = -self.ay

        #Reduire acelreation droite et gauche


        gravitmode = 1

        if gravitmode ==1:
            self.ax *= 0.99
            self.ay *= 0.99
        else:
            if(self.ax<0):
                self.ax+=0.1
            elif self.ax>0:
                self.ax-=0.1

            if (self.ay < 0):
                self.ay += 0.1
            elif self.ay > 0:
                self.ay -= 0.1

        #Check si il est en collistion

        try:
            for w in self.world.level.walls:
                if self.rect.colliderect(w):

                    #defintion des centre
                    mcX = self.rect.x+(self.sizex/2)
                    mcY = self.rect.y+(self.sizey/2)

                    scX = w.rect.x+(w.rect.size[0]/2)
                    scY = w.rect.y+(w.rect.size[1]/2)

                    minX = w.rect.x
                    minY = w.rect.y
                    maxX = w.rect.x+(w.rect.size[0])
                    maxY = w.rect.y+(w.rect.size[1])

                    if mcX>minX and mcX<maxX:
                        self.ay*=-1
                        if mcY>scY:
                            self.setPostion(self.x,maxY)
                        else:
                            self.setPostion(self.x,minY-self.sizey)
                    if mcY>minY and mcY<maxY:
                        self.ax*=-1
                        if mcX>scX:
                            self.setPostion(maxX, self.y)
                        else:
                            self.setPostion(minX - self.sizex, self.y)

                    #break
        except:
            0

        cToRemove=0
        try:
            #Recuperation des coins
            for c in self.world.level.coins:
                if self.rect.colliderect(c):
                    c.visible=0
                    self.world.sonCoin.play()
                    self.world.toUpdate.append(c)
                    cToRemove=c
                    break

            if cToRemove:
                self.addCoin()
                self.world.level.coins.remove(cToRemove)
        except:
            0
       # print("Fin ax " + str(self.ax) + " ay " + str(self.ay))
        #print("------------------------------------------")
        return self.rect

       # print("x="+str(self.x)+"y = "+str(self.y)+" ax = "+str(self.ax)+" ay "+str(self.ay)+"rect x "+str(self.rect.x)+" rect y "+str(self.rect.y))

