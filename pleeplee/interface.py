#!/usr/bin/env python3

import pygame
from .menu import menu_loop
from .globals import screen_width, screen_height


def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Appleeplee!')

    # Run the menu
    menu_loop(screen)

