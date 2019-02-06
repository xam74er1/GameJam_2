import pygame
from Class.button import *
from Class.Character import *
from pygame.locals import *
from Class.World import *
from Class.Walls import *


MAX_X =750
MAX_Y =750
FPS = 30

#list update

def updateimage(frame,array):
    for it in array:
        frame.blit(it[0],it[1])

def testButton():
    print("ce test as marche ")




#-----------Main -----------


pygame.init()

# Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((MAX_X,MAX_Y ))



# Chargement et collage du fond
#fond = pygame.image.load("images/background.jpg").convert()
#fenetre.blit(fond, (0, 0))




arrayUpdate = [];
arrayClick = []

count = 0
bigText = pygame.font.SysFont(pygame.font.get_fonts()[7], 80)
textColor = (255,255,255)


pygame.mouse.set_cursor(*pygame.cursors.diamond)

world = World(fenetre,MAX_X,MAX_Y)

# Rafraîchissement de l'écran
pygame.display.flip()
# BOUCLE INFINIE
continuer = 1


perso = Character(world, MAX_X/2, MAX_Y-100, 32, 32)
fenetre.blit(perso.image, perso.rect)

#arrayUpdate.append((fond,(0,0)))

world.initLevels()
world.level = world.levels[0]
world.level.rezieBacground(MAX_X,MAX_Y)
world.level.printLvl(fenetre)
world.gravity = world.level.gravity
fenetre.blit(world.level.background, (0, 0))

pygame.key.set_repeat(40, 100)

while continuer:

    for event in pygame.event.get():  # Attente des événements
        if event.type == QUIT:
            continuer = 0
        gravityForce = 0.5
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                #perso.applyAcceleration(0,4)
                perso.down(world)
            if event.key == K_UP:
                #perso.applyAcceleration(0,-10)
                perso.up(world)
            if event.key == K_LEFT:
                perso.left(world)
                #perso.applyAcceleration(-4, 0)
            if event.key == K_RIGHT:
                perso.right(world)
                #perso.applyAcceleration(4, 0)
            if event.key == K_F1:
                world.gravity = (0,gravityForce)
            if event.key == K_F2:
                world.gravity =(0,-gravityForce)
            if event.key == K_F3:
                world.gravity=(gravityForce,0)
            if event.key == K_F4:
                world.gravity=(-gravityForce,0)
            if event.key == K_F5:
                perso.fly = not perso.fly
            if event.key == K_F6:
                world.timer -= 30

    #Gravite
    perso.move()
    perso.applyAcceleration(world.gravity[0], world.gravity[1])



    if world.level.coins == []:
        world.nextLevel()

    #-----------GESTION DE LIMAGE -------
    # bacgound
    fenetre.blit(world.level.background, (0, 0))



    title_text = bigText.render(str(world.getTimeFormated()), True,textColor )
    textpos = title_text.get_rect()
    textpos.centerx = fenetre.get_rect().centerx
    textpos.centery = fenetre.get_rect().centery
    fenetre.blit(title_text, textpos)





    updateimage(fenetre, arrayUpdate)
    fenetre.blit(perso.image, perso.rect)

    world.level.printLvl(fenetre)

    #fenetre.blit(perso, position_perso)
    # Rafraichissement
    pygame.display.flip()


#-----------Gestion du temp---------
    count += 1
    if(count>FPS):
        count = 0
        world.aplyTime()




    pygame.time.Clock().tick(FPS)


