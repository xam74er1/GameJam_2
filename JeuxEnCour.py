import pygame
from Class.button import *
from Class.Character import *
from pygame.locals import *
from Class.World import *
from Class.Walls import *








def play(fenetre):
    #-----------Main -----------

    if env.with_music:
        pygame.mixer.music.load(env.music_path)


    # Chargement et collage du fond
    #fond = pygame.image.load("images/background.jpg").convert()
    #fenetre.blit(fond, (0, 0))

    MAX_X =750
    MAX_Y =750
    FPS = 30


    arrayUpdate = [];
    arrayClick = []

    count = 0.0
    bigText = pygame.font.SysFont(pygame.font.get_fonts()[7], 80)
    smallText =pygame.font.SysFont(pygame.font.get_fonts()[7], 20)
    textColor = (255,255,255)


    pygame.mouse.set_cursor(*pygame.cursors.diamond)

    world = World(fenetre,MAX_X,MAX_Y)

    # Rafraîchissement de l'écran
    pygame.display.flip()
    # BOUCLE INFINIE
    continuer = 1


    perso = Character(world, 50, 700, 32, 32)
    fenetre.blit(perso.image, perso.rect)

    #arrayUpdate.append((fond,(0,0)))
    pygame.key.set_repeat(40, 100)

    world.initLevels()
    world.level = world.levels[env.lvl_start]
    world.level.rezieBacground(MAX_X,MAX_Y)
    world.level.printLvl(fenetre,world)
    world.gravity = world.level.gravity

    pygame.key.set_repeat(40, 100)

    world.startTimer()
    if env.with_music:
        pygame.mixer.music.play()
    world.level.printLvl(fenetre,world)
    fenetre.blit(world.level.background, (0, 0))

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
                    world.timeMax -= 30
                if event.key == K_F7:
                    world.timeMax += 30
                if event.key == K_F8:
                    world.gravity = (0, 0)
                    perso.ax = 0
                    perso.ay = 0
                if event.key == K_ESCAPE:
                    continuer = 0

        #Gravite
        perso.move()
        perso.applyAcceleration(world.gravity[0], world.gravity[1])



        if world.level.coins == []:
            continuer = world.nextLevel()
            perso.changeGravity(world.level.gravity)

        if world.timer <=0 :
            continuer =0

        #-----------GESTION DE LIMAGE -------
        # bacgound
        fenetre.blit(world.level.background, (0, 0))


        world.aplyTime()
        if env.with_score:
            title_text = bigText.render(str(world.getTimeFormated()), True,textColor )
            textpos = title_text.get_rect()
            textpos.centerx = fenetre.get_rect().centerx
            textpos.centery = fenetre.get_rect().centery
            fenetre.blit(title_text, textpos)

            title_text = smallText.render("level:"+str(world.level.numlevel)+"-score :"+str(perso.coins), True, textColor)
            textpos = title_text.get_rect()
            textpos.x = 20
            textpos.y = 20
            fenetre.blit(title_text, textpos)

        fenetre.blit(perso.image, perso.rect)

        world.level.printLvl(fenetre,world)

        #fenetre.blit(perso, position_perso)
        # Rafraichissement
        pygame.display.flip()


    #-----------Gestion du temp---------
        count += 1.0
        if(count>env.FPS):
            count -= env.FPS
            #world.aplyTime()


        #if count%8==0:
            #perso.animation()





        pygame.time.Clock().tick(FPS)

#---------------------------------------------------------
    #ces deux lignes doivent être commentées ou décommentées en même temps
    if env.with_music:
        pygame.mixer.music.stop()
    env.lib_perso=[]

    return perso
