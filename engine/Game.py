# Ryan Schumacher
# Game.py
#
# The main game loop 

import pygame, os, sys
from Hero import Hero #, Obstacle, Projectile, Sector, Unit, Weapon
from pygame.locals import *
from random import randint

# Runtime parameters
FPS = 50
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)

# Pygame Initialization
pygame.init()
pygame.display.set_caption('Sektor CS')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
clock = pygame.time.Clock()

# Make the hero unit
hero = Hero(screen)

# Game loop
while True:
    time_elapsed = clock.tick(FPS)

    # TODO: Change control scheme
    # TODO: Implement joystick controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == K_DOWN:
                    hero.setDY(1)
            elif event.key == K_LEFT:
                    hero.setDX(-1)
            elif event.key == K_RIGHT:
                    hero.setDX(1)
            elif event.key == K_UP:
                    hero.setDY(-1)
            elif event.key == K_SPACE:
                    hero.fireLaser()
        elif event.type == KEYUP:
            if event.key == K_DOWN:
                hero.setDY(0)
            elif event.key == K_LEFT:
                hero.setDX(0)
            elif event.key == K_RIGHT:
                hero.setDX(0)
            elif event.key == K_UP:
                hero.setDY(0)

    # Draw background, update sprites, redraw sprites
    screen.fill(BACKGROUND_COLOR)

    hero.update()
    hero.draw()

    # TODO: Update and draw everything in the sector....

    pygame.display.update()
