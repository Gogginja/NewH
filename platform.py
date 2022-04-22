from pickle import TRUE
import pygame

#test
level1 = [
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

level2 = [
    pygame.Rect(0, 200, 100, 400),
    pygame.Rect(100, 200, 75, 25),
    pygame.Rect(300, 100, 120, 20),
    pygame.Rect(300, 175, 120, 20),
    pygame.Rect(300, 250, 120, 20),
    pygame.Rect(470, 125, 120, 20),
    pygame.Rect(470, 200, 120, 20),
    pygame.Rect(180, 400, 480, 20),
    pygame.Rect(400, 350, 50, 50),
    pygame.Rect(500, 300, 50, 100),
    pygame.Rect(600, 350, 50, 50)
]
locked2 = True

level3 = [
    pygame.Rect(0, 250, 75, 25),
    pygame.Rect(100, 250, 100, 25),
    pygame.Rect(188, 262, 25, 25),
    pygame.Rect(200, 275, 25, 25),
    pygame.Rect(212, 287, 25, 25),
    pygame.Rect(225, 300, 25, 25),
    pygame.Rect(237, 312, 25, 25),
    pygame.Rect(250, 325, 25, 25),
    pygame.Rect(262, 337, 25, 25),
    pygame.Rect(275, 350, 25, 25),
    pygame.Rect(300, 250, 200, 25),
    pygame.Rect(300, 350, 200, 25),
    pygame.Rect(600, 50, 100, 200),
    pygame.Rect(550, 300, 25, 75),
    pygame.Rect(510, 220, 20, 50),
    pygame.Rect(550, 160, 15, 50),
    pygame.Rect(570, 110, 10, 50),
    pygame.Rect(200, 100, 120, 25),
    pygame.Rect(400, 50, 120, 25),
    pygame.Rect(50, 200, 25, 50),
    pygame.Rect(100, 175, 50, 25)
]
locked3 = True

level4 = [
            pygame.Rect(0, 250, 75, 25)
         ]

slopes = [
            #pygame.polygon((200,200),(200,250),(300,200),(300,150))
         ]


def makePlatform(screen,arr, color):
    #Test for an upward incline using polygons
    #pygame.draw.polygon(screen,color,slopes)
    for p in arr:
        pygame.draw.rect(screen,color,p)
        
'''
levelTest = [
    [0, 450, 50, 50],
    [100, 450, 50, 50],
    [200, 450, 50, 50],
    [350, 450, 50, 50],
    [400, 400, 50, 50],
    [450, 350, 50, 50],
    [500, 300, 50, 50],
    [550, 250, 50, 50],
    [600, 200, 50, 50],
    [450, 200, 50, 50],
    [250, 300, 100, 25],
    [300, 150, 100, 25],
    [300, 100, 25, 50]
]

def level1Test(screen,color, offset):
    #Test for an upward incline using polygons
    #pygame.draw.polygon(screen,color,slopes)
        pygame.draw.rect(screen,color,pygame.Rect(levelTest[0][0]-offset, levelTest[0][1], levelTest[0][2], levelTest[0][3]))
        pygame.draw.rect(screen,color,pygame.Rect(levelTest[1][0]-offset, levelTest[1][1], levelTest[1][2], levelTest[1][3]))
        pygame.draw.rect(screen,color,pygame.Rect(levelTest[2][0]-offset, levelTest[2][1], levelTest[2][2], levelTest[2][3]))
        pygame.draw.rect(screen,color,pygame.Rect(levelTest[3][0]-offset, levelTest[3][1], levelTest[3][2], levelTest[3][3]))
        pygame.draw.rect(screen,color,pygame.Rect(levelTest[4][0]-offset, levelTest[4][1], levelTest[4][2], levelTest[4][3]))
        pygame.draw.rect(screen,color,pygame.Rect(levelTest[5][0]-offset, levelTest[5][1], levelTest[5][2], levelTest[5][3]))
        pygame.draw.rect(screen,color,pygame.Rect(levelTest[6][0]-offset, levelTest[6][1], levelTest[6][2], levelTest[6][3]))
        pygame.draw.rect(screen,color,pygame.Rect(levelTest[7][0]-offset, levelTest[7][1], levelTest[7][2], levelTest[7][3]))
        pygame.draw.rect(screen,color,pygame.Rect(levelTest[8][0]-offset, levelTest[8][1], levelTest[8][2], levelTest[8][3]))
        pygame.draw.rect(screen,color,pygame.Rect(levelTest[9][0]-offset, levelTest[9][1], levelTest[9][2], levelTest[9][3]))
        pygame.draw.rect(screen,color,pygame.Rect(levelTest[10][0]-offset, levelTest[10][1], levelTest[10][2], levelTest[10][3]))
        pygame.draw.rect(screen,color,pygame.Rect(levelTest[11][0]-offset, levelTest[11][1], levelTest[11][2], levelTest[11][3]))
        pygame.draw.rect(screen,color,pygame.Rect(levelTest[12][0]-offset, levelTest[12][1], levelTest[12][2], levelTest[12][3]))
'''