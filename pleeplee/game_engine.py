#!/usr/bin/env python3

import pygame
import sys
import time
import json
import os

from pygame.locals import *
from .button import Button
from .light_beacon import LightBeacon
from .plant import Plant
from .globals import (screen_width, screen_height, FPS, fps_clock, assetsPath,
        basePath)


class GameEngine:

    # surface should be a surface of the size of 350x950
    def __init__(self, screen):
        self.balises = []
        self.balises_additionnals = []
        self.plants = []
        self.obstacles = []
        self.outfile_json = 'data_json'
        beaconRed = os.path.join(assetsPath, 'misc/light_beacon_red.png')
        lu_beacon1 = LightBeacon(screen, beaconRed, beaconRed, (50, 50), 'red')
        beaconGreen = os.path.join(assetsPath, 'misc/light_beacon_green.png')
        lu_beacon2 = LightBeacon(screen, beaconGreen, beaconGreen,
                                 (50, 899), 'green')
        beaconWhite = os.path.join(assetsPath, 'misc/light_beacon_white.png')
        lu_beacon3 = LightBeacon(screen, beaconWhite, beaconWhite,
                                 (899, 899), 'white')
        beaconBlue = os.path.join(assetsPath, 'misc/light_beacon_blue.png')
        lu_beacon4 = LightBeacon(screen, beaconBlue, beaconBlue,
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
        dataPath = os.path.join(basePath, 'data_json')
        with open(dataPath) as json_file:
            data = json.load(json_file)

            for plant_i in plant_info:
                for p in data['plants']:
                    p_tab = p['position'].split(",")
                    if plant_i[0][0] == int(p_tab[0]) and int(p_tab[1]) == plant_i[0][1]:
                        self.plants.append(Plant(plant_i[0][0], plant_i[0][1],
                                            plant_i[1], plant_i[1],
                                            p['picture_path']))
                        break
