#!/usr/bin/env python3

import time
import pygame
from pygame.locals import *
from pygame.sprite import Sprite

import sys
from .vec2d import vec2d

class LightBeacon(Sprite):

    # surface should be a surface of the size of 950x950
    def __init__(self, screen, img_filename, imga_filename, init_position,
                 color, action=None):
        Sprite.__init__(self)
        self.screen = screen
        self.image_na = pygame.image.load(img_filename).convert_alpha()
        self.image_a = pygame.image.load(imga_filename).convert_alpha()
        self.init_pos = init_position
        self.pos = vec2d(init_position)
        self.color = color
        self.action = action
        self.isactive = False

    # draw on the given surface
    def draw(self):
        if (self.isactive):
            self.draw_rect = self.image_a.get_rect().move(
                self.pos.x - self.image_a.get_width() / 2,
                self.pos.y - self.image_a.get_height() / 2)
            self.screen.blit(self.image_a, self.draw_rect)
        else:
            self.draw_rect = self.image_na.get_rect().move(
                self.pos.x - self.image_na.get_width() / 2,
                self.pos.y - self.image_na.get_height() / 2)
            self.screen.blit(self.image_na, self.draw_rect)


    def update(self, screen):
        mouse = pygame.mouse.get_pos() # mouse[0] : x / mouse[1] : y
        click = pygame.mouse.get_pressed()

        if (self.pos.x + self.image_na.get_width() > mouse[0] > self.pos.x
            and self.pos.y + self.image_na.get_height() > mouse[1] > self.pos.y):
            self.isactive = True
            if (click[0] and self.action != None):
                self.action(screen)
        else:
            self.isactive = False
