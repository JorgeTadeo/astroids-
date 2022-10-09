import pygame
from pygame.locals import *
from Missile import *
# Player class


class Player():

    def __init__(self, window, windowWidth, windowHeight):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.missileList = []
        self.missileMgr = MissileMgr(self.window)

        # pygame.draw.polygon(window, (0, 255, 0), [[25, 25], [0, 50], [50, 50]], 2)
        # building our triangle
        halfWindowWidth = self.windowWidth / 2
        p1 = ((halfWindowWidth - 25) + (halfWindowWidth + 25)) / 2
        #print(p1, windowHeight - 50)
        self.topPoint = [p1, windowHeight - 50]
        self.leftPoint = [halfWindowWidth - 25, windowHeight - 25]
        #print(halfWindowWidth - 25, windowHeight - 25)
        self.rightPoint = [halfWindowWidth + 25, windowHeight - 25]
        #print(halfWindowWidth + 25, windowHeight - 25)

    def move_left(self):
        if self.leftPoint[0] > 10:
            #print(self.topPoint[0], self.topPoint[1])
            self.topPoint[0] -= 10
            self.rightPoint[0] -= 10
            self.leftPoint[0] -= 10
        else:
            return

    def move_right(self):
        if self.rightPoint[0] + 10 < self.windowWidth:
            self.topPoint[0] += 10
            self.rightPoint[0] += 10
            self.leftPoint[0] += 10
        else:
            return

    def fire(self):
        if self.missileMgr.missiles() > 2:
            return
        else:
            print(self.topPoint[0], self.topPoint[1])
            self.missileMgr.addMissile(self.topPoint[0], self.topPoint[1])

    def update(self):
            self.missileMgr.update()

    def draw(self):
        pygame.draw.polygon(self.window, (0, 255, 0), [
                            self.topPoint, self.leftPoint, self.rightPoint], 0)
        self.missileMgr.draw()
