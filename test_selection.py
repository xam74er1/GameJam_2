import pygame
from Class.button import *
from pygame.locals import *
from JeuxEnCour import *
from pygame import font

# Changement page
def loadPerso1():
    return "menu"

def loadPerso2():
    return "jouer"

def loadPerso3():
    return "highscore"

def quitGame():
    pygame.display.quit()
    quit()

# list update
def updateimage(frame,array):
    for it in array:
        frame.blit(it.getImage(),it.rect)

#-----------Main -----------

pygame.init()

current_page = "selection"

# Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((750, 750))

perso1 = Bouton("sprites/Blob/Blopchon.png", 100, 150, 150, 150)
perso1.setImageOver("sprites/Blob/Blopchon3.png")

perso2 = Bouton("sprites/Blob/Blopchon.png", 100, 300, 150, 150)
perso2.setImageOver("sprites/Blob/Blopchon3.png")

perso3 = Bouton("sprites/Blob/Blopchon.png",100, 450,150, 150)
perso3.setImageOver("sprites/Blob/Blopchon3.png")


quitter = Bouton("sprites/Boutons/Quitter normal.png", 255, 640, 240, 86)
quitter.setImageOver("sprites/Boutons/Quitter animé.png")

partie = 1
fond = Level('m')
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
        fenetre.blit(quitter.image,quitter.rect)

        # Affection de la fonction as mettre lorsque l'on fait l'action
        perso1.setButtonAction(loadPerso1)
        font = pygame.font.Font("Font/JELLYBELLY.TTF", 100)
        texte0 = font.render("Blopchon", 1, (255, 102, 255))

        perso2.setButtonAction(loadPerso2)
        font = pygame.font.Font("Font/JELLYBELLY.TTF", 100)
        texte1 = font.render("A définir", 1, (255, 102, 255))

        perso3.setButtonAction(loadPerso3)
        font = pygame.font.Font("Font/JELLYBELLY.TTF", 100)
        texte2 = font.render("A définir", 1, (255, 102, 255))

        quitter.setButtonAction(quitGame)

        # Rafraîchissement de l'écran
        pygame.display.flip()
        # BOUCLE INFINIE
        continuer = 1

        # Ajout de tout les trucs as update
        arrayUpdate.append(perso1)
        arrayUpdate.append(perso2)
        arrayUpdate.append(perso3)
        arrayUpdate.append(quitter)

        # Ajout de tout les trucs qui attendent un event
        arrayClick.append(perso1)
        arrayClick.append(perso2)
        arrayClick.append(perso3)
        arrayClick.append(quitter)

        while continuer:
            for event in pygame.event.get():  # Attente des événements
                if event.type == QUIT:
                    continuer = 0
                    quitGame()

                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:  # Si clic gauche
                        for bt in arrayClick:
                            val = bt.isInZone(event.pos[0],event.pos[1])
                            if bt.isInZone(event.pos[0],event.pos[1]) :
                                current_page = bt.action()
                                continuer = 0

            # Re-collage
            fenetre.blit(fond.background, (0, 0))
            fenetre.blit(titre, (70, 40))
            fenetre.blit(texte0, (375, 200))
            fenetre.blit(texte1, (375, 350))
            fenetre.blit(texte2, (375, 500))
            updateimage(fenetre,arrayUpdate)
            #fenetre.blit(perso, position_perso)
            # Rafraichissement
            pygame.display.flip()
            pygame.key.set_repeat(40,30)