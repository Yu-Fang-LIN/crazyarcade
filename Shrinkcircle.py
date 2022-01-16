import pygame
import random
from pygame.locals import *

def shrink_circle(radius, center, screen, timer):
    pygame.draw.circle(screen, (255, 0, 0), center, radius, 1)
    if timer < 1000:
        pass
    elif timer < 2000:
        pygame.draw.circle(screen, (0, 255, 0), center, 500, 1)
    elif timer < 3000:
        pygame.draw.circle(screen, (0, 255, 0), center, 350, 1)
    elif timer < 4000:
        pygame.draw.circle(screen, (0, 255, 0), center, 300, 1)
    elif timer < 5000:
        pygame.draw.circle(screen, (0, 255, 0), center, 250, 1)
    elif timer < 6000:
        pygame.draw.circle(screen, (0, 255, 0), center, 200, 1)
    # elif timer < 7000:
    #     pygame.draw.circle(screen, (0, 255, 0), center, 150, 1)
    # elif timer < 8000:
    #     pygame.draw.circle(screen, (0, 255, 0), center, 100, 1)
    # elif timer < 9000:
    #     pygame.draw.circle(screen, (0, 255, 0), center, 50, 1)

def change_radius(radius, timer):
    if timer < 1000:
        radius = 1000
    elif timer < 2000:
        radius = 700
    elif timer < 3000:
        radius = 500
    elif timer < 4000:
        radius = 350
    elif timer < 5000:
        radius = 300
    elif timer < 6000:
        radius = 250
    else:
        radius = 200
    # elif timer < 7000:
    #     radius = 200
    # elif timer < 8000:
    #     radius = 150
    # elif timer < 9000:
    #     radius = 100
    # else:
    #     radius = 50
    return radius

def eliminate(player1, player2, radius, center):
    if (player1.rect.center[0]-center[0])**2+(player1.rect.center[1] - center[1])**2 > radius**2:
        player1.kill()
    if (player2.rect.center[0]-center[0])**2+(player2.rect.center[1] - center[1])**2 > radius**2:
        player2.kill()
