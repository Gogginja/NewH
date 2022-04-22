import pygame
import platforms
import player
import coin
import animationHandler


class main:
    # GLOBAL VARIABLES #
    global SCREEN_SIZE, BACKGROUND_COLOR, DARK_GREY, GREEN
    global WHITE, DARK, screen, width, height, clock
    global screenList, currentScreen, paused, devMenu
    SCREEN_SIZE = (700, 500)
    MENU_COLOR = (50, 50, 50)
    DARK_GREY = (50, 50, 50)
    GREEN = (16, 173, 42)
    WHITE = (255, 255, 255)
    DARK = (100, 100, 100)
    screen = pygame.display.set_mode(SCREEN_SIZE)
    width = screen.get_width()
    height = screen.get_height()

    clock = pygame.time.Clock()
    devMenu = False

    screenList = ['mainMenu', 'levelSelect', 'settings', 'settings_audio',
                  'settings_gameplay', 'settings_video', 'level_1']

    currentScreen = 'mainMenu'
    previousScreen = ''
    paused = False
    run = True

    # Skyboxes #
    sky1 = pygame.image.load('Image/textures/skybox.png')
    sky2 = pygame.image.load('Image/textures/skybox2.png')
    sky3 = pygame.image.load('Image/textures/skybox3.png')

    # Get current pause state
    def getPaused():
        return paused

    # Get current screen
    def getScreen():
        return currentScreen

    # Draw a background
    def draw_bg(sky):
        width = sky.get_width()
        for x in range(4):
            screen.blit(sky, ((x * width), 0))

    # BUTTON CREATION FUNCTION #
    def createButton(text, x, y):
        smallfont = pygame.font.SysFont('Corbel', 20)
        buttonText = smallfont.render(text, True, WHITE)
        mouse = pygame.mouse.get_pos()
        if(x <= mouse[0] <= x + 140) and (y <= mouse[1] <= y + 40):
            pygame.draw.rect(screen, (255, 255, 255), [x, y, 140, 40])
        else:
            pygame.draw.rect(screen, (100, 100, 100), [x, y, 140, 40])
        # add text (centered on the button)
        screen.blit(buttonText, (x + 70 - buttonText.get_width() / 2,
                                 y + buttonText.get_height() / 2))

    # Create Text anywhere on the screen
    def createText(text, x, y):
        smallfont = pygame.font.SysFont('Corbel', 50)
        txt = smallfont.render(text, True, WHITE)
        screen.blit(txt, (x - txt.get_width() / 2, y - txt.get_height()))

    # Create Text with a frame anywhere on the screen
    def drawtext(t, x, y):
        font = pygame.font.Font(pygame.font.get_default_font(), 24)
        text = font.render(t, True, GREEN, DARK_GREY)
        text_rectangle = text.get_rect()
        text_rectangle.topleft = (x, y)
        screen.blit(text, text_rectangle)

    # PAUSE MENU #
    def pause():
        global currentScreen, paused, run
        window = pygame.Surface(SCREEN_SIZE)
        window.set_colorkey(DARK_GREY)
        window.set_alpha(200)
        smallfont = pygame.font.SysFont('Corbel', 50)
        pauseText = smallfont.render('PAUSED', True, WHITE)
        # PAUSE WHITE WINDOW
        screen.blit(window, (0, 0))
        # PAUSE TEXT
        screen.blit(pauseText, (350 - pauseText.get_width() / 2,
                                175 - pauseText.get_height()))

        mouse = pygame.mouse.get_pos()
        resumePos = [width / 2 - 70, height / 2.5]
        mainMenuPos = [width / 2 - 70, height / 2]
        quitPost = [width / 2 - 70, height / 1.65]

        # EVENT HANDLER #
        for ev in pygame.event.get():
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_TAB:
                    paused = not paused
            # If mouse clicks:
            if ev.type == pygame.MOUSEBUTTONDOWN:
                # Resume
                if(resumePos[0] <= mouse[0]
                                <= resumePos[0] + 140) and (
                                resumePos[1] <= mouse[1]
                                <= resumePos[1] + 40):
                    paused = False
                # Main Menu
                elif(mainMenuPos[0] <= mouse[0]
                                    <= mainMenuPos[0] + 140) and (
                                    mainMenuPos[1] <= mouse[1]
                                    <= mainMenuPos[1] + 40):
                    currentScreen = 'mainMenu'
                    paused = False
                # Quit
                elif(quitPost[0] <= mouse[0]
                                 <= quitPost[0] + 140) and (
                                 quitPost[1] <= mouse[1]
                                 <= quitPost[1] + 40):
                    pygame.quit()
            if ev.type == pygame.QUIT:
                run = False

# MAIN GAME LOOP #
    while run:
        # Initialize pygame
        pygame.init()
        # Get mouse position
        mouse = pygame.mouse.get_pos()
        # Get the keys pressed
        keys = pygame.key.get_pressed()
        # Font to use for buttons/text
        font = pygame.font.Font(pygame.font.get_default_font(), 24)

        # Generate background
        screen.fill(MENU_COLOR)
        # set FPS
        clock.tick(60)

# --------------- MAIN MENU --------------- #

        if currentScreen == 'mainMenu':
            # BUTTON SETTINGS #
            levelSelect = [width / 6, height / 6]
            settingsPos = [width / 6, height / 3]
            quitPos = [width / 6, height / 2]

            # EVENT HANDLER #
            for ev in pygame.event.get():
                # If mouse clicks:
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    # Level Select
                    if(levelSelect[0] <= mouse[0]
                                      <= levelSelect[0] + 140) and (
                                      levelSelect[1] <= mouse[1]
                                      <= levelSelect[1] + 40):
                        currentScreen = 'level_select'
                    # Settings
                    elif(settingsPos[0] <= mouse[0]
                                        <= settingsPos[0] + 140) and (
                                        settingsPos[1] <= mouse[1]
                                        <= settingsPos[1] + 40):
                        currentScreen = 'settings'
                    # Quit
                    elif(quitPos[0] <= mouse[0]
                                    <= quitPos[0] + 140) and (
                                    quitPos[1] <= mouse[1]
                                    <= quitPos[1] + 40):
                        pygame.quit()

            # Create Title on main menu
            smallfont = pygame.font.SysFont('Corbel', 100)
            txt = smallfont.render('Star Dust', True, WHITE)
            screen.blit(txt, (475 - txt.get_width() / 2,
                              250 - txt.get_height()))

            # BUTTON CREATION #
            createButton('SELECT LEVEL', levelSelect[0], levelSelect[1])
            createButton('SETTINGS', settingsPos[0], settingsPos[1])
            createButton('QUIT', quitPos[0], quitPos[1])

# --------------- SETTINGS - MAIN --------------- #

        if currentScreen == 'settings':
            # BUTTON SETTINGS #
            audioPos = [width / 6, height / 6]
            gameplayPos = [width / 6, height / 3]
            videoPos = [width / 6, height / 2]
            backPos = [width / 1.5, height / 1.5]

            # EVENT HANDLER #
            for ev in pygame.event.get():
                # If mouse clicks:
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    # Audio
                    if(audioPos[0] <= mouse[0]
                                   <= audioPos[0] + 140) and (
                                   audioPos[1] <= mouse[1]
                                   <= audioPos[1] + 40):
                        currentScreen = 'settings_audio'
                    # Gameplay
                    elif(gameplayPos[0] <= mouse[0]
                                        <= gameplayPos[0] + 140) and (
                                        gameplayPos[1] <= mouse[1]
                                        <= gameplayPos[1] + 40):
                        currentScreen = 'settings_gameplay'
                    # Video
                    elif(videoPos[0] <= mouse[0]
                                     <= videoPos[0] + 140) and (
                                     videoPos[1] <= mouse[1]
                                     <= videoPos[1] + 40):
                        currentScreen = 'settings_video'
                    # Back
                    elif(backPos[0] <= mouse[0]
                                    <= backPos[0] + 140) and (
                                    backPos[1] <= mouse[1]
                                    <= backPos[1] + 40):
                        currentScreen = 'mainMenu'

            # BUTTON CREATION #
            createButton('AUDIO', audioPos[0], audioPos[1])
            createButton('GAMEPLAY', gameplayPos[0], gameplayPos[1])
            createButton('VIDEO', videoPos[0], videoPos[1])
            createButton('BACK', backPos[0], backPos[1])

# --------------- SETTIGNS - AUDIO --------------- #

        if currentScreen == 'settings_audio':
            # BUTTON SETTINGS #
            backPos = [width/1.5, height/1.5]

            # EVENT HANDLER #
            for ev in pygame.event.get():
                # If mouse clicks:
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    # Back
                    if(backPos[0] <= mouse[0]
                                  <= backPos[0] + 140) and (
                                  backPos[1] <= mouse[1]
                                  <= backPos[1] + 40):
                        currentScreen = 'settings'

            # BUTTON CREATION #
            createButton('BACK', backPos[0], backPos[1])

# --------------- SETTIGNS - GAMEPLAY --------------- #

        if currentScreen == 'settings_gameplay':
            # BUTTON SETTINGS #
            backPos = [width / 1.5, height / 1.5]

            # EVENT HANDLER #
            for ev in pygame.event.get():
                # If mouse clicks:
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    # Back
                    if(backPos[0] <= mouse[0]
                                  <= backPos[0] + 140) and (
                                  backPos[1] <= mouse[1]
                                  <= backPos[1] + 40):
                        currentScreen = 'settings'

            # BUTTON CREATION #
            createButton('BACK', backPos[0], backPos[1])

# --------------- SETTIGNS - VIDEO --------------- #

        if currentScreen == 'settings_video':
            # BUTTON SETTINGS #
            backPos = [width / 1.5, height / 1.5]

            # EVENT HANDLER #
            for ev in pygame.event.get():
                # If mouse clicks:
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    # Back
                    if(backPos[0] <= mouse[0]
                                  <= backPos[0] + 140) and (
                                  backPos[1] <= mouse[1]
                                  <= backPos[1] + 40):
                        currentScreen = 'settings'

            # BUTTON CREATION #
            createButton('BACK', backPos[0], backPos[1])

# --------------- LEVEL SELECT --------------- #

        if currentScreen == 'level_select':
            # BUTTON SETTINGS #
            level1Pos = [width / 2-70, height / 3]
            level2Pos = [width / 2-70, height / 2]
            level3Pos = [width / 2-70, height / 1.5]
            backPos = [width / 1.5, height / 1.5]

            # EVENT HANDLER #
            for ev in pygame.event.get():
                # If mouse clicks:
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    # Back
                    if(backPos[0] <= mouse[0]
                                  <= backPos[0] + 140) and (
                                  backPos[1] <= mouse[1]
                                  <= backPos[1] + 40):
                        currentScreen = 'mainMenu'
                    # Level 1
                    elif(level1Pos[0] <= mouse[0]
                                      <= level1Pos[0] + 140) and (
                                      level1Pos[1] <= mouse[1]
                                      <= level1Pos[1] + 40):
                        player.canMove = True
                        # Change to level 1
                        currentScreen = 'level_1'
                        # Reset player position and speed
                        player.player_x = 0
                        player.player_y = 0
                        player.player_speed = 0
                    # Level 2
                    elif(level2Pos[0] <= mouse[0]
                                      <= level2Pos[0] + 140) and (
                                      level2Pos[1] <= mouse[1]
                                      <= level2Pos[1] + 40):
                        # If level is locked:
                        if not platforms.locked2:
                            player.canMove = True
                            # Change to level 2
                            currentScreen = 'level_2'
                            # Reset player position and speed
                            player.player_x = 0
                            player.player_y = 0
                            player.player_speed = 0
                        else:
                            # DISPLAY LOCKED TEXT
                            createText('LOCKED', 350, 115)
                    # Level 3
                    elif(level3Pos[0] <= mouse[0]
                                      <= level3Pos[0] + 140) and (
                                      level3Pos[1] <= mouse[1]
                                      <= level3Pos[1] + 40):
                        # If level is not locked:
                        if not platforms.locked3:
                            player.canMove = True
                            # Change to level 3
                            currentScreen = 'level_3'
                            # Reset player position and speed
                            player.player_x = 0
                            player.player_y = 0
                            player.player_speed = 0
                        # If locked
                        else:
                            # DISPLAY LOCKED TEXT
                            createText('LOCKED', 350, 115)

            # HOVER FUNCTIONALITY #
            # Level 1
            if(level2Pos[0] <= mouse[0]
                            <= level2Pos[0] + 140) and (
                            level2Pos[1] <= mouse[1]
                            <= level2Pos[1] + 40):
                # If level is locked
                if platforms.locked2:
                    createText('LOCKED', 350, 115)
            # Level 3
            elif(level3Pos[0] <= mouse[0]
                              <= level3Pos[0] + 140) and (
                              level3Pos[1] <= mouse[1]
                              <= level3Pos[1] + 40):
                # If level is locked
                if platforms.locked3:
                    createText('LOCKED', 350, 115)

            # BUTTON CREATION #
            createButton('LEVEL 1', level1Pos[0], level1Pos[1])
            createButton('LEVEL 2', level2Pos[0], level2Pos[1])
            createButton('LEVEL 3', level3Pos[0], level3Pos[1])
            createButton('BACK', backPos[0], backPos[1])

# --------------- LEVEL 1 --------------- 3

        if currentScreen == 'level_1':
            # Draws the background, score, and lives count
            draw_bg(sky1)
            drawtext('Score: ' + str(coin.score) + ' ', 0, 10)
            drawtext('Lives: ' + str(player.player_life) + ' ', 100, 10)

            # Generate starcoins
            for c in coin.coin1:
                screen.blit(coin.coin_image, (c[0], c[1]))

            # Generate End Goal
            pygame.draw.rect(screen, coin.RED, coin.goal1[0])

            # Generate Player
            screen.blit(player.current_image, (player.player_x,
                                               player.player_y))

            # Keep track of starcoins collected
            coin.score += coin.collect(player.player_x, player.player_y,
                                       coin.coin1)

            # If end goal is reached:
            if coin.end(player.player_x, player.player_y, coin.goal1):
                # Unlock level 2
                platforms.locked2 = False
                # View the Win Menu
                currentScreen = 'winMenu'
                # Reset the player
                player.player_x = 0
                player.player_y = 0
            # Generate the platformss
            platforms.makePlatform(screen, platforms.level1, GREEN)

            # If game is paused
            if not paused:
                # Set the x coordinates of the player
                player.player_x = player.movement(keys, player.player_x,
                                                  player.player_y,
                                                  player.player_width,
                                                  player.player_height,
                                                  player.player_speed,
                                                  player.ground,
                                                  platforms.level1)[0]
                # Calculate the fall data of the player
                fall = player.movement(keys, player.player_x, player.player_y,
                                       player.player_width,
                                       player.player_height,
                                       player.player_speed, player.ground,
                                       platforms.level1)[1]
                # Set y coordinates, speed, and ground toggle of the player
                player.player_y = fall[0]
                player.player_speed = fall[1]
                player.ground = fall[2]
            # If not paused
            else:
                # Make pause menu appear
                pause()
                # BUTTON CREATION #
                resumePos = [width/2-70, height/2.5]
                mainMenuPos = [width/2-70, height/2]
                quitPost = [width/2-70, height/1.65]
                createButton('RESUME', resumePos[0], resumePos[1])
                createButton('MAIN MENU', mainMenuPos[0], mainMenuPos[1])
                createButton('QUIT', quitPost[0], quitPost[1])

# --------------- LEVEL 2 --------------- #

        if currentScreen == 'level_2':
            # Draws the background, score, and lives count
            draw_bg(sky2)
            drawtext('Score: ' + str(coin.score)+' ', 0, 10)
            drawtext('Lives: ' + str(player.player_life) + ' ', 100, 10)

            # Generate starcoins
            for c in coin.coin2:
                screen.blit(coin.coin_image, (c[0], c[1]))

            # Generate end goal
            pygame.draw.rect(screen, coin.RED, coin.goal2[0])

            # Generate player
            screen.blit(player.current_image, (player.player_x,
                                               player.player_y))

            # Keep track of starcoins collected
            coin.score += coin.collect(player.player_x, player.player_y,
                                       coin.coin2)
            # If end goal is reached:
            if coin.end(player.player_x, player.player_y, coin.goal2):
                # Unlocked level 3
                platforms.locked3 = False
                # View the Win Menu
                currentScreen = 'winMenu'
                # Reset the player
                player.player_x = 0
                player.player_y = 0
            # Generate the platformss
            platforms.makePlatforms(screen, platforms.level2, GREEN)

            # If game is paused:
            if not paused:
                # Set the x coordinates of the player
                player.player_x = player.movement(keys, player.player_x,
                                                  player.player_y,
                                                  player.player_width,
                                                  player.player_height,
                                                  player.player_speed,
                                                  player.ground,
                                                  platforms.level2)[0]
                # Calculate the fall data of the player
                fall = player.movement(keys, player.player_x, player.player_y,
                                       player.player_width,
                                       player.player_height,
                                       player.player_speed, player.ground,
                                       platforms.level2)[1]
                # Set y coordinates, speed, and ground toggle of the player
                player.player_y = fall[0]
                player.player_speed = fall[1]
                player.ground = fall[2]
            # If not paused:
            else:
                # Make pause menu appear
                pause()
                # BUTTON CREATION #
                resumePos = [width/2-70, height/2.5]
                mainMenuPos = [width/2-70, height/2]
                quitPost = [width/2-70, height/1.65]
                createButton('RESUME', resumePos[0], resumePos[1])
                createButton('MAIN MENU', mainMenuPos[0], mainMenuPos[1])
                createButton('QUIT', quitPost[0], quitPost[1])

# --------------- LEVEL 3 --------------- #

        if currentScreen == 'level_3':
            # Draws the background, score, and lives count
            draw_bg(sky3)
            drawtext('Score: ' + str(coin.score) + ' ', 0, 10)
            drawtext('Lives: ' + str(player.player_life) + ' ', 100, 10)

            # Generate starcoins
            for c in coin.coin3:
                screen.blit(coin.coin_image, (c[0], c[1]))

            # Generate the end goal
            pygame.draw.rect(screen, coin.RED, coin.goal3[0])
            # Generate the player
            screen.blit(player.current_image, (player.player_x,
                                               player.player_y))

            # Keep track of starcoins collected
            coin.score += coin.collect(player.player_x, player.player_y,
                                       coin.coin3)
            # If end goal is reached:
            if coin.end(player.player_x, player.player_y, coin.goal3):
                # View the Win Menu
                currentScreen = 'winMenu'
                # Reset the player
                player.player_x = 0
                player.player_y = 0
            # Generate the platformss
            platforms.makeplatforms(screen, platforms.level3, GREEN)

            # If game is not paused:
            if not paused:
                # Set the x coordinates of the player
                player.player_x = player.movement(keys, player.player_x,
                                                  player.player_y,
                                                  player.player_width,
                                                  player.player_height,
                                                  player.player_speed,
                                                  player.ground,
                                                  platforms.level3)[0]
                # Calculate the fall data of the player
                fall = player.movement(keys, player.player_x, player.player_y,
                                       player.player_width,
                                       player.player_height,
                                       player.player_speed, player.ground,
                                       platforms.level3)[1]
                # Set y coordinates, speed, and ground toggle of the player
                player.player_y = fall[0]
                player.player_speed = fall[1]
                player.ground = fall[2]
            # If paused:
            else:
                # View the pause menu
                pause()
                # BUTTON CREATION #
                resumePos = [width / 2 - 70, height / 2.5]
                mainMenuPos = [width / 2 - 70, height / 2]
                quitPost = [width / 2 - 70, height / 1.65]
                createButton('RESUME', resumePos[0], resumePos[1])
                createButton('MAIN MENU', mainMenuPos[0], mainMenuPos[1])
                createButton('QUIT', quitPost[0], quitPost[1])

# --------------- DEATH MENU --------------- #

        if currentScreen == 'deathScreen':
            # Button positions
            respawnPos = [width / 2 - 70, height / 2]
            mainMenuPos = [width / 2 - 70, height / 1.65]
            # Background of menu
            window = pygame.Surface((700, 500))
            window.set_colorkey((10, 10, 10))
            smallfont = pygame.font.SysFont('Corbel', 50)
            # If player has more than 3 lives:
            if player.player_life > 0:
                # Display 'YOU DIED'
                diedText = smallfont.render('YOU DIED', True, (255, 255, 255))
            # If player has no lives left:
            else:
                # Display 'GAME OVER'
                diedText = smallfont.render('GAME OVER', True, (255, 255, 255))

            # Generate background
            screen.blit(window, (0, 0))
            # Generate text
            screen.blit(diedText, (350-diedText.get_width()/2,
                        175-diedText.get_height()))
            # Reset animation
            player.frameNum = 0
            # Start death animation
            animationHandler.animate()
            # Display the player
            screen.blit(player.current_image, (340, 200))

            # EVENT HANDLER #
            for ev in pygame.event.get():
                # If mouse clicks:
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    # Back
                    if(respawnPos[0] <= mouse[0]
                                     <= respawnPos[0] + 140) and (
                                     respawnPos[1] <= mouse[1]
                                     <= respawnPos[1] + 40):
                        # Show the previous screen
                        currentScreen = previousScreen
                        # Player allowed to move
                        canMove = True
                    # Level 1
                    elif(mainMenuPos[0] <= mouse[0]
                                        <= mainMenuPos[0] + 140) and (
                                        mainMenuPos[1] <= mouse[1]
                                        <= mainMenuPos[1] + 40):
                        # Go to main menu
                        currentScreen = 'mainMenu'
                        # Reset the life count
                        player.player_life = 3
                        # Reset the score
                        coin.score = 0
                        # If was playing level 1:
                        if previousScreen == 'level_1':
                            # Reset coins
                            coin.coin1 = coin.copy1
                        # If was playing level 2:
                        elif previousScreen == 'level_2':
                            # Reset coins
                            coin.coin2 = coin.copy2
                        # If was playing level 3:
                        elif previousScreen == 'level_3':
                            # Reset coins
                            coin.coin3 = coin.copy3

            # BUTTON CREATION #
            # If player has lives:
            if player.player_life > 0:
                createButton('RESPAWN', respawnPos[0], respawnPos[1])
            createButton('MAIN MENU', mainMenuPos[0], mainMenuPos[1])

# --------------- WIN MENU --------------- #

        if currentScreen == 'winMenu':
            # Button positions
            mainMenuPos = [width / 2 - 70, height / 2]
            quitPos = [width / 2 - 70, height / 1.65]
            # Background of menu
            window = pygame.Surface((700, 500))
            window.set_colorkey((10, 10, 10))
            smallfont = pygame.font.SysFont('Corbel', 50)
            winText = smallfont.render('YOU WON!', True, (255, 255, 255))
            # Generate the background
            screen.blit(window, (0, 0))
            # Generate the text
            screen.blit(winText, (350-winText.get_width()/2,
                        175-winText.get_height()))
            # Change player state to won
            player.state = 'won'
            # Reset player animation
            player.frameNum = 0
            # Animate the player
            animationHandler.animate()
            # Display the player
            screen.blit(player.current_image, (340, 200))

            # EVENT HANDLER #
            for ev in pygame.event.get():
                # If mouse clicks:
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    # Back
                    if(mainMenuPos[0] <= mouse[0]
                                      <= mainMenuPos[0] + 140) and (
                                      mainMenuPos[1] <= mouse[1]
                                      <= mainMenuPos[1] + 40):
                        # Go to the main menu
                        currentScreen = 'mainMenu'
                        # ALlow the player to move
                        canMove = True
                    # Level 1
                    elif (quitPos[0] <= mouse[0]
                                     <= quitPos[0] + 140) and (
                                     quitPos[1] <= mouse[1]
                                     <= quitPos[1] + 40):
                        # Quit the program
                        pygame.quit()

            # BUTTON CREATION #
            createButton('MAIN MENU', mainMenuPos[0], mainMenuPos[1])
            createButton('QUIT', quitPos[0], quitPos[1])

# --------------- DEV MENU - (FOR DEBUGGING) --------------- #

        if devMenu:
            # View real-time state of player
            drawtext('State: ' + str(player.state) + ' ', 200, 10)

        # If player falls off map:
        if player.player_y > 500:
            # Can not move
            canMove = False
            # Reset animation
            player.frameNum = 0
            # Lose a life
            player.player_life -= 1
            # Reset the player
            player.player_x = 0
            player.player_y = 0
            player.player_speed = 0
            # Set state to died
            player.state = 'died'
            # Save previous screen
            previousScreen = currentScreen
            # View death menu
            currentScreen = 'deathScreen'

        # Check pygame events
        for ev in pygame.event.get():
            # If [X] on window is pressed:
            if ev.type == pygame.QUIT:
                pygame.quit()
            # If [key] is pressed:
            if ev.type == pygame.KEYDOWN:
                # If [Tab] is pressed:
                if ev.key == pygame.K_TAB:
                    # Toggle pausing
                    paused = not paused
                # If [F9] is pressed:
                elif ev.key == pygame.K_F9:
                    # Toggle developer info
                    devMenu = not devMenu

        # Refreshes/Updates the screen frame by frame.
        # Set window name
        pygame.display.set_caption('Star Dust')
        pygame.display.flip()
        # Update frame
        pygame.display.update()
    # Quit the program
    pygame.quit()
