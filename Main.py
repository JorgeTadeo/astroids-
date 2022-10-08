# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random
from Enemy import *
from Player import *
from Missile import *

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 Load assets: image(s), sound(s), etc.

# 5 - Initialize variables
oEnemy3 = Enemy(window, WINDOW_WIDTH, WINDOW_HEIGHT, 50, 50)
oPlayer = Player(window, WINDOW_WIDTH, WINDOW_HEIGHT)

# 6 - Loop forever
while True:
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                oPlayer.fire()
        keys = pygame.key.get_pressed()
        if keys[K_a]:
            oPlayer.move_left()
        elif keys[K_d]:
            oPlayer.move_right()

    # 8 - Do any "per frame" actio ns
    # oEnemy1.update()
    # oEnemy2.update()
    oEnemy3.update()
    oPlayer.update()

    # 9 - Clear the window before drawing it gain
    window.fill(BLACK)

    # 10 - Draw the window elements
    # oEnemy1.draw()  # tell the Ball to draw itself
    # oEnemy2.draw()
    oEnemy3.draw()
    oPlayer.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
