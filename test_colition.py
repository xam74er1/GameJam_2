import pygame
from Class.button import *
from Class.Character import *
from pygame.locals import *
from Class.World import *
from Class.Walls import *


MAX_X =640
MAX_Y =480

#list update

def updateimage(frame,array):
    for it in array:
        frame.blit(it[0],it[1])

def testButton():
    print("ce test as marche ")




#-----------Main -----------

pygame.init()

# Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((MAX_X,MAX_Y ))



# Chargement et collage du fond
#fond = pygame.image.load("images/background.jpg").convert()
#fenetre.blit(fond, (0, 0))



arrayUpdate = [];
arrayClick = []
gravity = (0,0.9)

world = World(fenetre,MAX_X,MAX_Y,gravity)

# Rafraîchissement de l'écran
pygame.display.flip()
# BOUCLE INFINIE
continuer = 1


perso = Character("sprites/perso.png",world,MAX_X/2,MAX_Y-100,32,32)
fenetre.blit(perso.image,perso.rect)

#arrayUpdate.append((fond,(0,0)))

#defintion des walls

world.addWall(Walls((200,400),(200,30),(0,255,0)))
world.addWall(Walls((400,400),(20,80),(255,0,0)))
world.addWall(Walls((0,0),(20,750),(242,0,255)))
world.addWall(Walls((0,0),(750,20),(242,0,255)))
world.addWall(Walls((730,0),(20,750),(242,0,255)))
world.addWall(Walls((0,730),(750,20),(242,0,255)))
pygame.key.set_repeat(40,100)

while continuer:

    for event in pygame.event.get():  # Attente des événements
        if event.type == QUIT:
            continuer = 0
        gravityForce = 0.5
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                perso.aplyAceleration(0,4)
            if event.key == K_UP:
                perso.aplyAceleration(0,-10)
            if event.key == K_LEFT:
                perso.aplyAceleration(-4, 0)
            if event.key == K_RIGHT:
                perso.aplyAceleration(4, 0)
            if event.key == K_F1:
                world.gravity = (0,gravityForce)
            if event.key == K_F2:
                world.gravity =(0,-gravityForce)
            if event.key == K_F3:
                world.gravity=(gravityForce,0)
            if event.key == K_F4:
                world.gravity=(-gravityForce,0)

    #Gravite
    perso.move()
    perso.aplyAceleration(world.gravity[0],world.gravity[1])





    # Re-collage
    #fenetre.blit(fond, (0, 0))

    updateimage(fenetre,arrayUpdate)
    world.draw()
    fenetre.blit(perso.image, perso.rect)

    #fenetre.blit(perso, position_perso)
    # Rafraichissement
    pygame.display.flip()

    pygame.time.Clock().tick(30)


