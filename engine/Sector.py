# Sektor CS
# Sector.py
#
# A sector is what is displayed on the screen at any given time. A sector
# contains enemies, obstacles, and paths to other sectors. They are the
# building blocks of the world.

import pygame, os, sys
from pygame.locals import *

class Sector():
    def __init__(self, mainChar, name, neighbors, spawnX, spawnY):
        # A sector's name MUST be unique for populating it
        self.name = name
        self.hero = mainChar
        self.unitGroup = pygame.sprite.Group()
        self.obstGroup = pygame.sprite.Group()
        self.respawnX  = x
        self.respawnY  = y
    
