#!/usr/bin/env python3.5

import pygame
from pygame.locals import *

import sys
import time

class Button:

    # Button constructor
    def __init__(self, pos_x, pos_y, width, height, image_a=None, image_na=None,
                 action=None, plant=None):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.action = action
        self.isactive = False
        self.plant = plant

        if (image_a is not None and image_na is not None):
            self.image_a = pygame.image.load(image_a).convert_alpha()
            self.image_a = pygame.transform.scale(self.image_a, (width, height))
            self.image_na = pygame.image.load(image_na).convert_alpha()
            self.image_na = pygame.transform.scale(self.image_na, (width, height))
            self.draw_rect = self.image_a.get_rect().move(self.pos_x, self.pos_y)
        else:
            self.image_a = pygame.Surface((width, height), pygame.SRCALPHA)
            self.image_a.fill((255, 255, 255))
            self.image_na = self.image_a
            self.draw_rect = self.image_a.get_rect().move(self.pos_x, self.pos_y)

    def update(self, screen=None, menu=None, game=None, game_map=None):
        mouse = pygame.mouse.get_pos() # mouse[0] : x / mouse[1] : y
        click = pygame.mouse.get_pressed()

        if (self.pos_x + self.width > mouse[0] > self.pos_x
            and self.pos_y + self.height > mouse[1] > self.pos_y):
            self.isactive = True
            if (click[0] and self.action != None):
                self.action(screen, menu, game, game_map, self.plant)
        else:
            self.isactive = False

    def draw(self, screen):
        if (self.isactive):
            screen.blit(self.image_a, self.draw_rect)
        else:
            screen.blit(self.image_na, self.draw_rect)
