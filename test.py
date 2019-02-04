import pygame
from button import *
from pygame.locals import *

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

# Rafraîchissement de l'écran
pygame.display.flip()



b = Bouton("perso.png",10,1,30,30)
print(b.rect.x)


# BOUCLE INFINIE
continuer = 1
pygame.key.set_repeat(1,50)
while continuer:
    print(position_perso.x)
    for event in pygame.event.get():  # Attente des événements
        if event.type == QUIT:
            continuer = 0

        if event.type == KEYDOWN:
            if event.key == K_DOWN:  # Si "flèche bas"
                position_perso = position_perso.move(0, 3)
            if event.key == K_UP:  # Si "flèche bas"
                position_perso = position_perso.move(0, -3)
            if event.key == K_LEFT:  # Si "flèche bas"
                position_perso = position_perso.move(-3, 0)
            if event.key == K_RIGHT:  # Si "flèche bas"
                position_perso = position_perso.move(3, 0)

    # Re-collage
    fenetre.blit(fond, (0, 0))
    fenetre.blit(perso, position_perso)
    # Rafraichissement
    pygame.display.flip()
    pygame.key.set_repeat(40,30)
