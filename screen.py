from pickle import FALSE, TRUE
from tkinter import Y
from types import NoneType
import pygame
import sys
import platform
import player
import coin

class screen:
    SCREEN_SIZE = (700, 500)
    DARK_GREY = (50, 50, 50)
    GREEN = (16, 173, 42)
    WHITE = (255,255,255)
    DARK = (100,100,100)
    screen = pygame.display.set_mode(SCREEN_SIZE)
    width = screen.get_width()
    height = screen.get_height()

    clock = pygame.time.Clock()
    game_state = 'play'
    currentLevel = 0
    
    run  = TRUE
    while run == TRUE:
        pygame.init()

############################ MAIN MENU CONFIG ################################

        if currentLevel == 0:
            smallfont = pygame.font.SysFont('Corbel',35)
            startText = smallfont.render('Begin', True, WHITE)
            # QUIT BUTTON NOT MADE YET
            quitText = smallfont.render('Quit', True, WHITE)

            mouse = pygame.mouse.get_pos() 
            for ev in pygame.event.get(): 
                if ev.type == pygame.QUIT: 
                    pygame.quit() 
                # If mouse is click:
                if ev.type == pygame.MOUSEBUTTONDOWN: 
                    #If mouse clicks button then quit game.
                    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
                        currentLevel = 1 
                    
            # fills the screen with a color 
            screen.fill((60,25,60))  
            
            # If mouse hovers on button change to lighter shade. 
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
                pygame.draw.rect(screen,WHITE,[width/2,height/2,140,40]) 
            else: 
                pygame.draw.rect(screen,DARK,[width/2,height/2,140,40]) 
            
            # Put text onto the button 
            screen.blit(startText , (width/2+50,height/2)) 
            
            # CRITICAL (DO NOT DELETE). Refreshes/Updates the screen frame by frame.
            pygame.display.update()

############################ LEVEL 1 CONFIG ################################

        if currentLevel == 1:
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
            clock.tick(60)
    pygame.quit()