import pygame
from Class.button import *
from pygame.locals import *
from JeuxEnCour import *
from pygame import font


# list update
def updateimage(frame,array):
    for it in array:
        frame.blit(it.getImage(),it.rect)

# Changement page
def loadMenu():
    return "menu"

def loadJouer():
    return "jouer"

def loadHighscore():
    return "highscore"

def loadCredit():
    return "credit"

def quitGame():
    pygame.display.quit()
    quit()

# Trie les score du plus grand au plus petit
def triScore():
    fichier = open("test-score.txt", "r")
    tableau = []

    NumberOfLine = 0
    for line in fichier:
        NumberOfLine += 1

    fichier.close()

    fichier = open("test-score.txt", "r")
    tableau = []

    i = 0
    while i < NumberOfLine:
        tableau.append(fichier.readline().split('|'))
        i += 1
    fichier.close()

    tableau.sort(reverse=True)
    return tableau

# affiche les 10 meilleurs socres
def afficheHighscore(tab, nb):
    font = pygame.font.Font("Font/JELLYBELLY.TTF", 40)
    return font.render(str(nb + 1) + "         " + tab[nb][0] + "        " + tab[nb][1], 1, (255, 255, 255))


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

menu = Bouton("sprites/Boutons/Jouer normal.png", 255, 650, 240, 86)
menu.setImageOver("sprites/Boutons/Jouer animé.png")

partie = 1
fond = Level('m')
while partie:
    if current_page == "menu":
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
        fenetre.blit(jouer.getImage(),jouer.rect)
        fenetre.blit(highscore.image,highscore.rect)
        fenetre.blit(credit.image,credit.rect)
        fenetre.blit(quitter.image,quitter.rect)

        # Affection de la fonction as mettre lorsque l'on fait l'action
        jouer.setButtonAction(loadJouer)
        highscore.setButtonAction(loadHighscore)
        credit.setButtonAction(loadCredit)
        quitter.setButtonAction(quitGame)

        # Rafraîchissement de l'écran
        pygame.display.flip()
        # BOUCLE INFINIE
        continuer = 1

        # Ajout de tout les trucs as update
        arrayUpdate.append(jouer)
        arrayUpdate.append(highscore)
        arrayUpdate.append(credit)
        arrayUpdate.append(quitter)

        # Ajout de tout les trucs qui attendent un event
        arrayClick.append(jouer)
        arrayClick.append(highscore)
        arrayClick.append(credit)
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
        # Chargement et collage du fond
        fond = pygame.image.load("sprites/Background/Background_Accueil.png").convert()
        fenetre.blit(fond, (0, 0))
        titre = pygame.transform.scale(pygame.image.load("sprites/Title/Logo.png"), (610, 130))
        fenetre.blit(fond, (0, 0))

        # liste de tout les trucs a update
        arrayUpdate = []

        # liste de tout les trucs qui attendent un clique , equivalent as a event listner pour les boutons
        arrayClick = []

        # Creation du bouton
        fenetre.blit(menu.image, menu.rect)

        # Affection de la fonction a mettre lorsque l'on fait l'action
        menu.setButtonAction(loadMenu)

        # Rafraîchissement de l'écran
        pygame.display.flip()
        # BOUCLE INFINIE
        continuer = 1

        # Ajout de tout les trucs a update
        arrayUpdate.append((menu))

        # Ajout de tout les truc qui attendent un event
        arrayClick.append(menu)

        # appel le trie et l'affichage des meilleurs scores
        tableau = triScore()

        font = pygame.font.Font("Font/JELLYBELLY.TTF", 60)
        texte0 = font.render("Rang   Score    Pseudo", 1, (255, 255, 255))
        font = pygame.font.Font("Font/JELLYBELLY.TTF", 30)
        texte1 = afficheHighscore(tableau, 0)
        texte2 = afficheHighscore(tableau, 1)
        texte3 = afficheHighscore(tableau, 2)
        texte4 = afficheHighscore(tableau, 3)
        texte5 = afficheHighscore(tableau, 4)
        texte6 = afficheHighscore(tableau, 5)
        texte7 = afficheHighscore(tableau, 6)
        texte8 = afficheHighscore(tableau, 7)
        texte9 = afficheHighscore(tableau, 8)
        texte10 = afficheHighscore(tableau, 9)


        while continuer:
            for event in pygame.event.get():  # Attente des événements
                if event.type == QUIT:
                    continuer = 0
                    quitGame()

                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:  # Si clic gauche
                        for bt in arrayClick:
                            val = bt.isInZone(event.pos[0], event.pos[1])
                            if bt.isInZone(event.pos[0], event.pos[1]):
                                current_page = bt.action()
                                continuer = 0

            # Re-collage
            fenetre.blit(fond, (0, 0))
            fenetre.blit(titre, (70, 50))
            fenetre.blit(texte0, (100, 170))
            fenetre.blit(texte1, (130, 250))
            fenetre.blit(texte2, (130, 290))
            fenetre.blit(texte3, (130, 330))
            fenetre.blit(texte4, (130, 370))
            fenetre.blit(texte5, (130, 410))
            fenetre.blit(texte6, (130, 450))
            fenetre.blit(texte7, (130, 490))
            fenetre.blit(texte8, (130, 530))
            fenetre.blit(texte9, (130, 570))
            fenetre.blit(texte10, (130, 610))
            updateimage(fenetre, arrayUpdate)
            # fenetre.blit(perso, position_perso)
            # Rafraichissement
            pygame.display.flip()
            pygame.key.set_repeat(40, 30)





    elif current_page == "credit":
        pygame.display.flip()




    elif current_page == "fin_de_partie":
        # Chargement et collage du fond
        fond = pygame.image.load("sprites/Background/Background_Accueil.png").convert()
        fenetre.blit(fond, (0, 0))
        titre = pygame.transform.scale(pygame.image.load("sprites/Title/Logo.png"), (610, 130))
        fenetre.blit(fond, (0, 0))

        # liste de tout les trucs a update
        arrayUpdate = []

        # liste de tout les trucs qui attendent un clique , equivalent as a event listner pour les boutons
        arrayClick = []

        # Creation du bouton
        fenetre.blit(menu.image, menu.rect)

        # Affection de la fonction a mettre lorsque l'on fait l'action
        menu.setButtonAction(loadMenu)

        # Rafraîchissement de l'écran
        pygame.display.flip()
        # BOUCLE INFINIE
        continuer = 1

        # Ajout de tout les trucs a update
        arrayUpdate.append((menu))

        # Ajout de tout les truc qui attendent un event
        arrayClick.append(menu)

        # appel le trie et l'affichage des meilleurs scores
        tableau = triScore()

        font = pygame.font.Font("Font/JELLYBELLY.TTF", 60)
        texte0 = font.render("Rang   Score    Pseudo", 1, (255, 255, 255))
        font = pygame.font.Font("Font/JELLYBELLY.TTF", 30)
        texte1 = afficheHighscore(tableau, 0)
        texte2 = afficheHighscore(tableau, 1)
        texte3 = afficheHighscore(tableau, 2)
        texte4 = afficheHighscore(tableau, 3)
        texte5 = afficheHighscore(tableau, 4)
        texte6 = afficheHighscore(tableau, 5)
        texte7 = afficheHighscore(tableau, 6)
        texte8 = afficheHighscore(tableau, 7)
        texte9 = afficheHighscore(tableau, 8)
        texte10 = afficheHighscore(tableau, 9)

        while continuer:
            for event in pygame.event.get():  # Attente des événements
                if event.type == QUIT:
                    continuer = 0
                    quitGame()

                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:  # Si clic gauche
                        for bt in arrayClick:
                            val = bt.isInZone(event.pos[0], event.pos[1])
                            if bt.isInZone(event.pos[0], event.pos[1]):
                                current_page = bt.action()
                                continuer = 0

            # Re-collage
            fenetre.blit(fond, (0, 0))
            fenetre.blit(titre, (70, 50))
            fenetre.blit(texte0, (100, 170))
            fenetre.blit(texte1, (130, 250))
            fenetre.blit(texte2, (130, 290))
            fenetre.blit(texte3, (130, 330))
            fenetre.blit(texte4, (130, 370))
            fenetre.blit(texte5, (130, 410))
            fenetre.blit(texte6, (130, 450))
            fenetre.blit(texte7, (130, 490))
            fenetre.blit(texte8, (130, 530))
            fenetre.blit(texte9, (130, 570))
            fenetre.blit(texte10, (130, 610))
            updateimage(fenetre, arrayUpdate)
            # fenetre.blit(perso, position_perso)
            # Rafraichissement
            pygame.display.flip()
            pygame.key.set_repeat(40, 30)