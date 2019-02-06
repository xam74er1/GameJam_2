import pygame
from Class.button import *
from pygame.locals import *
from JeuxEnCour import *


#list update

def updateimage(frame,array):
    for it in array:
        frame.blit(it.getImage(),it.rect)

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
jouer = Bouton("sprites/Boutons/Jouer normal.png", 255, 250, 240, 86)
jouer.setImageOver("sprites/Boutons/Jouer animé.png")

highscore = Bouton("sprites/Boutons/Highscore normal.png", 255, 350, 240, 86)
highscore.setImageOver("sprites/Boutons/Highscore animé.png")

credit = Bouton("sprites/Boutons/Credits normal.png",255,450,240,86)
credit.setImageOver("sprites/Boutons/Credits animé.png")

quitter = Bouton("sprites/Boutons/Quitter normal.png", 255, 550, 240, 86)
quitter.setImageOver("sprites/Boutons/Quitter animé.png")
partie = 1

while partie:
    if current_page == "menu":
        # Chargement et collage du fond
        fond = pygame.image.load("sprites/Background/Background_Accueil.png").convert()
        #fenetre.blit(fond, (0, 0))
        titre = pygame.transform.scale(pygame.image.load("sprites/Title/Logo.png"), (610, 130))

        #list de tout les truc as update
        arrayUpdate = []

        #list de tout les truc qui attendre un clique , equivant as a event listner pour les boutton
        arrayClick = []

        #Creation du bouton

        fenetre.blit(jouer.getImage(),jouer.rect)

        fenetre.blit(highscore.image,highscore.rect)

        fenetre.blit(credit.image,credit.rect)

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
        arrayUpdate.append(jouer)
        arrayUpdate.append(highscore)
        arrayUpdate.append(credit)
        arrayUpdate.append(quitter)

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
            fenetre.blit(fond, (0, 0))
            fenetre.blit(titre, (70, 50))
            updateimage(fenetre,arrayUpdate)
            #fenetre.blit(perso, position_perso)
            # Rafraichissement
            pygame.display.flip()
            pygame.key.set_repeat(40,30)




    elif current_page == "jouer":
        perso = play(fenetre)
        score = perso.coins
        print("score = "+str(score))

        del perso
        current_page = "menu"



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

