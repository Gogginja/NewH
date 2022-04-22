import pygame


class platforms:
    global level1, level2, locked2, level3, locked3
    # Level 1 Data
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

    # Level 2 Data
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

    # Level 3 Data
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


# Generate the platforms in each list
def makePlatform(screen, arr, color):
    for p in arr:
        pygame.draw.rect(screen, color, p)
