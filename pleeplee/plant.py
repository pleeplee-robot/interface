#!/usr/bin/env python3

import pygame
from pygame.locals import *

import sys
import time

class Plant:

    # Button constructor
    def __init__(self, pos_x, pos_y, width, height, picture_path):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.picture_path = picture_path
        self.time_to_water = 0
