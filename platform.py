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

level1 = [pygame.Rect(0, 450, 700, 50)]

level2 = [
            pygame.Rect(0, 450, 700, 50),
            pygame.Rect(0, 200, 100, 400),
            pygame.Rect(100, 200, 75, 25),
            pygame.Rect(300, 100, 120, 20),
            pygame.Rect(300, 175, 120, 20),
            pygame.Rect(300, 250, 120, 20),
            pygame.Rect(500, 100, 120, 20),
            pygame.Rect(500, 175, 120, 20),
            pygame.Rect(150, 350, 100, 100),
            pygame.Rect(450, 300, 100, 200),
            pygame.Rect(550, 375, 120, 10)
         ]
level3 = [
            pygame.Rect(0, 450, 700, 50)
         ]
slopes = [(200,200),(200,250),(300,200),(300,150)]


def makePlatform(screen,arr, color):
    #Test for an upward incline using polygons
    #pygame.draw.polygon(screen,color,slopes)
    for p in arr:
        pygame.draw.rect(screen,color,p)
