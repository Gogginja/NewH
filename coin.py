from pickle import FALSE, TRUE
import pygame
import player
coin_image = pygame.image.load('Image/coin11.png')
coin = [
    pygame.Rect(600, 150, 22, 22),
    pygame.Rect(200, 250, 22, 22)
    ]
RED = (237, 12, 12)
goal = pygame.Rect(350, 0, 10, 30)

score = 0

def collect(x, y):
    player_x = x
    player_y = y
    player_rect = pygame.Rect(player_x, player_y,
                            player.player_width, player.player_height)
    if coin != []:
        for c in coin:
            if c.colliderect(player_rect):
                coin.remove(c)
                return 1
            else:
                return 0
    else:
        return 0
        
def end(x, y):
    player_x = x
    player_y = y
    player_rect = pygame.Rect(player_x, player_y,
                              player.player_width, player.player_height)
    if goal.colliderect(player_rect):       
        return FALSE
    else:
        return TRUE