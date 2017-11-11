#!/usr/bin/env python3

import pygame
from pygame.locals import *

import sys
import time
import os

from .tool import blit_on
from .globals import assetsPath

class Map:
    """Game map representation.

    Contains the information related to the map on graphics part.

    Attributes:
        surface: pygame surface that contains the whole garden graphics
        surface_grass: pygame surface that contains only grass part of the garden
    """

    # surface should be a surface of the size of 950x950
    def __init__(self, surface_e):
        """Initilialize the map with a 950x950 surface by default"""
        # get a surface
        self.surface = surface_e
        self.surface.fill((255, 255, 255))
        self.surface_grass = self.surface.copy()


    def create_plant(self, map_data, y , x, plant_info):
        """Parse the map.init file and retrieve plant information

        Args:
            self: the current map.
            map_data: the character file that represent the garden.
            y: y coordinate in the garden.
            x: x coordinate in the garden.
            plant_info: list of plant information
        """
        width = 1
        acc_x = x + 1
        acc_y = y

        while map_data[900 * y + acc_x] == 'P':
            map_data[900 * y + acc_x] = 'G'
            width += 1;
            acc_x += 1

        for j in range(y + 1, y + width):
            for i in range(x, x + width):
                map_data[900 * j + i] = 'G'
        plant_info.append(((x, y), width))

    def parse_file(self, map_filed, mask):
        """Parse the map init file and create of mask for blitting grass surface
        on durt surface
        """

        map_data = []
        plant_info = []
        with open(map_filed, 'r') as f:
            map_data = list(f.read().replace('\n', ''))
            for y in range(0, 900):
                for x in range(0, 900):
                    c = map_data[900 * y + x]
                    if not c:
                        print("End of file")
                        break
                    if c == 'G':
                        self.surface.set_at((x + 25 , y + 25), Color("white"))
                    elif c == 'O':
                        # insert obstacle
                        continue
                    elif c == 'P':
                        self.create_plant(map_data, y, x, plant_info)
                        continue
                    elif c == 'F':
                        # insert flower
                        continue
                    elif c == 'B':
                        # insert balise
                        continue
                    elif c == 'D':
                        # insert balise
                        mask.set_at((x, y), Color("white"))
                    else:
                        mask.set_at((x, y), Color("white"))
        f.close()
        return plant_info

    def init_map(self, map_name):
        """Initialize graphics part with a map init file."""

        file_obj = open(map_name, "w+")
        for y in range(0, 900):
            for x in range(0, 900):
                file_obj.write("D")
        file_obj.close()
        textureDirt = os.path.join(assetsPath, 'textures/durt2.jpg')
        textureGrass = os.path.join(assetsPath, 'textures/grass.jpg')
        blit_on(self.surface, textureDirt)
        blit_on(self.surface_grass, textureGrass)


    def init(self, map_filed):
        """Initialize graphics part with a map init file."""

        mask = pygame.Surface((899, 899), pygame.SRCALPHA)
        mask.fill((255, 255, 255))
        textureDirt = os.path.join(assetsPath, 'textures/durt2.jpg')
        textureGrass = os.path.join(assetsPath, 'textures/grass.jpg')
        blit_on(self.surface, textureDirt)
        blit_on(mask, textureGrass)
        # Modify mask and surface depending the file / should pass later
        # an object controler for balise, flower and obstacle
        plant_info = self.parse_file(map_filed, mask)

        self.surface.blit(mask, (25, 25), None, pygame.BLEND_RGBA_MULT)
        return plant_info

    def mask_grass_on_durt(self, map_data):
        """Apply grass mask on the dust surface to draw grass in the garden"""
        for j in range(0, self.surface.get_height()):
            for i in range(0, self.surface.get_width()):
                if self.surface.get_at((i, j)) != Color("white"):
                    self.surface_grass.set_at((i, j), Color("white"))
                else:
                    map_data[900 * (j - 25) + i - 25] = 'G'

        self.surface.blit(self.surface_grass, (0, 0), None, pygame.BLEND_RGBA_MULT)

    # draw on the given surface
    def draw_on(self, screen):
        """Draw the map on the main screen"""
        screen.blit(self.surface, (0, 0))
