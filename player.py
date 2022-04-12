from hmac import new
from pickle import FALSE, TRUE
import platform
from turtle import speed
import pygame
    

player_image = pygame.image.load('Sprites/adventurer-idle-02.png')
player_x = 0
player_y = 0
player_speed = 0.0
player_width = 19
player_height = 30
ground = False
hook = []

# player input
def movementHorizantal(keys, x, y, w, h):
    new_player_x = x
    # a=left
    if keys[pygame.K_a]:
        new_player_x -= 2
    # d=right
    if keys[pygame.K_d]:
        new_player_x += 2
    new_player_rect = pygame.Rect(new_player_x, y,
                                      w, h)
    x_collision = False
    # ..check against every playform
    for p in platform.level1:
        if p.colliderect(new_player_rect):
            x_collision = TRUE
            new_player_x = x
            break

        #if x_collision is False:
         #  return new_player_x
    return new_player_x

def movementVertical(keys, x, y, w, h,  speed, ground):
    
    new_player_y = y
    player_speed = speed
    player_acceleration = 0.2
    player_speed += player_acceleration
    new_player_y += player_speed
    fall = [new_player_y, player_speed, ground]
    new_player_rect = pygame.Rect(x, new_player_y,
                                      w, h)
    y_collision = False
    if keys[pygame.K_w] and ground == TRUE:
            player_speed = -5
            ground = FALSE
    ground = FALSE
    # ..check against every playform
    for p in platform.level1:
        if p.colliderect(new_player_rect):
            player_speed = 0
            # if the platform is below the player
            if p[1] > new_player_y:
                # stick player to platform
                new_player_y = p[1] - player_height
                ground = TRUE
                fall = [new_player_y, player_speed, ground]
                break
        if y_collision is False:
            fall = [new_player_y,player_speed,ground]
    return fall      