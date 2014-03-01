# Ryan Schumacher
# Projectile.py
#
# An object that moves. All projectiles are fired from the Unit class.

import pygame, os, sys
from Laser import Laser
from pygame.locals import *
from random import randint

class Projectile(pygame.sprite.Sprite):
    ''' A flying sprite '''

    def load_image(self, image_path):
        ''' Loads the sprite from the designated path'''
        try:
            image = pygame.image.load(image_path)
        except pygame.error, message:
            print "Error loading image: " + image_path
            raise SystemExit, message
        return image.convert_alpha()

    def __init__(self, image, onCollide, damage, initDX, initDY, canvas)
        ''' Creates an obstacle at coordinates x y with the given canvas'''
        pygame.sprite.Sprite.__init__(self)

        self.image   = self.load_image(imagePath)
        self.image_w = self.image.get_width()
        self.image_h = self.image.get_height()

        self.rect   = self.image.get_rect()
        self.rect.x = init_y
        self.rect.y = init_y

        self.onCollideImage   = onCollide   # Path to collision image
        self.damageScore = damage

        self.dx = initDX
        self.dy = initDY

        self.screen = canvas
        self.active = True

    def update(self):
        '''Updates the sprite's position and active status'''
        self.x += self.dx
        self.y += self.dy

        self.rect.x += self.dx
        self.rect.y += self.dy

        # TODO: Test for moving off screen

    def draw(self):
        self.screen.blit(self.image, 
                         self.image.get_rect().move(self.x - self.image_w / 2, 
                         self.y - self.image_h / 2))

    def getDamageScore(self):
        return self.damageScore

    def setDamageScore(self, newDamageScore):
        self.damageScore = newDamageScore

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
