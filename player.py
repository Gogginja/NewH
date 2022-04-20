from asyncio.windows_events import NULL
from hmac import new
from pickle import FALSE, TRUE
import platform
from turtle import speed
import pygame

global run_anim, idle_anim, current_index, current_image
run_anim = [
    pygame.image.load('Sprites/run/adventurer-run-00.png'),
    pygame.image.load('Sprites/run/adventurer-run-01.png'),
    pygame.image.load('Sprites/run/adventurer-run-02.png'),
    pygame.image.load('Sprites/run/adventurer-run-03.png'),
    pygame.image.load('Sprites/run/adventurer-run-04.png'),
    pygame.image.load('Sprites/run/adventurer-run-05.png')
]
idle_anim = [
    pygame.image.load('Sprites/idle/adventurer-idle-00.png'),
    pygame.image.load('Sprites/idle/adventurer-idle-01.png'),
    pygame.image.load('Sprites/idle/adventurer-idle-02.png'),
    pygame.image.load('Sprites/idle/adventurer-idle-03.png')
]
jump_anim = [
    pygame.image.load('Sprites/jump/jump-00.png'),
    pygame.image.load('Sprites/jump/jump-01.png'),
    pygame.image.load('Sprites/jump/jump-02.png'),
    pygame.image.load('Sprites/jump/jump-03.png')
]
cornerJump_anim = [
    pygame.image.load('Sprites/jump/jump-00.png'),
    pygame.image.load('Sprites/jump/jump-01.png'),
    pygame.image.load('Sprites/jump/crnr-jump-00.png'),
    pygame.image.load('Sprites/jump/crnr-jump-01.png'),
    pygame.image.load('Sprites/jump/crnr-jump-02.png')
]
fall_anim = [
    pygame.image.load('Sprites/fall/fall-00.png'),
    pygame.image.load('Sprites/fall/fall-01.png')
]

current_index = 0
current_image = pygame.image.load('Sprites/idle/adventurer-idle-00.png')
state = 'idle'
# True = right : False = left
direction = True
deb = 0

player_x = 0
player_y = 0
player_speed = 0.0
player_width = 19
player_height = 30
ground = False

# player input
def movement(keys, x, y, w, h, speed, ground, level):
    animate()
    global state,direction

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
    # a=left
    if keys[pygame.K_a]:
        state = 'run'
        direction = False
        new_player_x -= 2
    # d=right
    elif keys[pygame.K_d]:
        state = 'run'
        direction = True
        new_player_x += 2
    elif not (keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d] or keys[pygame.K_w]):
        state = 'idle'
    # W = Jump
    if keys[pygame.K_w] and ground == TRUE:
        state = 'jumping'
        player_speed = -5
        ground = FALSE
    # W + A = Left Jump
    if keys[pygame.K_w] and keys[pygame.K_a]:
        state = 'jumping-left'
        direction = False
    # W + D = Right Junmp
    elif keys[pygame.K_w] and keys[pygame.K_d]:
        state = 'jumping-right'
        direction = True
    ground = FALSE

    # If player is falling
    if player_speed >= 0:
        state = 'falling'
    
    # COLLISION HANDLER
    new_player_rect = pygame.Rect(new_player_x, y, w, h)
    x_collision = False
    # ..check against every playform
    for p in level:
        if p.colliderect(new_player_rect):
            x_collision = TRUE
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
                ground = TRUE
                fall = [new_player_y, player_speed, ground]
                break
        if y_collision is False:
            fall = [new_player_y,player_speed,ground]
        #if x_collision is False:
        #  return new_player_x
    return [new_player_x, fall]

def animate():
    global state,current_image,current_index,deb

    def playAnim(animList):
        global state,current_image,current_index,deb
        if current_index > len(animList)-1:
            current_index = 0
        current_index += 1
        if current_index == len(animList):
            current_index = 0
        if direction:
            current_image = animList[current_index]
        else:
            imgCopy = animList[current_index].copy()
            current_image = pygame.transform.flip(imgCopy, True, False)

    if state == 'idle':
        deb += 1
        # Every 5 frames, update the animation to the next frame
        if deb == 5:
            # if idle
            playAnim(idle_anim)
        elif deb > 15:
            deb = 0
    elif state == 'run':
        deb += 1
        # Every 2 frames, update the animation to the next frame
        if deb == 2:
            # if idle
            playAnim(run_anim)
        elif deb > 15:
            deb = 0
    elif state == 'jumping':
        deb += 1
        # Every 2 frames, update the animation to the next frame
        if deb == 2:
            # if idle
            playAnim(jump_anim)
        elif deb > 15:
            deb = 0
    elif state == 'jumping-left':
        deb += 1
        # Every 2 frames, update the animation to the next frame
        if deb == 2:
            # if idle
            playAnim(cornerJump_anim)
        elif deb > 15:
            deb = 0
    elif state == 'jumping-right':
        deb += 1
        # Every 2 frames, update the animation to the next frame
        if deb == 2:
            # if idle
            playAnim(cornerJump_anim)
        elif deb > 15:
            deb = 0
    elif state == 'falling':
        deb += 1
        # Every 5 frames, update the animation to the next frame
        if deb == 5:
            # if idle
            playAnim(fall_anim)
        elif deb > 15:
            deb = 0
