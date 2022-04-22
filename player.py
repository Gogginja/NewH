import platform
import animationHandler
import pygame

current_index = 0
current_image = pygame.image.load('Sprites/idle/adventurer-idle-00.png')
state = 'idle'
# True = right : False = left
direction = True
deb = 0
frameNum = 0

canMove = True
player_life = 3
player_x = 0
player_y = 0
player_speed = 0.0
player_width = 19
player_height = 30
ground = False

# player input
def movement(keys, x, y, w, h, speed, ground, level):
    animationHandler.animate()
    global state,direction,player_speed,current_image,player_height,player_y,canMove

    if not (keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d] or keys[pygame.K_w]):
        state = 'idle'
        canMove = True

    if canMove:
        new_player_x = x
        new_player_y = y
        player_speed = speed
        player_acceleration = 0.2
        player_speed += player_acceleration
        new_player_y += player_speed
        fall = [new_player_y, player_speed, ground]
        new_player_rect = pygame.Rect(x, new_player_y,
                                        w, h)
        y_collision = False
        player_height = current_image.get_height()

        # a=left
        if keys[pygame.K_a] and state != 'crouching':
            state = 'run'
            direction = False
            new_player_x -= 3
        # d=right
        elif keys[pygame.K_d] and state != 'crouching':
            state = 'run'
            direction = True
            new_player_x += 3
        # W = Jump
        if keys[pygame.K_w] and ground == True:
            state = 'jumping'
            player_speed = -7
            ground = False
        # W + A = Left Jump
        if keys[pygame.K_w] and keys[pygame.K_a]:
            state = 'jumping-left'
            direction = False
        # W + D = Right Junmp
        elif keys[pygame.K_w] and keys[pygame.K_d]:
            state = 'jumping-right'
            direction = True
        elif keys[pygame.K_s] and ground == True:
            state = 'crouching'
            player_y += 7
            player_speed = 0
            canMove = False

        # If player is falling
        if player_speed > 1:
            state = 'falling'

        # COLLISION HANDLER
        new_player_rect = pygame.Rect(new_player_x, y, w, h)
        x_collision = False
        # ..check against every playform
        for p in level:
            if p.colliderect(new_player_rect):
                x_collision = True
                new_player_x = x
                break

        # ..check against every playform
        for p in level:
            if p.colliderect(new_player_rect):
                player_speed = 0
                # if the platform is below the player
                if p[1] > new_player_y:
                    # stick player to platform
                    new_player_y = p[1] - player_height
                    ground = True
                    fall = [new_player_y, player_speed, ground]
                    break
            if y_collision is False:
                fall = [new_player_y,player_speed,ground]

        return [new_player_x, fall]
    else:
        return [player_x, [player_y,player_speed,ground]]
    