from math import *
from random import *
import constants as cnst
from ship import *
from bullet import*
import numpy as np
import pygame


def game(field_type1):
    cnst.screen = pygame.display.set_mode((cnst.WIDTH, cnst.HEIGHT))
    clock = pygame.time.Clock()
    finished = False

    ship1 = Ship([WIDTH / 2, 750], SHIPIMG, SHIPSTR)

    
bullets = []
rockets = []

   while not finished:
    ship1.changespd()
    bounce1(ship1)
    for b in bullets:
        b.movebullet(SCALE)
    for k in rockets:
        k.moverocket(SCALE)
    ship1.move(SCALE)
    ship1.shoot(bullets)

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == ship1.get_steer().rocket:
                ship1.rocket(rockets)
    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()
