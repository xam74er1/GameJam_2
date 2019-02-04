import pygame
from button import *
from pygame.locals import *



#list update

def updateimage(frame,array):
    for it in array:
        frame.blit(it[0],it[1])

def testButton():
    print("ce test as marche ")


#-----------Main -----------

pygame.init()

# Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))

# Chargement et collage du fond
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0, 0))

# Chargement et collage du personnage
perso = pygame.image.load("perso.png").convert_alpha()

position_perso = perso.get_rect()
position_perso = position_perso.move(100,100)
fenetre.blit(perso, position_perso)

#list de tout les truc as update
arrayUpdate = [];

#list de tout les truc qui attendre un clique , equivant as a event listner pour les boutton
arrayClick = []

#Creation du bouton

b = Bouton("images/Bouton1.png",100,100,300,300)
fenetre.blit(b.image,b.rect)

#Afection de la fonction as mettre lorsque lon fait laction
act = testButton
b.setButtonAction(act)

# Rafraîchissement de l'écran
pygame.display.flip()
# BOUCLE INFINIE
continuer = 1

#Ajout de tout les truc as update
arrayUpdate.append((fond,(0,0)))
arrayUpdate.append((b.image,b.rect))
arrayUpdate.append((perso,position_perso))

#Ajout de tout les truc qui attende un event 
arrayClick.append(b)


while continuer:

    for event in pygame.event.get():  # Attente des événements
        if event.type == QUIT:
            continuer = 0



        if event.type == MOUSEBUTTONDOWN:

            if event.button == 1:  # Si clic gauche

                for bt in arrayClick:

                    val = bt.isInZone(event.pos[0],event.pos[1])

                    if bt.isInZone(event.pos[0],event.pos[1]) :
                        print("dans la zone")
                        bt.action()

    # Re-collage
    #fenetre.blit(fond, (0, 0))

    updateimage(fenetre,arrayUpdate)
    #fenetre.blit(perso, position_perso)
    # Rafraichissement
    pygame.display.flip()
    pygame.key.set_repeat(40,30)


