#!/usr/bin/env python3.5

import pygame
import sys
import time
import json

from pygame.locals import *
from button import *
from main import *
from light_beacon import *
from plant import *

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
        lu_beacon1 = LightBeacon(screen,
                                '../assets/misc/light_beacon_red.png',
                                '../assets/misc/light_beacon_red.png',
                                 (50, 50), 'red')
        lu_beacon2 = LightBeacon(screen,
                                '../assets/misc/light_beacon_green.png',
                                '../assets/misc/light_beacon_green.png',
                                 (50, 899), 'green')
        lu_beacon3 = LightBeacon(screen,
                                '../assets/misc/light_beacon_white.png',
                                '../assets/misc/light_beacon_white.png',
                                 (899, 899), 'white')
        lu_beacon4 = LightBeacon(screen,
                                '../assets/misc/light_beacon_blue.png',
                                '../assets/misc/light_beacon_blue.png',
                                 (899, 50), 'blue')

        self.balises.append(lu_beacon1)
        self.balises.append(lu_beacon2)
        self.balises.append(lu_beacon3)
        self.balises.append(lu_beacon4)

    def draw_stuff_on(self):
        # Render elements
        for b in self.balises:
            b.draw()
        for b in self.balises_additionnals:
            b.draw()

    def set_plant(self, plant_info):
        with open('data_json') as json_file:
            data = json.load(json_file)

            for plant_i in plant_info:
                for p in data['plants']:
                    p_tab = p['position'].split(",")
                    if plant_i[0][0] == int(p_tab[0]) and int(p_tab[1]) == plant_i[0][1]:
                        self.plants.append(Plant(plant_i[0][0], plant_i[0][1],
                                            plant_i[1], plant_i[1],
                                            p['picture_path']))
                        break
