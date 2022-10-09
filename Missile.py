import pygame
from pygame.locals import *


class Missile():
    def __init__(self, window, xLoc, yLoc):
        self.window = window
        self.outOfRange = False
        # the location of the top of the ship should be where the missle is fired from
        self.x = xLoc
        self.y = yLoc
        # the width and height of the missile
        self.height = 10
        self.width = 10
        self.missile = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        if self.y > 0:
            self.y = self.y - 10
            self.missile = pygame.Rect(self.x, self.y, self.width, self.height)
        return self.location()

    def location(self):
        if self.y == 0:
            self.outOfRange = True
            return self.outOfRange
        else:
            return self.outOfRange

    def draw(self):
        pygame.draw.rect(self.window, (0, 255, 0), self.missile, 0)
    
    def collide(self, enemyRect):
        collidedWithEnemy = self.missile.colliderect(enemyRect)
        return collidedWithEnemy

# MissileMgr class
class MissileMgr():

    def __init__(self, window):
        self.window = window
        self.missileList = []
    
    def missiles(self):
        return len(self.missileList)
    
    def update(self):
        missileListCopy = self.missileList.copy()
        for oMissile in missileListCopy:
            deleteMe = oMissile.update()
            if deleteMe:
                self.missileList.remove(oMissile)

    def draw(self):
        for oMissile in self.missileList:
            oMissile.draw()
    
    def hasMissileHitEnemy(self, enemyRect):
        for oMissile in self.missileList:
            if oMissile.collide(enemyRect):
                return True
        return False
    
    def addMissile(self, xLoc, yLoc):
        oMissile = Missile(self.window, xLoc, yLoc)
        self.missileList.append(oMissile)