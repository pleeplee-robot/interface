#!/usr/bin/env python3

import pygame
from pygame.locals import *

import sys
import time

class Button:
    """Simple button representation.

    Contains the logic of clicking and calling a predefine function after that.

    Attributes:
        pos_x: x corrdinate of the button
        pos_y: y corrdinate of the button
        width: width of the button
        height: height of the button
        image_a: path of the image when the mouse is on the button
        image_na: path of the image when the mouse is not on the button
        action: function that is called when clicking on the button
        plant: contains a plant object if the button is connected with a plant
    """
    def __init__(self, pos_x, pos_y, width, height, image_a=None, image_na=None,
                 action=None, plant=None):
        """ Initialiaze all the attribute of the button object."""
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
        """Called in the gameloop to update the status of the button
        and call action if needed

        Args:
            self: The current button object.
            screen: Pygame screen object on which everything is blitted.
            menu: Menu Object that contains everything related to the menu.
            game: game Object that contains everything related to the core application.
            game_map: Map object that represents the map part of the application.
        """

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
        """Draw the button on the screen thanks to initialized image attribute

        Args:
            self: The current button object.
            screen: Pygame screen object on which everything is blitted.
        """
        if (self.isactive):
            screen.blit(self.image_a, self.draw_rect)
        else:
            screen.blit(self.image_na, self.draw_rect)
