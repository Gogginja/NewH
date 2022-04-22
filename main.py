import pygame
import platform
import player
import coin
import animationHandler

class main:
    # GLOBAL VARIABLES #
    global SCREEN_SIZE,BACKGROUND_COLOR,DARK_GREY,GREEN,WHITE,DARK,screen,width,height,clock,screenList,currentScreen,paused,devMenu
    SCREEN_SIZE =   (700, 500)
    MENU_COLOR =    (50, 50, 50)
    DARK_GREY =     (50, 50, 50)
    GREEN =         (16, 173, 42)
    WHITE =         (255,255,255)
    DARK =          (100,100,100)
    screen =        pygame.display.set_mode(SCREEN_SIZE)
    width =         screen.get_width()
    height =        screen.get_height()
    plr =           player.current_image

    clock =         pygame.time.Clock()
    devMenu =       False

    screenList =    ['mainMenu', 'levelSelect', 'settings', 'settings_audio', 'settings_gameplay', 'settings_video', 'level_1']
    currentScreen = 'mainMenu'
    previousScreen = ''
    paused =        False
    run =           True
    deb = 0

    #Skyboxes
    sky1 = pygame.image.load('Image/textures/skybox.png')
    sky2 = pygame.image.load('Image/textures/skybox2.png')
    sky3 = pygame.image.load('Image/textures/skybox3.png')

    scroll_left = False
    scroll_right = False
    scroll = 0
    scroll_speed = 1

    #Draw a more detailed background
    def draw_bg(sky, scroll, speed):
        width = sky.get_width()
        #Loops the background image everytime we scroll a certain distance
        for x in range(4):
            screen.blit(sky, ((x * width) - (scroll * speed),0))

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
    
    def createText(text, x, y):
        smallfont = pygame.font.SysFont('Corbel',50)
        txt = smallfont.render(text, True, WHITE)
        screen.blit(txt, (x-txt.get_width()/2, y-txt.get_height()))

    def drawtext(t, x, y):
        font = pygame.font.Font(pygame.font.get_default_font(), 24)
        text = font.render(t, True, GREEN, DARK_GREY)
        text_rectangle = text.get_rect()
        text_rectangle.topleft = (x, y)
        screen.blit(text, text_rectangle)

    # PAUSE MENU #
    def pause():
            global currentScreen,paused,mouse, run
            window = pygame.Surface(SCREEN_SIZE)
            window.set_colorkey(DARK_GREY)
            window.set_alpha(200)
            smallfont = pygame.font.SysFont('Corbel',50)
            pauseText = smallfont.render('PAUSED', True, WHITE)
            # PAUSE WHITE WINDOW
            screen.blit(window, (0, 0))
            # PAUSE TEXT
            screen.blit(pauseText, (350-pauseText.get_width()/2, 175-pauseText.get_height()))

            mouse = pygame.mouse.get_pos() 
            resumePos = [width/2-70, height/2.5]
            mainMenuPos = [width/2-70, height/2]
            quitPost = [width/2-70, height/1.65]
            
            # EVENT HANDLER #
            for ev in pygame.event.get(): 
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_TAB:
                        paused = not paused
                # If mouse clicks:
                if ev.type == pygame.MOUSEBUTTONDOWN: 
                    # Resume
                    if (resumePos[0] <= mouse[0] <= resumePos[0]+140) and (resumePos[1] <= mouse[1] <= resumePos[1]+40): 
                        paused = False
                    # Main Menu
                    elif (mainMenuPos[0] <= mouse[0] <= mainMenuPos[0]+140) and (mainMenuPos[1] <= mouse[1] <= mainMenuPos[1]+40): 
                        currentScreen = 'mainMenu'
                        paused = False
                    # Quit
                    elif (quitPost[0] <= mouse[0] <= quitPost[0]+140) and (quitPost[1] <= mouse[1] <= quitPost[1]+40): 
                        pygame.quit()
                if ev.type == pygame.QUIT:
                    run = False

# MAIN GAME LOOP #
    while run:
        pygame.init()
        mouse = pygame.mouse.get_pos()
        font = pygame.font.Font(pygame.font.get_default_font(), 24)
        
        screen.fill(MENU_COLOR)
        # set FPS
        clock.tick(60)
       
        if player.player_x > width:
            scroll_right = True
        elif player.player_x < 0:
            scroll_left = True
        else:
            scroll_left = False
            scroll_right = False
        
        if scroll_left == True and scroll > 0:
            scroll -= 5
        if scroll_right == True:
            scroll += 5

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
            level2Pos = [width/2-70, height/2]
            level3Pos = [width/2-70, height/1.5]
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
                        player.canMove = True
                        currentScreen = 'level_1'
                        player.player_x = 0
                        player.player_y = 0
                        player.player_speed = 0
                    # Level 2
                    elif (level2Pos[0] <= mouse[0] <= level2Pos[0]+140) and (level2Pos[1] <= mouse[1] <= level2Pos[1]+40):
                        if not platform.locked2:
                            player.canMove = True
                            currentScreen = 'level_2'
                            player.player_x = 0
                            player.player_y = 0
                            player.player_speed = 0
                        else:
                            createText('LOCKED', 350, 115)
                    # Level 3
                    elif (level3Pos[0] <= mouse[0] <= level3Pos[0]+140) and (level3Pos[1] <= mouse[1] <= level3Pos[1]+40):
                        if not platform.locked3:
                            player.canMove = True
                            currentScreen = 'level_3'
                            player.player_x = 0
                            player.player_y = 0
                            player.player_speed = 0
                        else:
                            createText('LOCKED', 350, 115)

            # HOVER FUNCTIONALITY #
            # Level 1
            if (level2Pos[0] <= mouse[0] <= level2Pos[0]+140) and (level2Pos[1] <= mouse[1] <= level2Pos[1]+40):
                if platform.locked2:
                    createText('LOCKED', 350, 115)
            # Level 3
            elif (level3Pos[0] <= mouse[0] <= level3Pos[0]+140) and (level3Pos[1] <= mouse[1] <= level3Pos[1]+40):
                if platform.locked3:
                    createText('LOCKED', 350, 115)
            
            # BUTTON CREATION #
            createButton('LEVEL 1', level1Pos[0], level1Pos[1])
            createButton('LEVEL 2', level2Pos[0], level2Pos[1])
            createButton('LEVEL 3', level3Pos[0], level3Pos[1])
            createButton('BACK', backPos[0], backPos[1]) 

############################# LEVEL 1 #################################

        if currentScreen == 'level_1':

            #Draws a scrollable background
            draw_bg(sky1, scroll, scroll_speed)
            drawtext('Score: '+ str(coin.score)+' ', 0, 10)
            drawtext('Lives: '+ str(player.player_life)+' ', 100, 10)
            #screen.fill(DARK_GREY)
            keys = pygame.key.get_pressed()

            for c in coin.coin1:
                screen.blit(coin.coin_image, (c[0], c[1]))

            pygame.draw.rect(screen, coin.RED, coin.goal1[0])
            screen.blit(player.current_image, (player.player_x, player.player_y))

            coin.score += coin.collect(player.player_x,player.player_y,coin.coin1)
            if coin.end(player.player_x, player.player_y, coin.goal1):
                platform.locked2 = False
                currentScreen='winMenu'
                player.player_x=0
                player.player_y=0
            platform.makePlatform(screen,platform.level1,GREEN)

            # RUN PLAYER MOVEMENTS ONLY WHEN UNPAUSED
            if paused == False:
                player.player_x = player.movement(keys, player.player_x, player.player_y, 
                                        player.player_width, player.player_height, player.player_speed, player.ground, platform.level1)[0]
                fall = player.movement(keys, player.player_x, player.player_y, 
                                        player.player_width, player.player_height, player.player_speed, player.ground, platform.level1)[1]
                player.player_y = fall[0]
                player.player_speed = fall[1]
                player.ground = fall[2]
            else:
                pause()
                # BUTTON CREATION #
                resumePos = [width/2-70, height/2.5]
                mainMenuPos = [width/2-70, height/2]
                quitPost = [width/2-70, height/1.65]
                createButton('RESUME', resumePos[0], resumePos[1]) 
                createButton('MAIN MENU', mainMenuPos[0], mainMenuPos[1]) 
                createButton('QUIT', quitPost[0], quitPost[1])
            pygame.display.flip()
        
############################# LEVEL 2 #################################

        if currentScreen == 'level_2':
            draw_bg(sky2, scroll, scroll_speed)
            drawtext('Score: '+ str(coin.score)+' ', 0, 10)
            drawtext('Lives: '+ str(player.player_life)+' ', 100, 10)
            keys = pygame.key.get_pressed()

            for c in coin.coin2:
                screen.blit(coin.coin_image, (c[0], c[1]))
            
            pygame.draw.rect(screen, coin.RED, coin.goal2[0])
            screen.blit(player.current_image, (player.player_x, player.player_y))
            
            coin.score += coin.collect(player.player_x,player.player_y,coin.coin2)
            # End Goal
            if coin.end(player.player_x, player.player_y, coin.goal2):
                currentScreen='winMenu'
                platform.locked3 = False
                player.player_x=0
                player.player_y=0
            platform.makePlatform(screen,platform.level2,GREEN)

            # RUN PLAYER MOVEMENTS ONLY WHEN UNPAUSED
            if paused == False:
                player.player_x = player.movement(keys, player.player_x, player.player_y, 
                                        player.player_width, player.player_height, player.player_speed, player.ground, platform.level2)[0]
                fall = player.movement(keys, player.player_x, player.player_y, 
                                        player.player_width, player.player_height, player.player_speed, player.ground, platform.level2)[1]
                player.player_y = fall[0]
                player.player_speed = fall[1]
                player.ground = fall[2]
            else:
                pause()
                # BUTTON CREATION #
                resumePos = [width/2-70, height/2.5]
                mainMenuPos = [width/2-70, height/2]
                quitPost = [width/2-70, height/1.65]
                createButton('RESUME', resumePos[0], resumePos[1]) 
                createButton('MAIN MENU', mainMenuPos[0], mainMenuPos[1]) 
                createButton('QUIT', quitPost[0], quitPost[1])
            pygame.display.flip()

############################# LEVEL 3 #################################

        if currentScreen == 'level_3':
            draw_bg(sky3, scroll, scroll_speed)
            drawtext('Score: '+ str(coin.score)+' ', 0, 10)
            drawtext('Lives: '+ str(player.player_life)+' ', 100, 10)
            keys = pygame.key.get_pressed()
                    
            for c in coin.coin3:
                screen.blit(coin.coin_image, (c[0], c[1]))

            pygame.draw.rect(screen, coin.RED, coin.goal3[0])
            screen.blit(player.current_image, (player.player_x, player.player_y))

            coin.score += coin.collect(player.player_x,player.player_y,coin.coin3)
            # End Goal
            if coin.end(player.player_x, player.player_y, coin.goal3):
                currentScreen='winMenu'
                player.player_x=0
                player.player_y=0
            platform.makePlatform(screen,platform.level3,GREEN)

            # RUN PLAYER MOVEMENTS ONLY WHEN UNPAUSED
            if paused == False:
                player.player_x = player.movement(keys, player.player_x, player.player_y, 
                                        player.player_width, player.player_height, player.player_speed, player.ground, platform.level3)[0]
                fall = player.movement(keys, player.player_x, player.player_y, 
                                        player.player_width, player.player_height, player.player_speed, player.ground, platform.level3)[1]
                player.player_y = fall[0]
                player.player_speed = fall[1]
                player.ground = fall[2]
            else:
                pause()
                # BUTTON CREATION #
                resumePos = [width/2-70, height/2.5]
                mainMenuPos = [width/2-70, height/2]
                quitPost = [width/2-70, height/1.65]
                createButton('RESUME', resumePos[0], resumePos[1]) 
                createButton('MAIN MENU', mainMenuPos[0], mainMenuPos[1]) 
                createButton('QUIT', quitPost[0], quitPost[1])
            pygame.display.flip()

############################# DEATH MENU #################################

        if currentScreen == 'deathScreen':
            player.player_x = 0
            player.player_y = 0
            player.player_speed = 0
            respawnPos = [width/2-70, height/2]
            mainMenuPos = [width/2-70, height/1.65]
            window = pygame.Surface((700, 500))
            window.set_colorkey((10,10,10))
            smallfont = pygame.font.SysFont('Corbel',50)
            diedText = smallfont.render('YOU DIED', True, (255,255,255))
            
            screen.blit(window, (0, 0))
            screen.blit(diedText, (350-diedText.get_width()/2, 175-diedText.get_height()))
            animationHandler.animate()
            screen.blit(player.current_image, (340, 200))

            # EVENT HANDLER #
            for ev in pygame.event.get(): 
                # If mouse clicks:
                if ev.type == pygame.MOUSEBUTTONDOWN: 
                    # Back
                    if (respawnPos[0] <= mouse[0] <= respawnPos[0]+140) and (respawnPos[1] <= mouse[1] <= respawnPos[1]+40):
                        currentScreen = previousScreen
                        canMove = True
                    # Level 1
                    elif (mainMenuPos[0] <= mouse[0] <= mainMenuPos[0]+140) and (mainMenuPos[1] <= mouse[1] <= mainMenuPos[1]+40):
                        currentScreen = 'mainMenu' 

            # BUTTON CREATION #
            createButton('RESPAWN', respawnPos[0], respawnPos[1]) 
            createButton('MAIN MENU', mainMenuPos[0], mainMenuPos[1])

############################# WIN MENU #################################

        if currentScreen == 'winMenu':
            mainMenuPos = [width/2-70, height/2]
            quitPos = [width/2-70, height/1.65]
            window = pygame.Surface((700, 500))
            window.set_colorkey((10,10,10))
            smallfont = pygame.font.SysFont('Corbel',50)
            winText = smallfont.render('YOU WON!', True, (255,255,255))
            
            screen.blit(window, (0, 0))
            screen.blit(winText, (350-winText.get_width()/2, 175-winText.get_height()))
            animationHandler.animate()
            screen.blit(player.current_image, (340, 200))

            # EVENT HANDLER #
            for ev in pygame.event.get(): 
                # If mouse clicks:
                if ev.type == pygame.MOUSEBUTTONDOWN: 
                    # Back
                    if (mainMenuPos[0] <= mouse[0] <= mainMenuPos[0]+140) and (mainMenuPos[1] <= mouse[1] <= mainMenuPos[1]+40):
                        currentScreen = 'mainMenu'
                        canMove = True
                    # Level 1
                    elif (mainMenuPos[0] <= mouse[0] <= mainMenuPos[0]+140) and (mainMenuPos[1] <= mouse[1] <= mainMenuPos[1]+40):
                        run = False

            # BUTTON CREATION #
            createButton('MAIN MENU', mainMenuPos[0], mainMenuPos[1]) 
            createButton('QUIT', quitPos[0], quitPos[1])

############################# DEV MENU #################################

        if devMenu:
            drawtext('State: '+ str(player.state)+' ', 200, 10)

        #Check if player falls off map and loses life
        if player.player_y>500:
            canMove = False
            player.frameNum = 0
            player.player_life -= 1
            player.player_x = 0
            player.player_y = 0
            player.state = 'died'
            previousScreen = currentScreen
            currentScreen = 'deathScreen'

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                run = False
            if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_TAB:
                        paused = not paused
                    elif ev.key == pygame.K_F9:
                        devMenu = not devMenu

        # CRITICAL (DO NOT DELETE). Refreshes/Updates the screen frame by frame.
        pygame.display.update()
    pygame.quit()