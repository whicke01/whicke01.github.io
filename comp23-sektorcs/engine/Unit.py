# Ryan Schumacher
# Unit.py
#
# A unit is the sprite played by the user or the sprites opposing the user

import pygame, os, sys
from pygame.locals import *

class Unit(pygame.sprite.Sprite):
    '''A sprite that moves and fires a weapon'''

    def load_image(self, image_path):
        ''' Loads the sprite from the designated path'''
        try:
            image = pygame.image.load(image_path)
        except pygame.error, message:
            print "Error loading image: " + image_path
            raise SystemExit, message
        return image.convert_alpha()

    def __init__(self, hpMax, hpCur, staminaMax, staminaCur, weapons, armor
                 image, onHit, onDeath, initX, initY, canvas):
        self.hpMax = hpMax
        self.hpCur = hpCur
        self.staminaMax = staminaMax
        self.staminaCur = staminaCur

        # Some units have multiple weapons
        self.weapons    = weapons
        self.currWeap   = weapons[0]

        self.armorClass = armor # armorClass = an integer that dampens damage

        self.x = init_x
        self.y = init_y

        self.image =   self.load_image(image)
        self.image_w = self.image.get_width()
        self.image_h = self.image.get_height()
        self.onHitImage   = onHit   # Path to image of sprite getting hit
        self.onDeathImage = onDeath # Path to image of sprite dying

        self.rect = self.image.get_rect()
        self.rect.x = init_y
        self.rect.y = init_y

        self.screen = canvas
        self.active = True

    def update(self):
        '''Updates the sprite's position and active status'''
        self.x += self.dx
        self.y += self.dy

        self.rect.x += self.dx
        self.rect.y += self.dy

        # TODO: Test for moving into another sector
        # TODO: Test for computer units not moving off screen
        # TODO: Regenerate stamina function (only relevant for hero unit)

    def draw(self):
        self.screen.blit(self.image, 
                         self.image.get_rect().move(self.x - self.image_w / 2, 
                                                    self.y - self.image_h / 2))

    def checkDeath(self):
        # TODO: Should this be done on a separate thread?
        if hpCur <= 0:
            # TODO: Load the death image for ~ 0.5 seconds
            self.active = False
            # Kill the sprite

    def fireWeapon(self):
        #TODO: Have the weapon class call its fire routine passing in the
        # appropriate data

        #
        yolo = "Swag"

    # Get/set routines for public members

    def getHpMax(self):
        return self.hpMax

    def setHpMax(self, newhpMax):
        self.hpMax = newhpMax;

    def getHpCur(self):
        return self.hpCur

    def setHpCur(self, newHpCur):
        self.hpCur = newHpCur

    def getStaminaMax(self):
        return self.staminaMax

    def setStaminaMax(self, newStamMax):
        self.staminaMax = newStamMax

    def getStaminaCur(self):
        return self.staminaCur

    def setStaminacur(self, newStaminaCur):
        self.StaminaCur = newStaminaCur

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

    def getWeapons(self):
        return self.weapons

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
