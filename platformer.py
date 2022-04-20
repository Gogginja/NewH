# Link for Sprite:https://rvros.itch.io/animated-pixel-hero

# Star Sprite bs galangpiliang
# Link:https://opengameart.org/content/star-vector

from pickle import TRUE
import pygame

#main.py
def drawtext(t, x, y):
    text = font.render(t, TRUE, GREEN, DARK_GREY)
    text_rectangle = text.get_rect()
    text_rectangle.topleft = (x, y)
    screen.blit(text, text_rectangle)


# Constant variables - main.py
SCREEN_SIZE = (700, 500)
DARK_GREY = (50, 50, 50)
GREEN = (16, 173, 42)
RED = (237, 12, 12)

# init - main.py
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('StarDust')
clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(), 24)
# game states = playing // winning // losing
game_state = 'playing'


def getState():
    return game_state


# end goal - COIN.py
goal = pygame.Rect(350, 0, 10, 30)

# player - PLAYER.py
player_image = pygame.image.load('Sprites/idle/adventurer-idle-02.png')
player_x = 0
player_y = 0
player_speed = 0
player_acceleration = 0.2
player_width = 19
player_height = 30


def getX():
    return player_x


def getY():
    return player_y


# platforms - PLATFORM.py
platforms = [

    pygame.Rect(0, 450, 50, 50),
    pygame.Rect(100, 450, 50, 50),
    pygame.Rect(200, 450, 50, 50),
    pygame.Rect(350, 450, 50, 50),
    pygame.Rect(400, 400, 50, 50),
    pygame.Rect(450, 350, 50, 50),
    pygame.Rect(500, 300, 50, 50),
    pygame.Rect(550, 250, 50, 50),
    pygame.Rect(600, 200, 50, 50),
    pygame.Rect(450, 200, 50, 50),
    pygame.Rect(250, 300, 100, 25),
    pygame.Rect(300, 150, 100, 25),
    pygame.Rect(300, 100, 25, 50)
]
# Coins - COIN.py
coin_image = pygame.image.load('Image/coin11.png')
coin = [
    pygame.Rect(600, 150, 22, 22),
    pygame.Rect(200, 250, 22, 22)
    ]

# main.py
score = 0

def getScore():
    return score

# game loop - SCREEN.py
running = True
while running:
    # ------
    # Input
    # ------

    # checking for quit - SCREEN.py
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if game_state == 'playing':
        new_player_x = player_x
        new_player_y = player_y

        # player input
        keys = pygame.key.get_pressed()
        # a=left
        if keys[pygame.K_a]:
            new_player_x -= 2
        # d=right
        if keys[pygame.K_d]:
            new_player_x += 2
        # w=jump (if on the ground)
        if keys[pygame.K_w] and player_on_ground:
            player_speed = -5

    # ------
    # update
    # s------
    # horizontal movement
    if game_state == 'playing':
        new_player_rect = pygame.Rect(new_player_x, player_y,
                                      player_width, player_height)
        x_collision = False
        # ..check against every playform
        for p in platforms:
            if p.colliderect(new_player_rect):
                x_collision = TRUE
                break

        if x_collision is False:
            player_x = new_player_x

        # vertical movement

        player_speed += player_acceleration
        new_player_y += player_speed

        new_player_rect = pygame.Rect(player_x, new_player_y,
                                      player_width, player_height)
        y_collision = False
        player_on_ground = False
        # ..check against every playform
        for p in platforms:
            if p.colliderect(new_player_rect):
                y_collision = TRUE
                player_speed = 0
                # if the platform is below the player
                if p[1] > new_player_y:
                    # stick player to platform
                    player_y = p[1] - player_height
                    player_on_ground = True
                break

        if y_collision is False:
            player_y = new_player_y
        # see if any coins have been collected
        if player_y >= 500:
            game_state = 'lose'
        player_rect = pygame.Rect(player_x, player_y,
                                  player_width, player_height)
        for c in coin:
            if c.colliderect(player_rect):
                coin.remove(c)
                score += 1
        # check endgame
        goal_collision = False
        if goal_collision is False:
            player_rect = pygame.Rect(player_x, player_y,
                                      player_width, player_height)

            if goal.colliderect(player_rect):
                game_state = 'win'

    # -----
    # Draw
    # -----

    # background
    screen.fill(DARK_GREY)
    if game_state == 'playing':
        # plaforms
        for p in platforms:
            pygame.draw.rect(screen, GREEN, p)

        # coins
        for c in coin:
            screen.blit(coin_image, (c[0], c[1]))

        # player
        screen.blit(player_image, (player_x, player_y))

        # End Goal
        pygame.draw.rect(screen, RED, goal)

        drawtext('Score: ' + str(score), 10, 10)

    if game_state == 'win':
        # draw win text
        drawtext('You Win!', 10, 10)

    if game_state == 'lose':
        # draw lose text
        drawtext('You Lose!', 10, 10)

    pygame.display.flip()
    clock.tick(60)
# quit
pygame.quit()
