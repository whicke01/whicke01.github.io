# Ryan Schumacher
# Unit.py
#
# The main unit that is controlled by the player

import pygame, os, sys
from Unit import Unit
from pygame.locals import *

class Hero(Unit):
    def __init__(self):
        print "Sup dawg"

    def __init__(self, canvas):
        super(Hero, self).__init__(100, 100, 100, 100, ["Weapons"], 10,
                         "../assets/images/sprites/battlecruiser.gif", 
                         "../assets/images/sprites/battlecruiser.gif",
                         "../assets/images/sprites/battlecruiser.gif", 
                         canvas.get_width() / 2, 
                         canvas.get_height() / 2, canvas)
