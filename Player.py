import unittest
import pygame
from pygame.locals import *
from Missile import *
from Constants import *
# Player class


class Player():

    def __init__(self, window):
        self.window = window
        self.windowWidth = WINDOW_WIDTH
        self.windowHeight = WINDOW_HEIGHT
        self.missileMgr = MissileMgr(self.window)

        # pygame.draw.polygon(window, (0, 255, 0), [[25, 25], [0, 50], [50, 50]], 2)
        # building our triangle
        halfWindowWidth = self.windowWidth / 2
        p1 = ((halfWindowWidth - 25) + (halfWindowWidth + 25)) / 2
        self.topPoint = [p1, self.windowHeight - 50]
        self.leftPoint = [halfWindowWidth - 25, self.windowHeight - 25]
        self.rightPoint = [halfWindowWidth + 25, self.windowHeight - 25]

    def move_left(self):
        if self.leftPoint[0] > 10:
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
            self.missileMgr.addMissile(self.topPoint[0], self.topPoint[1])

    def update(self):
            self.missileMgr.update()

    def draw(self):
        pygame.draw.polygon(self.window, (0, 255, 0), [
                            self.topPoint, self.leftPoint, self.rightPoint], 0)
        self.missileMgr.draw()
#---------------------------------Unit Test Code-------------------------------------------------
class PlayerTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.oPlayer = Player(self.window)
    
    def test_player_has_fired_a_missile(self):
        self.oPlayer.fire()
        self.assertEqual(self.oPlayer.missileMgr.missiles(), 1)
    
    def test_player_cant_shoot_4_missiles(self):
        self.oPlayer.fire()
        self.oPlayer.fire()
        self.oPlayer.fire()
        self.oPlayer.fire()
        self.assertEqual(self.oPlayer.missileMgr.missiles(), 3)
    
    def test_player_has_moved_left(self):
        topPoint = self.oPlayer.topPoint[0]
        leftPoint = self.oPlayer.leftPoint[0]
        rightPoint = self.oPlayer.rightPoint[0]
        self.oPlayer.move_left()
        self.assertEqual(self.oPlayer.topPoint[0], topPoint - 10)
        self.assertEqual(self.oPlayer.leftPoint[0], leftPoint - 10)
        self.assertEqual(self.oPlayer.rightPoint[0], rightPoint - 10)

    def test_player_has_moved_right(self):
        topPoint = self.oPlayer.topPoint[0]
        leftPoint = self.oPlayer.leftPoint[0]
        rightPoint = self.oPlayer.rightPoint[0]
        self.oPlayer.move_right()
        self.assertEqual(self.oPlayer.topPoint[0], topPoint + 10)
        self.assertEqual(self.oPlayer.leftPoint[0], leftPoint + 10)
        self.assertEqual(self.oPlayer.rightPoint[0], rightPoint + 10)



if __name__ == '__main__':
    unittest.main()