import pygame

class Character:
    def __init__(self, image_path, x=0, y=0, sizex=100, sizey=100):
        # charge limage
        self.image = pygame.image.load(image_path).convert_alpha()
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

    def forceMove(self,x,y):

        self.rect = self.rect.move(x, y)
        self.x = self.rect.x
        self.y = self.rect.y

    def setAceleration(self,x,y):
        self.ax = x
        self.ay =y

    def aplyAceleration(self,x,y):
        self.ax += x
        self.ay += y


#Verife que sa ne sort pas de la Zone

    def move(self,maxX,maxY):
        self.forceMove(self.ax,self.ay)
        #Verifiaction rapide

        #le Max (sol )
        if(self.x+self.sizex>maxX):
            print("Max x = " + str(maxX) + " x =" +  str(self.x) + " x ziez = " +  str(self.sizex) + " rect = " +  str(self.rect.x))
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



       # print("x="+str(self.x)+"y = "+str(self.y)+" ax = "+str(self.ax)+" ay "+str(self.ay)+"rect x "+str(self.rect.x)+" rect y "+str(self.rect.y))

