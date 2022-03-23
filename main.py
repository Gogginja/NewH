from pickle import FALSE, TRUE
from tkinter import Y
from turtle import _Screen
from types import NoneType

import pygame
import platform
import player
import coin

class main:
    global SCREEN_SIZE,DARK_GREY,GREEN,WHITE,DARK,screen,width,height,mouse,clock,game_state,currentLevel
    SCREEN_SIZE = (700, 500)
    DARK_GREY = (50, 50, 50)
    GREEN = (16, 173, 42)
    WHITE = (255,255,255)
    DARK = (100,100,100)
    screen = pygame.display.set_mode(SCREEN_SIZE)
    width = screen.get_width()
    height = screen.get_height()
    mouse = pygame.mouse.get_pos()

    clock = pygame.time.Clock()
    game_state = 'play'
    currentLevel = 0
    
    run  = TRUE
    while run == TRUE:
        pygame.init()

############################ MAIN MENU CONFIG ################################

        if currentLevel == 0:
            # BUTTON SETTINGS #
            beginPos = [width/6, height/6]
            settingsPos = [width/6, height/3]
            quitPos = [width/6, height/2]
            mouse = pygame.mouse.get_pos()

            # BUTTON CREATION FUNCTION #
            def createButton(text, x, y):
                smallfont = pygame.font.SysFont('Corbel',35)
                buttonText = smallfont.render(text, True, WHITE)
                mouse = pygame.mouse.get_pos() 
                if (x <= mouse[0] <= x+140) and (y <= mouse[1] <= y+40): 
                    pygame.draw.rect(screen,(255,255,255),[x,y,140,40]) 
                else: 
                    pygame.draw.rect(screen,(100,100,100),[x,y,140,40])
                screen.blit(buttonText, (x+40, y)) 

            for ev in pygame.event.get(): 
                if ev.type == pygame.QUIT: 
                    pygame.quit() 
                # If mouse is click:
                if ev.type == pygame.MOUSEBUTTONDOWN: 
                    #If mouse clicks BEGIN then create Level 1.
                    if (beginPos[0] <= mouse[0] <= beginPos[0]+140) and (beginPos[1] <= mouse[1] <= beginPos[1]+40): 
                        currentLevel = 1
                    elif (settingsPos[0] <= mouse[0] <= settingsPos[0]+140) and (settingsPos[1] <= mouse[1] <= settingsPos[1]+40): 
                        print('PRESSED SETTINGS')
                    elif (quitPos[0] <= mouse[0] <= quitPos[0]+140) and (quitPos[1] <= mouse[1] <= quitPos[1]+40): 
                        pygame.quit()
                    
            # fills the screen with a color 
            screen.fill((60,25,60))  
            
            # BUTTON CREATION #
            createButton('BEGIN', beginPos[0], beginPos[1]) 
            createButton('SETTINGS', settingsPos[0], settingsPos[1]) 
            createButton('QUIT', quitPos[0], quitPos[1]) 
            
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