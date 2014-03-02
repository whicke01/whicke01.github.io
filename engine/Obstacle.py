# Ryan Schumacher
# Obstacle.py
#
# Any inanimate, immobile object is classified as an object in Sektor CS

import pygame, os, sys
from Laser import Laser
from pygame.locals import *
from random import randint

class Obstacle(pygame.sprite.Sprite):
    ''' An inanimate object that may deal damage when touched by a unit'''

    def load_image(self, image_path):
        ''' Loads the sprite from the designated path'''
        try:
            image = pygame.image.load(image_path)
        except pygame.error, message:
            print "Error loading image: " + image_path
            raise SystemExit, message
        return image.convert_alpha()

    def __init__(self, hpMax, armor, touchDamage, imagePath, onHit, onDeath, 
                 init_x, init_y, maxHP, armor, canvas):
        ''' Creates an obstacle at coordinates x y with the given canvas'''
        pygame.sprite.Sprite.__init__(self)

        self.hpMax = hpMax
        self.hpCur = hpMax
        self.armorClass  = armor #armorClass = an integer that dampens damage
        self.touchDamage = touchDamage # Damage dealt for touching this object

        self.x = init_x
        self.y = init_y

        self.image   = self.load_image(imagePath)
        self.image_w = self.image.get_width()
        self.image_h = self.image.get_height()
        self.onHitImage   = onHit   # Path to image of sprite getting hit
        self.onDeathImage = onDeath # Path to image of sprite dying 

        self.rect = self.image.get_rect()
        self.rect.x = init_y
        self.rect.y = init_y

        self.screen = canvas
        self.active = True

        self.dx = 0
        self.dy = 0

    def update(self):
        '''Updates the sprite's position and active status'''

    def draw(self):
        self.screen.blit(self.image, 
                         self.image.get_rect().move(self.x - self.image_w / 2, 
                         self.y - self.image_h / 2))

    def checkDeath (self):
        if self.hpCur <= 0:
            # TODO: Kill the sprite and play animation
            self.active = False;


    def getHpMax(self):
        return self.hpMax

    def setHpMax(self, newhpMax):
        self.hpMax = newhpMax;

    def getHpCur(self):
        return self.hpCur

    def setHpCur(self, newHpCur):
        self.hpCur = newHpCur

    def getX(self):
        return self.x

    def setX(self, newX):
        self.x = newX

    def getY(self):
        return self.y

    def setY(self, newY):
        self.y = newY

    def getDX(self):
        return self.dx

    def setDX(self, newDX):
        self.dx = newDX

    def getDY(self):
        return self.dy

    def setDY(self, newDY):
        self.dy = newDY

    def setImage(self, newImgPath):
        self.image = self.load_image(newImgPath)
        self.image_w = self.image.get_width()
        self.image_h = self.image.get_height()

    def getRect(self):
        return self.rect

    def getScreen(self):
        return self.screen

    def setScreen(self, newScreen):
        self.screen = newScreen

    def getActive(self):
        return self.active

    def setActive(self, newActive):
        self.active = newActive
