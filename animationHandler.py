import pygame
import player

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

def playAnim(animList):
        if player.current_index > len(animList)-1:
            player.current_index = 0
        player.current_index += 1
        if player.current_index == len(animList):
            player.current_index = 0
        if player.direction:
            player.current_image = animList[player.current_index]
        else:
            imgCopy = animList[player.current_index].copy()
            player.current_image = pygame.transform.flip(imgCopy, True, False)

def animate():
    if player.state == 'idle':
        player.deb += 1
        # Every 5 frames, update the animation to the next frame
        if player.deb == 5:
            playAnim(idle_anim)
        elif player.deb > 15:
            player.deb = 0
    elif player.state == 'run':
        player.deb += 1
        # Every 2 frames, update the animation to the next frame
        if player.deb == 2:
            playAnim(run_anim)
        elif player.deb > 15:
            player.deb = 0
    elif player.state == 'jumping':
        player.deb += 1
        # Every 2 frames, update the animation to the next frame
        if player.deb == 2:
            playAnim(jump_anim)
        elif player.deb > 15:
            player.deb = 0
    elif player.state == 'jumping-left':
        player.deb += 1
        # Every 2 frames, update the animation to the next frame
        if player.deb == 2:
            playAnim(cornerJump_anim)
        elif player.deb > 15:
            player.deb = 0
    elif player.state == 'jumping-right':
        player.deb += 1
        # Every 2 frames, update the animation to the next frame
        if player.deb == 2:
            playAnim(cornerJump_anim)
        elif player.deb > 15:
            player.deb = 0
    elif player.state == 'falling':
        player.deb += 1
        # Every 5 frames, update the animation to the next frame
        if player.deb == 5:
            playAnim(fall_anim)
        elif player.deb > 15:
            player.deb = 0
    elif player.state == 'crouching':
        player.deb += 1
        # Every 5 frames, update the animation to the next frame
        if player.deb == 5:
            playAnim(crouch_anim)
        elif player.deb > 15:
            player.deb = 0
    elif player.state == 'crouching':
        player.frameNum += 1
        if player.frameNum < 150:
            player.deb += 1
            if player.deb == 25:
                playAnim(crouch_anim)
            elif player.deb > 25:
                player.deb = 0
    elif player.state == 'died':
        player.frameNum += 1
        if player.frameNum < 150:
            player.deb += 1
            # Every 5 frames, update the animation to the next frame
            if player.deb == 25:
                playAnim(death_anim)
            elif player.deb > 25:
                player.deb = 0
    elif player.state == 'won':
        player.frameNum += 1
        if player.frameNum < 250:
            player.deb += 1
            # Every 5 frames, update the animation to the next frame
            if player.deb == 5:
                playAnim(win_anim)
            elif player.deb > 5:
                player.deb = 0