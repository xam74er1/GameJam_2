import pygame
from Class.button import *
from pygame.locals import *


#list update

def updateimage(frame,array):
    for it in array:
        frame.blit(it[0],it[1])

# Changement page
def loadMenu():
    return "menu"

def loadJouer():
    return "jouer"

def loadHighscore():
    return "hoghscore"

def loadCredit():
    return "credit"

def quitGame():
    pygame.display.quit()
    quit()

#-----------Main -----------

pygame.init()

current_page = "menu"

# Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((750, 750))

partie = 1

while partie:
    if current_page == "menu":
        # Chargement et collage du fond
        #fond = pygame.image.load("images/background.jpg").convert()
        #fenetre.blit(fond, (0, 0))
        titre = pygame.transform.scale(pygame.image.load("Rectangle_bleu_de_merde.png"), (350, 150))

        #list de tout les truc as update
        arrayUpdate = []

        #list de tout les truc qui attendre un clique , equivant as a event listner pour les boutton
        arrayClick = []

        #Creation du bouton
        jouer = Bouton("sprites/Button/Jouer.png",275,250,200,50)
        fenetre.blit(jouer.image,jouer.rect)


        highscore = Bouton("sprites/Button/Highscore.png",275,350,200,50)
        fenetre.blit(highscore.image,highscore.rect)

        credit = Bouton("sprites/Button/Credits.png",275,450,200,50)
        fenetre.blit(credit.image,credit.rect)

        quitter = Bouton("sprites/Button/Quitter.png",275,550,200,50)
        fenetre.blit(quitter.image,quitter.rect)

        #Afection de la fonction as mettre lorsque lon fait laction

        jouer.setButtonAction(loadJouer)
        highscore.setButtonAction(loadHighscore)
        credit.setButtonAction(loadCredit)
        quitter.setButtonAction(quitGame)

        # Rafraîchissement de l'écran
        pygame.display.flip()
        # BOUCLE INFINIE
        continuer = 1

        #Ajout de tout les truc as update
        #arrayUpdate.append((fond,(0,0)))
        arrayUpdate.append((jouer.image,jouer.rect))
        arrayUpdate.append((highscore.image,highscore.rect))
        arrayUpdate.append((credit.image,credit.rect))
        arrayUpdate.append((quitter.image,quitter.rect))

        #Ajout de tout les truc qui attende un event
        arrayClick.append(jouer)
        arrayClick.append(highscore)
        arrayClick.append(credit)
        arrayClick.append(quitter)


        while continuer:

            for event in pygame.event.get():  # Attente des événements
                if event.type == QUIT:
                    continuer = 0
                    quit()

                if event.type == MOUSEBUTTONDOWN:

                    if event.button == 1:  # Si clic gauche

                        for bt in arrayClick:

                            val = bt.isInZone(event.pos[0],event.pos[1])

                            if bt.isInZone(event.pos[0],event.pos[1]) :
                                current_page = bt.action()
                                continuer = 0


            # Re-collage
            #fenetre.blit(fond, (0, 0))
            fenetre.blit(titre, (200, 50))
            updateimage(fenetre,arrayUpdate)
            #fenetre.blit(perso, position_perso)
            # Rafraichissement
            pygame.display.flip()
            pygame.key.set_repeat(40,30)




    elif current_page == "jouer":
        print("test")


    elif current_page == "highscore":
        titre = pygame.transform.scale(pygame.image.load("Rectangle_bleu_de_merde.png"), (350, 150))
        fenetre.blit(titre, (500, 500))
        pygame.display.flip()

        # list de tout les truc as update
        arrayUpdate = []
        # list de tout les truc qui attendre un clique , equivant as a event listner pour les boutton
        arrayClick = []
        # Creation du bouton
        menu = Bouton("Rectangle_bleu_de_merde.png", 275, 250, 600, 50)
        fenetre.blit(menu.image, menu.rect)
        # Afection de la fonction as mettre lorsque lon fait laction
        menu.setButtonAction(loadMenu)
        # Ajout de tout les truc as update
        arrayUpdate.append((menu.image, menu.rect))
        # Ajout de tout les truc qui attende un event
        arrayClick.append(menu)

        while continuer:

            for event in pygame.event.get():  # Attente des événements
                if event.type == QUIT:
                    continuer = 0
                    quit()

                if event.type == MOUSEBUTTONDOWN:

                    if event.button == 1:  # Si clic gauche

                        for bt in arrayClick:

                            val = bt.isInZone(event.pos[0], event.pos[1])

                            if bt.isInZone(event.pos[0], event.pos[1]):
                                current_page = bt.action()
                                continuer = 0
            # Re-collage
            fenetre.blit(titre, (200, 50))
            updateimage(fenetre, arrayUpdate)
            # fenetre.blit(perso, position_perso)
            # Rafraichissement
            pygame.display.flip()
            pygame.key.set_repeat(40, 30)



    elif current_page == "credit":
        pygame.display.flip()

