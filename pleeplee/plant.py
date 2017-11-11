#!/usr/bin/env python3

import pygame
from pygame.locals import *

import sys
import time

class Plant:
    """Simple plant representation.

    Contains information of a plant.

    Attributes:
        pos_x: x coordinate of the plant.
        pos_y: y coordinate of the plant.
        width: width of the plant.
        height: height of the plant.
        picture_path: path to the picture file that represents the plant
    """
    def __init__(self, pos_x, pos_y, width, height, picture_path):
        """Initialize the plant with position, dimension and picture path"""
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.picture_path = picture_path
        self.time_to_water = 0
