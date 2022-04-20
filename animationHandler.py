from asyncio.windows_events import NULL
import pygame

# DO NOT MESS WITH PLEASE <3

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

def animate(state,direction,current_index,deb):
    current_index = 0
    # True = right : False = left
    direction = True
    deb = 0

    def playAnim(animList):
        nonlocal state,direction,current_index,deb
        if current_index > len(animList)-1:
            current_index = 0
        current_index += 1
        if current_index == len(animList):
            current_index = 0
        if direction:
            return animList[current_index]
        else:
            imgCopy = animList[current_index].copy()
            return pygame.transform.flip(imgCopy, True, False)

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
