#!/usr/bin/env python3.5

import pygame
from pygame.locals import *

import sys
import time
from tool import *

class Map:

    # surface should be a surface of the size of 950x950
    def __init__(self, surface_e):
        # get a surface
        self.surface = surface_e
        self.surface.fill((255, 255, 255))
        self.surface_grass = self.surface.copy()

    def parse_file(self, map_filed, mask):
        with open(map_filed) as f:
            for y in range(25, 925):
                for x in range(25, 925):
                    c = f.read(1)
                    if not c:
                        print("End of file")
                        break
                    if c == 'G':
                        mask.set_at((x, y), Color("white"))
                    elif c == 'O':
                        # insert obstacle
                        continue
                    elif c == 'F':
                        # insert flower
                        continue
                    elif c == 'B':
                        # insert balise
                        continue
                    elif c == 'D':
                        # insert balise
                        self.surface.set_at((x, y), Color("white"))
                    else:
                        self.surface.set_at((x, y), Color("white"))

    # init map
    def init_map(self, map_name):
        # FIXME check if open failed
        file_obj = open(map_name, "w+")
        for y in range(0, 900):
            for x in range(0, 900):
                file_obj.write("D")
        file_obj.close()
        blit_on(self.surface, "../assets/textures/durt2.jpg")
        blit_on(self.surface_grass, "../assets/textures/grass.jpg")


    def init(self, map_filed):
        dirt_img = pygame.image.load("../assets/textures/durt2.jpg").convert_alpha()
        grass_img = pygame.image.load("../assets/textures/grass.jpg").convert_alpha()

        grass_rect = grass_img.get_rect()
        dirt_rect = dirt_img.get_rect()

        surface_h = self.surface.get_height()
        surface_w = self.surface.get_width()

        nrows_grass = int(surface_h / grass_rect.height) + 1
        ncols_grass = int(surface_w / grass_rect.width) + 1
        nrows_dirt = int(surface_h / dirt_rect.height) + 1
        ncols_dirt = int(surface_w / dirt_rect.width) + 1

        for y in range(nrows_grass):
            for x in range(ncols_grass):
                grass_rect.topleft = ((x * grass_rect.width) + 25,
                                      (y * grass_rect.height) + 25)
                self.surface.blit(grass_img, grass_rect)

        mask = pygame.Surface((surface_w, surface_h), pygame.SRCALPHA)
        for y in range(nrows_dirt):
            for x in range(ncols_dirt):
                dirt_rect.topleft = (x * dirt_rect.width,
                                     y * dirt_rect.height)
                mask.blit(dirt_img, dirt_rect)

        # Modify mask and surface depending the file / should pass later
        # an object controler for balise, flower and obstacle
        self.parse_file(map_filed, mask)

        self.surface.blit(mask, (0, 0), None, pygame.BLEND_RGBA_MULT)

    def mask_grass_on_durt(self):
        for j in range(0, self.surface.get_height()):
            for i in range(0, self.surface.get_width()):
                if self.surface.get_at((i, j)) != Color("white"):
                    self.surface_grass.set_at((i, j), Color("white"))


        self.surface.blit(self.surface_grass, (0, 0), None, pygame.BLEND_RGBA_MULT)

    # draw on the given surface
    def draw_on(self, screen):
        screen.blit(self.surface, (0, 0))
