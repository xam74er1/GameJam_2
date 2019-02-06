import pygame
from random import randint
from pygame.locals import *

def paint():
    fenetre.blit(black,(0,0))
    for o in list:
        fenetre.blit(o[0], o[1])

def pretiprint(nb):
    if(nb<10):
        return "00"+str(nb)
    if(nb<100):
        return "0"+str(nb)
    return str(nb)

def addWall(pos,size):
    surface = pygame.Surface(size)
    surface.fill((255, 0, 0))
    list.append((surface, pos))

def loadLvl(path):
    addWall((0, 0), (20, 750))
    addWall((20, 0), (730, 20))
    addWall((730, 20), (20, 730))
    addWall((20, 730), (710, 20))
    with open(path, "r") as lvlfile:
        for line in lvlfile:
            if line != '\n' and line != '' and line[0] != '#':
                if line[:6] == 'Level:':
                    filezone = 'l'
                elif line[:6] == 'Coins:':
                    filezone = 'p'
                elif line[:6] == 'Color:':
                    filezone = 'c'
                elif line[:8] == 'Gravity:':
                    filezone = 'g'
                elif filezone == 'l':
                    x = int(line[:3])

                    y = int(line[4:7])
                    size_x = int(line[8:11])
                    size_y = int(line[12:15])
                    surface = pygame.Surface((size_x, size_y))
                    # rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
                    surface.fill((255, 0, 0))
                    list.append((surface, (x, y)))


pygame.init()

fenetre = pygame.display.set_mode((750, 750))

"""
#----------TUTO -----

Garde la souri enfon pour cree des mur 

Apyer sur P pour print la trace 

POur enleve un rectangle : Mette la souri et apyer sur R

Pour charge un niveaux deja existant : press L et rentre le num du level

Apyer sur W pour genere les 4 mur

Apyer sur F pour mettre une piece 

"""





continuer = 1

start = False
debut = (0,0)
fin = (0,0)
list = []

black = pygame.Surface((750, 750))
black.fill((0, 0, 0))

while continuer:
    paint()
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_p:
                print("---------------------------")
                for w in list:
                    sx = w[0].get_rect().right
                    sy =w[0].get_rect().bottom
                    dx = w[1][0]
                    dy = w[1][1]
                    print(pretiprint(dx)+" "+pretiprint(dy)+" "+pretiprint(sx)+" "+pretiprint(sy)+" 128")
            if event.key == K_r:

                for w in list:
                    rt = pygame.Rect(w[1][0],w[1][1],w[0].get_rect().right,w[0].get_rect().bottom)
                    if rt.collidepoint(pygame.mouse.get_pos()):
                        list.remove(w)
            if event.key == K_l:
                res = input("Insre le num du level")
                path ="levels/"+str(res)+".lvl"
                loadLvl(path)
            #Si sur W
            if event.key == 122:

                addWall((0, 0), (20, 750))
                addWall((20, 0), (730, 20))
                addWall((730, 20), (20, 730))
                addWall((20, 730), (710, 20))

            if event.key == K_f:
                surface = pygame.Surface((40, 40))
                surface.fill((252, 252, 0))
                #WIP

        if event.type == pygame.MOUSEBUTTONUP:
            try:
                fin = pygame.mouse.get_pos()
                #print(" debut = " + str(debut) + " fin = " + str(fin))

                sizeX = debut[0] - fin[0]
                sizeY = debut[1] - fin[1]

                surface = pygame.Surface((-sizeX, -sizeY))
                # rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
                surface.fill((randint(0, 255), randint(0, 255), randint(0, 255)))
                list.append((surface, debut))
                fenetre.blit(surface, debut)
                start = False
            except:
                1
        if event.type == pygame.MOUSEBUTTONDOWN:
            start = True
            debut = pygame.mouse.get_pos()

    if  pygame.mouse.get_pressed()[0] and start :
        fin = pygame.mouse.get_pos()
       # print(" debut = " + str(debut) + " fin = " + str(fin))

        sizeX = debut[0] - fin[0]
        sizeY = debut[1] - fin[1]

        try:
            surface = pygame.Surface((-sizeX, -sizeY))
            # rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
            surface.fill((0,0,255))
            fenetre.blit(surface, debut)
        except:
            1



    pygame.display.flip()

pygame.quit()

