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
fenetre = pygame.display.set_mode((640, 480))

# Chargement et collage du fond
fond = pygame.image.load("images/background.jpg").convert()
fenetre.blit(fond, (0, 0))

# Chargement et collage du personnage
perso = pygame.image.load("images/perso.png").convert_alpha()

position_perso = perso.get_rect()
position_perso = position_perso.move(100,100)
fenetre.blit(perso, position_perso)

arrayUpdate = [];
arrayClick = []



b = Bouton("sprites/Bouton1.png",100,100,300,300)
print(b.image)
print(position_perso)
fenetre.blit(b.image,b.rect)
print(b.rect.x)

act = testButton
b.setButtonAction(act)

# Rafraîchissement de l'écran
pygame.display.flip()
# BOUCLE INFINIE
continuer = 1

arrayUpdate.append((fond,(0,0)))
arrayUpdate.append((b.image,b.rect))
arrayUpdate.append((perso,position_perso))

arrayClick.append(b)


while continuer:

    for event in pygame.event.get():  # Attente des événements
        if event.type == QUIT:
            continuer = 0





    # Re-collage
    #fenetre.blit(fond, (0, 0))

    updateimage(fenetre,arrayUpdate)
    #fenetre.blit(perso, position_perso)
    # Rafraichissement
    pygame.display.flip()
    pygame.key.set_repeat(40,30)


