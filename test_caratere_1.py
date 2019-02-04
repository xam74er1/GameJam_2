import pygame
from button import *
from Character import *
from pygame.locals import *


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
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0, 0))



arrayUpdate = [];
arrayClick = []




# Rafraîchissement de l'écran
pygame.display.flip()
# BOUCLE INFINIE
continuer = 1


perso = Character("perso.png",MAX_X/2,MAX_Y-100,40,40)
fenetre.blit(perso.image,perso.rect)

arrayUpdate.append((fond,(0,0)))




while continuer:

    for event in pygame.event.get():  # Attente des événements
        if event.type == QUIT:
            continuer = 0

        if event.type == KEYDOWN:
            print("touche")
            if event.key == K_DOWN:
                perso.aplyAceleration(0,0)
            if event.key == K_UP:
                perso.aplyAceleration(0,-10)
            if event.key == K_LEFT:
                perso.aplyAceleration(-4, 0)
            if event.key == K_RIGHT:
                perso.aplyAceleration(4, 0)
    #Gravite
    perso.aplyAceleration(0,0.9)


    perso.move(MAX_X,MAX_Y)


    # Re-collage
    #fenetre.blit(fond, (0, 0))

    updateimage(fenetre,arrayUpdate)
    fenetre.blit(perso.image, perso.rect)

    #fenetre.blit(perso, position_perso)
    # Rafraichissement
    pygame.display.flip()
    pygame.key.set_repeat(40,30)
    pygame.time.Clock().tick(30)


