from pickle import TRUE
import pygame

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

def makePlatform(screen,arr, color):
    for p in arr:
        pygame.draw.rect(screen,color,p)