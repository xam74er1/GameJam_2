import sys, pygame

pygame.init()

# Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((1024, 768))

# Chargement et collage du fond
fond = pygame.image.load("images/background.jpg").convert()
fenetre.blit(fond, (192, 144))

# Rafraichissement de l'écrant
pygame.display.flip()

continuer = 1
while continuer:
    for event in pygame.event.get():  # Attente des événements
        if event.type == pygame.QUIT:
            continuer = 0


    # Recolage
    fenetre.blit(fond, (192,144))

    # Rafraichisement
    pygame.display.flip()