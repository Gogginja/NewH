# Link for Sprite:https://rvros.itch.io/animated-pixel-hero

# Star Sprite bs galangpiliang
# Link:https://opengameart.org/content/star-vector

from pickle import TRUE
import pygame
import platform
import player


#==[ Global Variables ]==#
#Screen Creation
SCREEN_SIZE =       (700, 500) #700x500
backgroundColor =   (50, 50, 50) #Dark Grey
platformColor =     (16, 173, 42) #Green
goalColor =         (237, 12, 12) #Red
#Pygame
clock =             None
screen =            None
font =              None
user =              None
game_state =        False
#Game Settings
score =             0

coin_image = pygame.image.load('Image/coin11.png')
coin = [
    pygame.Rect(600, 150, 22, 22),
    pygame.Rect(200, 250, 22, 22)
    ]
goal = pygame.Rect(350, 0, 10, 30)

def drawtext(t, x, y):
    text = font.render(t, TRUE, platformColor, backgroundColor)
    text_rectangle = text.get_rect()
    text_rectangle.topleft = (x, y)
    screen.blit(text, text_rectangle)

def getState():
    return game_state

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('StarDust')
clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(), 24)
game_state = 'playing'

# RUN GAME
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
        new_player_x = player.player_x
        new_player_y = player.player_y
        player.movement()

    # ------
    # update
    # s------
    # horizontal movement
    if game_state == 'playing':
        new_player_rect = pygame.Rect(new_player_x, player_y,
                                      player_width, player_height)
        x_collision = False
        # ..check against every playform
        for p in platform.platforms:
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
        for p in platform.platforms:
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
    screen.fill(backgroundColor)
    if game_state == 'playing':
        # plaforms
        for p in platform.platforms:
            pygame.draw.rect(screen, platformColor, p)

        # coins
        for c in coin:
            screen.blit(coin_image, (c[0], c[1]))

        # player
        screen.blit(player_image, (player_x, player_y))

        # End Goal
        pygame.draw.rect(screen, goalColor, goal)

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