import pygame
    

player_image = pygame.image.load('Sprites/adventurer-idle-02.png')
player_x = 0
player_y = 0
player_speed = 0
player_acceleration = 0.2
player_width = 19
player_height = 30
    

# player input
def movement():
    #new_player_x = player_x
    #new_player_y = player_y
    keys = pygame.key.get_pressed()
    # a=left
    if keys[pygame.K_a]:
        player_x -= 2
    # d=right
    if keys[pygame.K_d]:
        player_x += 2
    # w=jump (if on the ground)
    if keys[pygame.K_w] and player_y == 0:
        player_speed = -5
