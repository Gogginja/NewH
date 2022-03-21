from pickle import FALSE, TRUE
from tkinter import Y
import pygame
import platform
import player
import coin
class screen:
    SCREEN_SIZE = (700, 500)
    DARK_GREY = (50, 50, 50)
    GREEN = (16, 173, 42)
    clock = pygame.time.Clock()
    game_state = 'play'
    
    run  = TRUE
    while run == TRUE:
        pygame.init()
        screen = pygame.display.set_mode(SCREEN_SIZE)
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