import pygame
from pygame.locals import *


class Missile():
    def __init__(self, window, windowWidth, windowHeight, xLoc, yLoc):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.outOfRange = False

        # the location of the top of the ship should be where the missle is fired from
        self.x = xLoc
        self.y = yLoc

        # the width and height of the missle
        self.height = 10
        self.width = 10

    def update(self):
        if self.y > 0:
            self.y = self.y - 10

    def location(self):
        if self.y == 0:
            self.outOfRange = True
            return self.outOfRange
        else:
            return self.outOfRange

    def draw(self):
        pygame.draw.rect(self.window, (0, 255, 0),
                         (self.x, self.y, self.width, self.height), 0)
