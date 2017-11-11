#!/usr/bin/env python3

import time
import pygame
from pygame.locals import *
from pygame.sprite import Sprite

import sys
from .vec2d import vec2d

class LightBeacon(Sprite):
    """Simple Balise representation.

    Contains utility functions for balises manipulation.

    Attributes:
        screen: pygame screen object.
        image_a: path of the image when the mouse is not on the button.
        image_na: path of the image when the mouse is on the button.
        init_pos: init position.
        pos: current position.
        color: color of the balise.
        action: callback function when clicking on the balise.
        is_active: tells if the balise is active or not.
    """

    def __init__(self, screen, img_filename, imga_filename, init_position,
                 color, action=None):
        """Initialize balise width screen, images path, positionn, color and callback"""

        Sprite.__init__(self)
        self.screen = screen
        self.image_na = pygame.image.load(img_filename).convert_alpha()
        self.image_a = pygame.image.load(imga_filename).convert_alpha()
        self.init_pos = init_position
        self.pos = vec2d(init_position)
        self.color = color
        self.action = action
        self.isactive = False


    def draw(self):
        """Draw the current balise"""
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
        """Update the current balise"""

        mouse = pygame.mouse.get_pos() # mouse[0] : x / mouse[1] : y
        click = pygame.mouse.get_pressed()

        if (self.pos.x + self.image_na.get_width() > mouse[0] > self.pos.x
            and self.pos.y + self.image_na.get_height() > mouse[1] > self.pos.y):
            self.isactive = True
            if (click[0] and self.action != None):
                self.action(screen)
        else:
            self.isactive = False
