import pygame

from pygame.locals import *

pygame.init()

dep = 1
# Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))

# Chargement et collage du fond
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0, 0))

# Chargement et collage du personnage
perso = pygame.image.load("perso.png").convert_alpha()

position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)

# Rafraîchissement de l'écran
pygame.display.flip()




# BOUCLE INFINIE
continuer = 1
while continuer:

    if pygame.key.get_pressed()[K_DOWN]:  # Si "flèche bas"
        position_perso = position_perso.move(0, dep)
    if pygame.key.get_pressed()[K_UP]:  # Si "flèche bas"
        position_perso = position_perso.move(0, -dep)
    if pygame.key.get_pressed()[K_LEFT]:  # Si "flèche bas"
        position_perso = position_perso.move(-dep, 0)
    if pygame.key.get_pressed()[K_RIGHT]:  # Si "flèche bas"
        position_perso = position_perso.move(dep, 0)

    for event in pygame.event.get():  # Attente des événements
        if event.type == QUIT:
            continuer =0




    # Re-collage
    fenetre.blit(fond, (0, 0))
    fenetre.blit(perso, position_perso)
    # Rafraichissement
    pygame.display.flip()
    pygame.key.set_repeat(40,30)
