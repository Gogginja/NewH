import pygame
import player

# COIN DATA FOR EACH LEVEL
coin_image = pygame.image.load('Image/textures/star.png')
coin1 = [
    pygame.Rect(600, 150, 22, 22),
    pygame.Rect(200, 250, 22, 22)
]
coin2 = [
    pygame.Rect(550, 150, 22, 22),
    pygame.Rect(200, 350, 22, 22)
]
coin3 = [
    pygame.Rect(450, 300, 22, 22),
    pygame.Rect(200, 50, 22, 22)
]

# COIN RESET DATA FOR EACH LEVEL
copy1 = [
    pygame.Rect(600, 150, 22, 22),
    pygame.Rect(200, 250, 22, 22)
    ]
copy2 = [
    pygame.Rect(600, 150, 22, 22),
    pygame.Rect(200, 250, 22, 22)
]
copy3 = [
    pygame.Rect(450, 300, 22, 22),
    pygame.Rect(200, 50, 22, 22)
]

# Color of the end goal
RED = (237, 12, 12)

# End goal Data
goal1 = [
    pygame.Rect(350, 0, 10, 30)
    ]
goal2 = [
    pygame.Rect(350, 0, 10, 30)
    ]
goal3 = [
    pygame.Rect(650, 0, 10, 30)
    ]

# Score/Number of coins collected
score = 0

# Collect coin
def collect(x, y, coin):
    player_x = x
    player_y = y
    player_rect = pygame.Rect(player_x, player_y,
                            player.player_width, player.player_height)
    # If coin list is not empty:
    if coin != []:
        # For every coin in the list
        for c in coin:
            # If player collides with it:
            if c.colliderect(player_rect):
                # Remove coin
                coin.remove(c)
                return 1
            else:
                return 0
    # If coin list is empty
    else:
        return 0

# Touch the end goal
def end(x, y, goal):
    player_x = x
    player_y = y
    player_rect = pygame.Rect(player_x, player_y,
                              player.player_width, player.player_height)
    # For every goal in list:
    for g in goal:
        # If player collides with it:
        if g.colliderect(player_rect):
            player.canMove = False
            player.state = 'won'
            return True
        else:
            return False
    else:
        return False