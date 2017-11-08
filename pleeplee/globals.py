#/usr/bin/env python3

import os
import pygame

# Global parameter

FPS = 40
fps_clock = pygame.time.Clock()
screen_width = 1300
screen_height = 950

basePath = os.path.dirname(__file__)
assetsPath = os.path.join(basePath, '../assets')
fontPath = os.path.join(basePath, '../fonts')
