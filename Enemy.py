import pygame
from pygame.locals import *
import random

# Enemy class


class Enemy():
    def __init__(self, window, windowWidth, windowHeight, enemyWidth, enemyHeight):
        # we save the instance of the window to use in the draw method
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        # A react is made up of [x,y, width, height]
        self.height = enemyHeight
        self.width = enemyWidth
        self.maxWidth = self.windowWidth - self.width
        self.maxHeight = self.windowHeight - self.height

        self.x = windowWidth / 2
        self.y = 0

        # Choose a random speed between -4 and 4, but not zero
        # in both the x and y directions
        speedList = [3]
        self.xSpeed = random.choice(speedList)
        self.yDrop = self.height

    def update(self):
        # check for hitting a wall. If so, change the direction.
        if (self.x < 0) or (self.x >= self.maxWidth):
            self.xSpeed = -self.xSpeed
            self.y = self.y + self.height
        # Update the Ball's x and y, using the speed in two directions
        self.x = self.x + self.xSpeed

    def draw(self):
        pygame.draw.rect(self.window, (255, 0, 0),
                         (self.x, self.y, self.width, self.height), 0)
