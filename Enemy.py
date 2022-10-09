import pygame
from pygame.locals import *
import random
import pygwidgets
from Constants import *

# Enemy class


class Enemy():
    ENEMY_IMAGE = pygame.image.load('images/enemy.png')

    def __init__(self, window):
        # we save the instance of the window to use in the draw method
        self.window = window
        self.windowWidth = WINDOW_WIDTH
        self.windowHeight = WINDOW_HEIGHT

        self.x = WINDOW_WIDTH / 2
        self.y = 0
        
        self.image = pygwidgets.Image(self.window, (self.x, self.y), Enemy.ENEMY_IMAGE)
        enemyRect = self.image.getRect()
        self.width = enemyRect.width
        self.height = enemyRect.height

        self.maxWidth = self.windowWidth - self.width
        self.maxHeight = self.windowHeight - self.height

        self.xSpeed = 3

    def update(self):
        if (self.x < 0) or (self.x >= self.maxWidth):
            self.xSpeed = -self.xSpeed
            self.y = self.y + self.height
        self.x = self.x + self.xSpeed
        self.image.setLoc((self.x, self.y))
        if self.y > self.windowHeight:
            return True
        else:
            return False

    def draw(self):
        #pygame.draw.rect(self.window, (255, 0, 0),(self.x, self.y, self.width, self.height), 0)
        self.image.draw()

    def collide(self, missileRect):
        collidedWithMissile = self.image.overlaps(missileRect)
        return collidedWithMissile

class EnemyMgr():
    ADD_NEW_ENEMY_RATE = 8

    def __init__(self, window):
        self.window = window
        self.enemyList = []
        self.nFramesTilNextEnemy = EnemyMgr.ADD_NEW_ENEMY_RATE
    
    def update(self):
        enemyListCopy = self.enemyList.copy()
        for oEnemy in enemyListCopy:
            deleteMe = oEnemy.update()
            if deleteMe:
                self.enemyList.remove(oEnemy)
    
        self.nFramesTilNextEnemy = self.nFramesTilNextEnemy - 1
        if self.nFramesTilNextEnemy == 0:
            oEnemy = Enemy(self.window)
            self.enemyList.append(oEnemy)
            self.nFramesTilNextEnemy = EnemyMgr.ADD_NEW_ENEMY_RATE
    
    def draw(self):
        for oEnemy in self.enemyList:
            oEnemy.draw()
    
    def hasEnemyHitMissile(self, missileRect):
        for oEnemy in self.enemyList:
            if oEnemy.collide(missileRect):
                return True
        return False