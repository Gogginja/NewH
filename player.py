import platform
from turtle import speed
import pygame

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
crouch_anim = [
    pygame.image.load('Sprites/crouch/crouch-00.png'),
    pygame.image.load('Sprites/crouch/crouch-01.png'),
    pygame.image.load('Sprites/crouch/crouch-02.png'),
    pygame.image.load('Sprites/crouch/crouch-03.png')
]
death_anim = [
    pygame.image.load('Sprites/die/die-00.png'),
    pygame.image.load('Sprites/die/die-01.png'),
    pygame.image.load('Sprites/die/die-02.png'),
    pygame.image.load('Sprites/die/die-03.png'),
    pygame.image.load('Sprites/die/die-04.png'),
    pygame.image.load('Sprites/die/die-05.png'),
    pygame.image.load('Sprites/die/die-06.png')
]
win_anim = [
    pygame.image.load('Sprites/win/attack1-00.png'),
    pygame.image.load('Sprites/win/attack1-01.png'),
    pygame.image.load('Sprites/win/attack1-02.png'),
    pygame.image.load('Sprites/win/attack1-03.png'),
    pygame.image.load('Sprites/win/attack1-04.png'),
    pygame.image.load('Sprites/win/attack2-00.png'),
    pygame.image.load('Sprites/win/attack2-01.png'),
    pygame.image.load('Sprites/win/attack2-02.png'),
    pygame.image.load('Sprites/win/attack2-03.png'),
    pygame.image.load('Sprites/win/attack2-04.png'),
    pygame.image.load('Sprites/win/attack2-05.png'),
    pygame.image.load('Sprites/win/attack3-00.png'),
    pygame.image.load('Sprites/win/attack3-01.png'),
    pygame.image.load('Sprites/win/attack3-02.png'),
    pygame.image.load('Sprites/win/attack3-03.png'),
    pygame.image.load('Sprites/win/attack3-04.png'),
    pygame.image.load('Sprites/win/attack3-05.png')
]

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
    animate()
    global state,direction,player_speed,current_image
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
        # a=left
        if keys[pygame.K_a] and state != 'crouching':
            state = 'run'
            direction = False
            new_player_x -= 2
        # d=right
        elif keys[pygame.K_d] and state != 'crouching':
            state = 'run'
            direction = True
            new_player_x += 2
        elif not (keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d] or keys[pygame.K_w]):
            state = 'idle'
        # W = Jump
        if keys[pygame.K_w] and ground == True:
            state = 'jumping'
            player_speed = -8
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
            player_speed = 0

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
            #if x_collision is False:
            #  return new_player_x
        return [new_player_x, fall]
    else:
        return [player_x, [player_y,player_speed,ground]]

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

def animate():
    global state,current_image,current_index,deb,frameNum

    if state == 'idle':
        deb += 1
        # Every 5 frames, update the animation to the next frame
        if deb == 5:
            playAnim(idle_anim)
        elif deb > 15:
            deb = 0
    elif state == 'run':
        deb += 1
        # Every 2 frames, update the animation to the next frame
        if deb == 2:
            playAnim(run_anim)
        elif deb > 15:
            deb = 0
    elif state == 'jumping':
        deb += 1
        # Every 2 frames, update the animation to the next frame
        if deb == 2:
            playAnim(jump_anim)
        elif deb > 15:
            deb = 0
    elif state == 'jumping-left':
        deb += 1
        # Every 2 frames, update the animation to the next frame
        if deb == 2:
            playAnim(cornerJump_anim)
        elif deb > 15:
            deb = 0
    elif state == 'jumping-right':
        deb += 1
        # Every 2 frames, update the animation to the next frame
        if deb == 2:
            playAnim(cornerJump_anim)
        elif deb > 15:
            deb = 0
    elif state == 'falling':
        deb += 1
        # Every 5 frames, update the animation to the next frame
        if deb == 5:
            playAnim(fall_anim)
        elif deb > 15:
            deb = 0
    elif state == 'crouching':
        deb += 1
        # Every 5 frames, update the animation to the next frame
        if deb == 5:
            playAnim(crouch_anim)
        elif deb > 15:
            deb = 0
    elif state == 'crouching':
        frameNum += 1
        if frameNum < 150:
            deb += 1
            if deb == 25:
                playAnim(crouch_anim)
            elif deb > 25:
                deb = 0
    elif state == 'died':
        current_image = idle_anim[0]
        frameNum += 1
        if frameNum < 150:
            deb += 1
            # Every 5 frames, update the animation to the next frame
            if deb == 25:
                playAnim(death_anim)
            elif deb > 25:
                deb = 0
    elif state == 'won':
        current_image = win_anim[0]
        frameNum += 1
        if frameNum < 25*len(win_anim):
            deb += 1
            # Every 5 frames, update the animation to the next frame
            if deb == 25:
                playAnim(win_anim)
            elif deb > 25:
                deb = 0

    