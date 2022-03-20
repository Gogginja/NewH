from pickle import TRUE
import pygame
import platform
import player
class screen:
    SCREEN_SIZE = (700, 500)
    DARK_GREY = (50, 50, 50)
    GREEN = (16, 173, 42)
    
    run  = TRUE
    while run:
        pygame.init()
        screen = pygame.display.set_mode(SCREEN_SIZE)
        screen.fill(DARK_GREY)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.blit(player.player_image, (player.player_x, player.player_y))
        platform.makePlatform(screen,platform.platforms,GREEN)
        pygame.display.flip()
    pygame.quit()