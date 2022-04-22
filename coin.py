import pygame
import player

coin_image = pygame.image.load('Image/coin11.png')
coin1 = [
    pygame.Rect(600, 150, 22, 22),
    pygame.Rect(200, 250, 22, 22)
    ]
coin2 = [
    pygame.Rect(550, 150, 22, 22),
    pygame.Rect(200, 350, 22, 22)
    ]
coin3 = [
    pygame.Rect(600, 150, 22, 22),
    pygame.Rect(200, 250, 22, 22)
    ]
RED = (237, 12, 12)
goal = [
    pygame.Rect(350, 0, 10, 30)
    ]
score = 0

def collect(x, y, coin):
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
    for g in goal:
            if g.colliderect(player_rect):
                player.canMove = False
                player.state = 'won'
                return True
            else:
                return False
    else:
        return False