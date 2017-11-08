#!/usr/bin/env python3

import pygame
import sys
import time
import os

from pygame.locals import *
from .button import Button
from .application import appli_init_loop, appli_fetch_loop
from .globals import screen_width, screen_height, FPS, fps_clock, assetsPath


def draw_menu(screen, menu_img):
    menu = pygame.image.load(menu_img).convert_alpha()
    screen.blit(menu, (0, 0))


def menu_loop(screen):

    buttonInitA = os.path.join(assetsPath,
                               'buttons/button_initialisation_a.png')
    buttonInit = os.path.join(assetsPath, 'buttons/button_initialisation.png')
    button_init = Button(screen_width * 0.50, screen_width * 0.50, 232, 93,
                         buttonInitA, buttonInit, appli_init_loop)

    buttonFetchA = os.path.join(assetsPath, 'buttons/button_fetch_a.png')
    buttonFetch = os.path.join(assetsPath, 'buttons/button_fetch.png')
    button_fetch = Button(screen_width * 0.50, screen_width * 0.60, 232, 93,
                          buttonFetchA, buttonFetch, appli_fetch_loop)

    while True: # Menu game loop
        # Update
        time_passed = fps_clock.tick(FPS)
        button_init.update(screen, None, None, None)
        button_fetch.update(screen, None, None, None)

        # Draw menu
        housePic = os.path.join(assetsPath, 'misc/maison.jpg')
        draw_menu(screen, housePic)
        button_init.draw(screen)
        button_fetch.draw(screen)

        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
