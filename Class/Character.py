import pygame
import Class.Coin

class Character:
    def __init__(self, image_path,world, x=0, y=0, sizex=100, sizey=100):
        # charge limage
        self.image = pygame.image.load(image_path).convert()
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

    def forceMove(self,x,y):

        self.rect = self.rect.move(x, y)
        self.x = self.rect.x
        self.y = self.rect.y

    def setAcceleration(self, x, y):
        self.ax = x
        self.ay =y

    def applyAcceleration(self, x, y):
        self.ax += x
        self.ay += y


#Verife que sa ne sort pas de la Zone

    def move(self):
        self.forceMove(self.ax,self.ay)
        #Verifiaction rapide

        maxX = self.world.maxX
        maxY = self.world.maxY

        #le Max (sol )
        if(self.x+self.sizex>maxX):
            #print("Max x = " + str(maxX) + " x =" +  str(self.x) + " x ziez = " +  str(self.sizex) + " rect = " +  str(self.rect.x))
            self.forceMove(-1*(self.x+self.sizex-maxX),0)

            #rebon
            self.ax =-self.ax

        if (self.y + self.sizey >= maxY):
            self.forceMove(0,-1 * (self.y + self.sizey - maxY))
            self.ay =-self.ay

        #Le min

        if self.x<0:
            self.forceMove(-self.x,0)
            # rebon
            self.ax = -self.ax
        if self.y<0:
            self.forceMove(0,-self.y)
            self.ay = -self.ay

        #Reduire acelreation droite et gauche


        gravitmode = 0

        if gravitmode ==1:
            self.ax *= 0.95
            self.ay *= 0.95
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

        for w in self.world.listWall:
            if self.rect.colliderect(w):
               # self.ax = 0
                #self.ay = 0
               #si il est en haut

                #defintion des centre
                mcX = self.rect.x+(self.sizex/2)
                mcY = self.rect.y+(self.sizey/2)

                scX = w.rect.x+(w.rect.size[0]/2)
                scY = w.rect.y+(w.rect.size[1]/2)


                #print("mcY : "+str(mcY)+" scY "+str(scY))

                #Si le bas touche le haut
                if mcY<scY :

                    self.ay = -self.ay
                if mcY>scY :
                    self.ay = -self.ay
                if mcX<scX:
                    self.ax = -self.ax
                if mcX>scX:
                    self.ax = -self.ax


        cToRemove=0
        for c in self.world.level.coins:
            if self.rect.colliderect(c):
                print('collision coin')
                c.visible=0
                cToRemove=c
                break

        if cToRemove:
            self.world.level.coins.remove(cToRemove)

        return self.rect

       # print("x="+str(self.x)+"y = "+str(self.y)+" ax = "+str(self.ax)+" ay "+str(self.ay)+"rect x "+str(self.rect.x)+" rect y "+str(self.rect.y))

