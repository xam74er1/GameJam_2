import pygame
from Class.button import *
from pygame.locals import *
from JeuxEnCour import *
from pygame import font

# Changement page
def loadPerso1():
    return "perso1"

def loadPerso2():
    return "perso2"

def loadPerso3():
    return "perso3"

def quitGame():
    return "quit"

# list update
def updateimage(frame,array):
    for it in array:
        frame.blit(it.getImage(),it.rect)


#-----------Main -----------

def selection(fenetre):

    current_page = "selection"

    # Ouverture de la fenêtre Pygame


    perso1 = Bouton("sprites/Blob/Blopchon.png", 100, 150, 150, 150)
    perso1.setImageOver("sprites/Blob/Blopchon3.png")


    perso2 = Bouton("sprites/Blob/Blobette.png", 100, 300, 150, 150)
    perso2.setImageOver("sprites/Blob/Blobette animé.png")


    perso3 = Bouton("sprites/Blob/Ramblob.png",100, 450,150, 150)
    perso3.setImageOver("sprites/Blob/Ramblob animé.png")

    nom1 = Bouton("sprites/Title/Herve Blobchon.png", 300, 195, 407, 87)

    nom2 = Bouton("sprites/Title/Blobette.png", 300, 340, 407, 87)

    nom3 = Bouton("sprites/Title/Ramblob.png", 300, 500, 407, 87)



    #quitter = Bouton("sprites/Boutons/Jouer normal.png", 255, 640, 240, 86)
    #quitter.setImageOver("sprites/Boutons/Jouer animé.png")

    partie = 1
    fond = Level('m')

    newPerso = "perso1"
    while partie:
        if current_page == "selection":
            # Chargement et collage du fond
            fenetre.blit(fond.background,(0,0))
            fond.printLvl(fenetre)
            #fenetre.blit(fond, (0, 0))
            titre = pygame.transform.scale(pygame.image.load("sprites/Title/Logo.png"), (610, 130))

            # list de tout les truc as update
            arrayUpdate = []

            # list de tout les truc qui attendre un clique , equivant as a event listner pour les boutton
            arrayClick = []

            # Creation du bouton
            fenetre.blit(perso1.getImage(),perso1.rect)
            fenetre.blit(perso2.image,perso2.rect)
            fenetre.blit(perso3.image,perso3.rect)
            fenetre.blit(nom1.image, nom1.rect)
            fenetre.blit(nom2.image, nom2.rect)
            fenetre.blit(nom3.image, nom3.rect)
            #fenetre.blit(quitter.image,quitter.rect)

            # Affection de la fonction as mettre lorsque l'on fait l'action
            perso1.setButtonAction(loadPerso1)

            perso2.setButtonAction(loadPerso2)

            perso3.setButtonAction(loadPerso3)

            #quitter.setButtonAction(quitGame)

            # Rafraîchissement de l'écran
            pygame.display.flip()
            # BOUCLE INFINIE
            continuer = 1

            # Ajout de tout les trucs as update
            arrayUpdate.append(perso1)
            arrayUpdate.append(perso2)
            arrayUpdate.append(perso3)
            arrayUpdate.append(nom1)
            arrayUpdate.append(nom2)
            arrayUpdate.append(nom3)
            #arrayUpdate.append(quitter)

            # Ajout de tout les trucs qui attendent un event
            arrayClick.append(perso1)
            arrayClick.append(perso2)
            arrayClick.append(perso3)
            #arrayClick.append(quitter)

            while continuer:
                for event in pygame.event.get():  # Attente des événements
                    if event.type == QUIT:
                        partie = False

                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:  # Si clic gauche
                            for bt in arrayClick:
                                val = bt.isInZone(event.pos[0],event.pos[1])
                                if bt.isInZone(event.pos[0],event.pos[1]) :
                                    res = bt.action()
                                    if res =="quit":
                                        partie = False
                                    else:
                                        newPerso = res
                                        partie = False

                                    continuer = 0

                # Re-collage
                fenetre.blit(fond.background, (0, 0))
                fenetre.blit(titre, (70, 40))
                updateimage(fenetre,arrayUpdate)
                #fenetre.blit(perso, position_perso)
                # Rafraichissement
                pygame.display.flip()
                pygame.key.set_repeat(40,30)
    #---------Fin de perso ------
    if newPerso=="perso1":
        env.perso ="sprites/Blob/Blopchon.png"
    elif newPerso=="perso2":
        env.perso ="sprites/Blob/Blobette.png"
    elif newPerso=="perso3":
        env.perso ="sprites/Blob/Ramblob.png"