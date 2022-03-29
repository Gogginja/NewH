from pickle import TRUE
from turtle import _Screen

import pygame
import platform
import player
import coin

class main:
    # GLOBAL VARIABLES #
    global SCREEN_SIZE,BACKGROUND_COLOR,DARK_GREY,GREEN,WHITE,DARK,screen,width,height,clock,game_state,screenList,currentScreen
    SCREEN_SIZE =   (700, 500)
    MENU_COLOR =    (50, 50, 50)
    DARK_GREY =     (50, 50, 50)
    GREEN =         (16, 173, 42)
    WHITE =         (255,255,255)
    DARK =          (100,100,100)
    screen =        pygame.display.set_mode(SCREEN_SIZE)
    width =         screen.get_width()
    height =        screen.get_height()

    clock =         pygame.time.Clock()
    game_state =    'play'
    
    screenList =    ['mainMenu', 'levelSelect', 'settings', 'settings_audio', 'settings_gameplay', 'settings_video', 'level_1']
    currentScreen = 'mainMenu'
    run =           TRUE

# MAIN GAME LOOP #
    while run:
        pygame.init()
        mouse = pygame.mouse.get_pos()
        screen.fill(MENU_COLOR)
        # set FPS
        clock.tick(60)

        # BUTTON CREATION FUNCTION #
        def createButton(text, x, y):
            smallfont = pygame.font.SysFont('Corbel',20)
            buttonText = smallfont.render(text, True, WHITE)
            mouse = pygame.mouse.get_pos() 
            if (x <= mouse[0] <= x+140) and (y <= mouse[1] <= y+40): 
                pygame.draw.rect(screen,(255,255,255),[x,y,140,40]) 
            else: 
                pygame.draw.rect(screen,(100,100,100),[x,y,140,40])
            #add text (centered on the button)
            screen.blit(buttonText, (x+70-buttonText.get_width()/2, y+buttonText.get_height()/2)) 

############################ MAIN MENU ################################

        if currentScreen == 'mainMenu':
            # BUTTON SETTINGS #
            levelSelect = [width/6, height/6]
            settingsPos = [width/6, height/3]
            quitPos = [width/6, height/2]

            # EVENT HANDLER #
            for ev in pygame.event.get(): 
                # If mouse clicks:
                if ev.type == pygame.MOUSEBUTTONDOWN: 
                    # Level Select
                    if (levelSelect[0] <= mouse[0] <= levelSelect[0]+140) and (levelSelect[1] <= mouse[1] <= levelSelect[1]+40): 
                        currentScreen = 'level_select'
                    # Settings
                    elif (settingsPos[0] <= mouse[0] <= settingsPos[0]+140) and (settingsPos[1] <= mouse[1] <= settingsPos[1]+40): 
                        currentScreen = 'settings'
                    # Quit
                    elif (quitPos[0] <= mouse[0] <= quitPos[0]+140) and (quitPos[1] <= mouse[1] <= quitPos[1]+40): 
                        pygame.quit()
            
            # BUTTON CREATION #
            createButton('SELECT LEVEL', levelSelect[0], levelSelect[1]) 
            createButton('SETTINGS', settingsPos[0], settingsPos[1]) 
            createButton('QUIT', quitPos[0], quitPos[1]) 

######################### SETTIGNS - MAIN #############################

        if currentScreen == 'settings':
            # BUTTON SETTINGS #
            audioPos = [width/6, height/6]
            gameplayPos = [width/6, height/3]
            videoPos = [width/6, height/2]
            backPos = [width/1.5, height/1.5]

            # EVENT HANDLER #
            for ev in pygame.event.get(): 
                # If mouse clicks:
                if ev.type == pygame.MOUSEBUTTONDOWN: 
                    # Audio
                    if (audioPos[0] <= mouse[0] <= audioPos[0]+140) and (audioPos[1] <= mouse[1] <= audioPos[1]+40): 
                        currentScreen = 'settings_audio'
                    # Gameplay
                    elif (gameplayPos[0] <= mouse[0] <= gameplayPos[0]+140) and (gameplayPos[1] <= mouse[1] <= gameplayPos[1]+40): 
                        currentScreen = 'settings_gameplay'
                    # Video
                    elif (videoPos[0] <= mouse[0] <= videoPos[0]+140) and (videoPos[1] <= mouse[1] <= videoPos[1]+40): 
                        currentScreen = 'settings_video'
                    # Back
                    elif (backPos[0] <= mouse[0] <= backPos[0]+140) and (backPos[1] <= mouse[1] <= backPos[1]+40):
                        currentScreen = 'mainMenu'
            
            # BUTTON CREATION #
            createButton('AUDIO', audioPos[0], audioPos[1]) 
            createButton('GAMEPLAY', gameplayPos[0], gameplayPos[1]) 
            createButton('VIDEO', videoPos[0], videoPos[1]) 
            createButton('BACK', backPos[0], backPos[1]) 

######################## SETTIGNS - AUDIO ############################

        if currentScreen == 'settings_audio':
            # BUTTON SETTINGS #
            backPos = [width/1.5, height/1.5]

            # EVENT HANDLER #
            for ev in pygame.event.get(): 
                # If mouse clicks:
                if ev.type == pygame.MOUSEBUTTONDOWN: 
                    # Back
                    if (backPos[0] <= mouse[0] <= backPos[0]+140) and (backPos[1] <= mouse[1] <= backPos[1]+40):
                        currentScreen = 'settings'
            
            # BUTTON CREATION #
            createButton('BACK', backPos[0], backPos[1]) 

####################### SETTIGNS - GAMEPLAY ###########################

        if currentScreen == 'settings_gameplay':
            # BUTTON SETTINGS #
            backPos = [width/1.5, height/1.5]

            # EVENT HANDLER #
            for ev in pygame.event.get(): 
                # If mouse clicks:
                if ev.type == pygame.MOUSEBUTTONDOWN: 
                    # Back
                    if (backPos[0] <= mouse[0] <= backPos[0]+140) and (backPos[1] <= mouse[1] <= backPos[1]+40):
                        currentScreen = 'settings'  
            
            # BUTTON CREATION #
            createButton('BACK', backPos[0], backPos[1]) 

######################## SETTIGNS - VIDEO #############################

        if currentScreen == 'settings_video':
            # BUTTON SETTINGS #
            backPos = [width/1.5, height/1.5]

            # EVENT HANDLER #
            for ev in pygame.event.get(): 
                # If mouse clicks:
                if ev.type == pygame.MOUSEBUTTONDOWN: 
                    # Back
                    if (backPos[0] <= mouse[0] <= backPos[0]+140) and (backPos[1] <= mouse[1] <= backPos[1]+40):
                        currentScreen = 'settings'  
            
            # BUTTON CREATION #
            createButton('BACK', backPos[0], backPos[1]) 

########################## LEVEL SELECT ###############################

        if currentScreen == 'level_select':
            # BUTTON SETTINGS #
            level1Pos = [width/2-70, height/3]
            backPos = [width/1.5, height/1.5]

            # EVENT HANDLER #
            for ev in pygame.event.get(): 
                # If mouse clicks:
                if ev.type == pygame.MOUSEBUTTONDOWN: 
                    # Back
                    if (backPos[0] <= mouse[0] <= backPos[0]+140) and (backPos[1] <= mouse[1] <= backPos[1]+40):
                        currentScreen = 'mainMenu'
                    # Level 1
                    elif (level1Pos[0] <= mouse[0] <= level1Pos[0]+140) and (level1Pos[1] <= mouse[1] <= level1Pos[1]+40):
                        currentScreen = 'level_1' 
            
            # BUTTON CREATION #
            createButton('LEVEL 1', level1Pos[0], level1Pos[1])
            createButton('BACK', backPos[0], backPos[1]) 

############################# LEVEL 1 #################################

        if currentScreen == 'level_1':
            screen.fill(DARK_GREY)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
            for c in coin.coin:
                screen.blit(coin.coin_image, (c[0], c[1]))

            pygame.draw.rect(screen, coin.RED, coin.goal)
            screen.blit(player.player_image, (player.player_x, player.player_y))
            keys = pygame.key.get_pressed()
            player.player_x = player.movementHorizantal(keys, player.player_x, player.player_y, 
                                                        player.player_width, player.player_height)
            fall = player.movementVertical(keys, player.player_x, player.player_y, 
                                        player.player_width, player.player_height, player.player_speed, player.ground)
            
            coin.score += coin.collect(player.player_x,player.player_y)
            # End Goal
            run = coin.end(player.player_x, player.player_y)
            player.player_y = fall[0]
            player.player_speed = fall[1]
            player.ground = fall[2]
            platform.makePlatform(screen,platform.platforms,GREEN)
            pygame.display.flip()

        # CRITICAL (DO NOT DELETE). Refreshes/Updates the screen frame by frame.
        pygame.display.update()
    pygame.quit()