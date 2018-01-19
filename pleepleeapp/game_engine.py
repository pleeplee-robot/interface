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
                      basePath, factor_size)


class GameEngine:
    """Game engine and core information representation.

    Contains the information related to the core application.

    Attributes:
        balises: List of the main balises in the garden.
        balises_addtionnals: List of the addionnal balises in the garden.
        plants: List of the plant in the garden.
        obstacles: List of the obstacles in the garden.
        outfile_json: name of the json file that is created after initialisation.
    """

    def __init__(self, screen):
        """ Initialize game engine with the screen pygame object."""
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
        """Function that call the draw function of all the inner object of the game
        engine.
        """
        for b in self.balises:
            b.draw()
        for b in self.balises_additionnals:
            b.draw()

    def set_plant(self, plant_info):
        """Set new plant information.

        Args:
            self: The current game engine.
            plant_info: List of plant information retrieved from the init file.
        """
        dataPath = os.path.join(basePath, '../fetch/data_json')
        with open(dataPath) as json_file:
            data = json.load(json_file)
            for plant_i in plant_info:
                if 'plants' in data:
                    for p in data['plants']:
                        p_tab = p['position'].split(",")
                        self.plants.append(Plant(int(int(p_tab[0]) * factor_size),
                                                 int(int(p_tab[1]) * factor_size),
                                                 plant_i[1], plant_i[1],
                                                 p['picture_path']))

    def set_obstacles(self):
        """ Set osbtacles information.
        """
        dataPath = os.path.join(basePath, '../fetch/data_json')
        with open(dataPath) as json_file:
            data = json.load(json_file)
            if 'obstacles' in data:
                for p in data['obstacles']:
                    p_tab = p['position'].split(",")
                    self.obstacles.append(Plant(int(int(p_tab[0]) * factor_size),
                                                int(int(p_tab[1]) * factor_size),
                                                60, 60, p['picture_path']))
