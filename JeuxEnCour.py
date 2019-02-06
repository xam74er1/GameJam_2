import pygame
from Class.button import *
from Class.Character import *
from pygame.locals import *
from Class.World import *
from Class.Walls import *







def play(fenetre):
    #-----------Main -----------


    if env.with_music:
        pygame.mixer.music.load("music/Song_JellyBall.ogg")
        pygame.mixer.music.play()

    # Chargement et collage du fond
    #fond = pygame.image.load("images/background.jpg").convert()
    #fenetre.blit(fond, (0, 0))

    MAX_X =750
    MAX_Y =750
    FPS = 30


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
    world.level = world.levels[env.lvl_start]
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
                if event.key == K_F7:
                    world.timer += 30
                if event.key == K_ESCAPE:
                    continuer = 0

        #Gravite
        perso.move()
        perso.applyAcceleration(world.gravity[0], world.gravity[1])



        if world.level.coins == []:
            continuer = world.nextLevel()

        if world.timer <=0 :
            continuer =0

        #-----------GESTION DE LIMAGE -------
        # bacgound
        fenetre.blit(world.level.background, (0, 0))



        title_text = bigText.render(str(world.getTimeFormated()), True,textColor )
        textpos = title_text.get_rect()
        textpos.centerx = fenetre.get_rect().centerx
        textpos.centery = fenetre.get_rect().centery
        fenetre.blit(title_text, textpos)






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


        #if count%8==0:
            #perso.animation()





        pygame.time.Clock().tick(FPS)

#---------------------------------------------------------
    if env.with_music:
        pygame.mixer.music.stop()

    return perso
