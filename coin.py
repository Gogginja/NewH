import pygame

coin_image = pygame.image.load('Image/coin11.png')
coin = [
    pygame.Rect(600, 150, 22, 22),
    pygame.Rect(200, 250, 22, 22)
    ]

goal = pygame.Rect(350, 0, 10, 30)

def makeCoin():
    for c in coin:
        screen.blit(coin_image, (c[0], c[1]))