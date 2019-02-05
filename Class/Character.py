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

        self.tmp = False

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
        self.ax += x
        self.ay += y
    def setPostion(self,x,y):
        self.rect.x = x
        self.rect.y = y
        self.x = self.rect.x
        self.y = self.rect.y

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

                rcX = mcX-scX
                rcY = mcY-mcY

                #print("rcx = " + str(rcX) + "rcy = " + str(rcY))
                #print("mcY : "+str(mcY)+" scY "+str(scY))
                #print(" x : "+str(self.x)+" y : "+str(self.y)+" top :"+str(w.rect.top)+" bottom "+str(w.rect.bottom)+" mcX")

               #--------------------------------------------
               #V2 colition

               # print("x=" + str(self.x) + "y = " + str(self.y) + " ax = " + str(self.ax) + " ay " + str(
                #self.ay) + "rect x " + str(self.rect.x) + " rect y " + str(self.rect.y))
                #Si la boule est dans les x
                if ((self.x+self.sizex)>=(w.rect.x) and (self.x+self.sizex)<=(w.rect.x+w.rect.size[0])) or ((self.x)>=(w.rect.x) and (self.x)<=(w.rect.x+w.rect.size[0])):
                  #pour evite de passe en bas
                    if self.y>w.rect.y and self.y+self.sizey>w.rect.bottom:
                        print("Z")
                        self.ay =0
                        self.setPostion(self.x,w.rect.top+self.sizey)
                    #print("C1"+str(self.y > w.rect.y+w.size[1])+" C2"+str(self.y+self.sizey<w.rect.bottom))
                    if self.y < w.rect.bottom and self.y+self.sizey<w.rect.bottom:
                        print("Q2")
                        self.ay =0
                        self.setPostion(self.x,w.rect.top-w.size[1])

                if ((self.y + self.sizey) >= (w.rect.y) and (self.y + self.sizey) <= (w.rect.y + w.rect.size[1])) or (
                        (self.y) >= (w.rect.y) and (self.y) <= (w.rect.y + w.rect.size[1])):
                    # pour evite de passe en bas
                    if self.x > w.rect.x and self.x + self.sizex > w.rect.left:
                        print("Z")
                        self.ay = 0
                        self.setPostion(w.rect.x + self.sizex,self.y)
                    # print("C1"+str(self.y > w.rect.y+w.size[1])+" C2"+str(self.y+self.sizey<w.rect.bottom))
                    if self.y < w.rect.bottom and self.y + self.sizey < w.rect.bottom:
                        print("Q2")
                        self.ay = 0
                        self.setPostion(self.x, w.rect.top - w.size[1])






                """
                #((self.x+self.sizex)>=(w.rect.x) and (self.x+self.sizex)<=(w.rect.x+w.rect.size[0])) or ((self.x)>=(w.rect.x) and (self.x)<=(w.rect.x+w.rect.size[0])):
                #Si le bas touche le haut
               #& ((int(self.y)+self.sizey) < w.rect.y) & (self.x > w.rect.y)
                if (mcY<scY) :
                    print("Z")
                   # print("new x " + str(self.x) + "new y " + str(self.y))
                    #self.forceMove(0,self.y-w.rect.top)
                    print("actual postion "+str(self.rect)+" possible : "+str(w.rect.x+self.sizex))
                    self.setPostion(self.x,w.rect.x+self.sizex)
                    print("actual postion " + str(self.rect) + " possible : " + str(w.rect.x + self.sizex))
                    #self.ay = -self.ay*0.9
                    self.ay=0
                   #& (int(self.y+self.sizey) > w.rect.y+w.pos[1]) & (self.y < w.rect.y+w.pos[1])
                if (mcY>scY)  :
                    print("S")
                    #self.setPostion(self.x,w.rect.bottom)
                    self.forceMove(0, w.rect.bottom-self.y)
                    #self.ay = -self.ay*0.9
                    self.ay=0

                   # print("new x " + str(self.x) + "new y " + str(self.y))
                    #print("S")
                if mcX<scX:

                    print("D")
                    self.forceMove((self.x+self.sizex)-w.rect.right,0)
                    #self.ax = -self.ax*0.9
                    self.ax = 0


                if mcX>scX:
                    print("Q")

                    #self.forceMove(w.rect.right-self.x, 0)
                    self.setPostion(w.rect.x+w.size[0],self.y)


                    #self.ax = -self.ax*0.9
                    self.ax=0"""
                break

        cToRemove=0
        for c in self.world.level.coins:
            if self.rect.colliderect(c):
                print('collision coin')
                c.visible=0
                self.world.toUpdate.append(c)
                cToRemove=c
                break

        if cToRemove:
            self.world.level.coins.remove(cToRemove)

        return self.rect

       # print("x="+str(self.x)+"y = "+str(self.y)+" ax = "+str(self.ax)+" ay "+str(self.ay)+"rect x "+str(self.rect.x)+" rect y "+str(self.rect.y))

