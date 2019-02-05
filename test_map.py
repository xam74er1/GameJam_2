import sys, pygame
from Class.Walls import *
from Class.World import *

pygame.init()

# Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((1024, 768))

# Chargement et collage du fond
fond = pygame.image.load("background.bmp").convert()
fenetre.blit(fond, (192, 144))

# Chargement et collage du personnage
perso = pygame.image.load("Boule_jeu.png").convert_alpha()
#perso = pygame.transform.scale(perso.image,(10,10))
position_perso = perso.get_rect()
position_perso = position_perso.move(100,100)
#fenetre.blit(perso, position_perso)

# Chargement de la liste du décor
square_1 = pygame.image.load("Rectangle_bleu_de_merde.png").convert()
square_2 = pygame.image.load("Rectangle_bleu_de_merde.png").convert()
square_3 = pygame.image.load("Rectangle_bleu_de_merde.png").convert()
square_4 = pygame.image.load("Rectangle_bleu_de_merde.png").convert()
square_5 = pygame.image.load("Rectangle_bleu_de_merde.png").convert()
square_6 = pygame.image.load("Rectangle_bleu_de_merde.png").convert()
square_7 = pygame.image.load("Rectangle_bleu_de_merde.png").convert()
square_8 = pygame.image.load("Rectangle_bleu_de_merde.png").convert()
square_9 = pygame.image.load("Rectangle_bleu_de_merde.png").convert()
square_10 = pygame.image.load("Rectangle_bleu_de_merde.png").convert()
square_11 = pygame.image.load("Rectangle_bleu_de_merde.png").convert()
struct = [square_1,square_2,square_3,square_4,square_5,square_6,square_7,square_8,square_9,square_10,square_11]

x = 200
y = 300

for i in struct:
    fenetre.blit(i, (x, y))
    x = x + 16




# Rafraichissement de l'écrant
pygame.display.flip()

continuer = 1
while continuer:
    for event in pygame.event.get():  # Attente des événements
        if event.type == pygame.QUIT:
            continuer = 0


    # Recolage
    fenetre.blit(fond, (192,144))
    x = 200
    for i in struct:
        fenetre.blit(i, (x, y))
        x = x + 16

    # Rafraichisement
    pygame.display.flip()

