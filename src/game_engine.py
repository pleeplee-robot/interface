#!/usr/bin/env python3.5

import pygame
import sys
import time

from pygame.locals import *
from button import *
from main import *
from light_beacon import *

screen_width = 1300
screen_height = 950
FPS = 40
fps_clock = pygame.time.Clock()

class GameEngine:

    # surface should be a surface of the size of 350x950
    def __init__(self, screen):
        self.balises = []
        self.balises_additionnals = []
        self.plants = []
        self.obstacles = []
        self.outfile_json = 'data_json'
        # lu_beacon1 = LightBeacon(screen,
        #                         '../assets/misc/light_beacon_red.png',
        #                         '../assets/misc/light_beacon_red.png',
        #                         (25, 25))
        # lu_beacon2 = LightBeacon(screen,
        #                         '../assets/misc/light_beacon_red.png',
        #                         '../assets/misc/light_beacon_red.png',
        #                         (25, 924))
        # lu_beacon3 = LightBeacon(screen,
        #                         '../assets/misc/light_beacon_red.png',
        #                         '../assets/misc/light_beacon_red.png',
        #                         (924, 924))
        # lu_beacon4 = LightBeacon(screen,
        #                         '../assets/misc/light_beacon_red.png',
        #                         '../assets/misc/light_beacon_red.png',
        #                         (924, 25))

        # self.balises.append(lu_beacon1)
        # self.balises.append(lu_beacon2)
        # self.balises.append(lu_beacon3)
        # self.balises.append(lu_beacon4)

    def draw_stuff_on(self):
        # Render elements
        for b in self.balises:
            b.draw()
        for b in self.balises_additionnals:
            b.draw()
