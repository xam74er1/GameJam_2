import pygame
from Class.button import *
from pygame.locals import *
from JeuxEnCour import *
from pygame import font
import env_var as env


# Changement page
def loadMenu():
    return "menu"

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

def createLibPerso():
    perso = env.perso

    img = pygame.image.load(perso).convert_alpha()
    img = pygame.transform.scale(img,(env.sprite_size,env.sprite_size))
    img2 = pygame.transform.rotate(img, 90)
    img3 = pygame.transform.rotate(img, 180)
    img4 = pygame.transform.rotate(img, 270)
    img_flat = pygame.image.load(perso[:-4]+' animé.png').convert_alpha()
    img_flat= pygame.transform.scale(img_flat, (env.sprite_size, env.sprite_size))
    img_flat2 = pygame.transform.rotate(img_flat, 90)
    img_flat3 = pygame.transform.rotate(img_flat, 180)
    img_flat4 = pygame.transform.rotate(img_flat, 270)
    bottom = [img, img_flat]
    left = [img2, img_flat2]
    top = [img3, img_flat3]
    right = [img4, img_flat4]

    env.lib_perso.append(bottom)
    env.lib_perso.append(left)
    env.lib_perso.append(top)
    env.lib_perso.append(right)


#-----------Main -----------

def selection(fenetre):

    current_page = "selection"

    # Ouverture de la fenêtre Pygame

    perso1 = Bouton("sprites/Blob/Blopchon.png", 100, 150, 150, 150)
    perso1.setImageOver("sprites/Blob/Blopchon animé.png")

    perso2 = Bouton("sprites/Blob/Blobette.png", 100, 300, 150, 150)
    perso2.setImageOver("sprites/Blob/Blobette animé.png")

    perso3 = Bouton("sprites/Blob/Ramblob.png",100, 450,150, 150)
    perso3.setImageOver("sprites/Blob/Ramblob animé.png")

    nom1 = Bouton("sprites/Title/Herve Blobchon.png", 300, 195, 407, 87)

    nom2 = Bouton("sprites/Title/Blobette.png", 300, 340, 407, 87)

    nom3 = Bouton("sprites/Title/Ramblob.png", 300, 500, 407, 87)

    menu = Bouton("sprites/Boutons/Menu normal.png", 255, 650, 240, 86)
    menu.setImageOver("sprites/Boutons/Menu animé.png")

    #quitter = Bouton("sprites/Boutons/Jouer normal.png", 255, 640, 240, 86)
    #quitter.setImageOver("sprites/Boutons/Jouer animé.png")

    partie = 1
    fond = Level('m')

    newPerso = "perso1"
    while partie:
        if current_page == "selection":
            # Chargement et collage du fond
            fenetre.blit(fond.background,(0,0))
            fond.printLvl(fenetre,0)
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
            fenetre.blit(menu.image, menu.rect)
            #fenetre.blit(quitter.image,quitter.rect)

            # Affection de la fonction as mettre lorsque l'on fait l'action
            perso1.setButtonAction(loadPerso1)
            perso2.setButtonAction(loadPerso2)
            perso3.setButtonAction(loadPerso3)
            menu.setButtonAction(loadMenu)

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
            arrayUpdate.append((menu))
            #arrayUpdate.append(quitter)

            # Ajout de tout les trucs qui attendent un event
            arrayClick.append(perso1)
            arrayClick.append(perso2)
            arrayClick.append(perso3)
            arrayClick.append(menu)
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
                                    if res == "quit":
                                        partie = False
                                    elif res == "menu":
                                        current_page = "menu"
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

    createLibPerso()

    return  current_page == "menu"
