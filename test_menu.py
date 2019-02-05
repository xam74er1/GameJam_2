import pygame
from Class.button import *
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
fenetre = pygame.display.set_mode((750, 750))

# Chargement et collage du fond
#fond = pygame.image.load("images/background.jpg").convert()
#fenetre.blit(fond, (0, 0))
titre = pygame.transform.scale(pygame.image.load("Rectangle_bleu_de_merde.png"), (350, 150))

#list de tout les truc as update
arrayUpdate = []

#list de tout les truc qui attendre un clique , equivant as a event listner pour les boutton
arrayClick = []

#Creation du bouton

jouer = Bouton("Rectangle_bleu_de_merde.png",275,275,200,50)
fenetre.blit(jouer.image,jouer.rect)

highscore = Bouton("Rectangle_bleu_de_merde.png",275,375,200,50)
fenetre.blit(highscore.image,highscore.rect)

credit = Bouton("Rectangle_bleu_de_merde.png",275,475,200,50)
fenetre.blit(credit.image,credit.rect)

quitter = Bouton("Rectangle_bleu_de_merde.png",275,575,200,50)
fenetre.blit(quitter.image,quitter.rect)

#Afection de la fonction as mettre lorsque lon fait laction
act = testButton
jouer.setButtonAction(act)
highscore.setButtonAction(act)
credit.setButtonAction(act)
quitter.setButtonAction(act)


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


        if event.type == MOUSEBUTTONDOWN:

            if event.button == 1:  # Si clic gauche

                for bt in arrayClick:

                    val = bt.isInZone(event.pos[0],event.pos[1])

                    if bt.isInZone(event.pos[0],event.pos[1]) :
                        print("dans la zone")
                        bt.action()





    # Re-collage
    #fenetre.blit(fond, (0, 0))
    fenetre.blit(titre, (200, 75))
    updateimage(fenetre,arrayUpdate)
    #fenetre.blit(perso, position_perso)
    # Rafraichissement
    pygame.display.flip()
    pygame.key.set_repeat(40,30)


