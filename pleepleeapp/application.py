#!/usr/bin/env python3

import pygame
import sys
import time
import os
from . import pygame_textinput

from .game_engine import GameEngine
from pygame.locals import *
from .g_map import Map
from .menu_init import MenuInit
from .menu_fetch import MenuFetch
from .light_beacon import LightBeacon
from .globals import FPS, fps_clock, screen_width, screen_height, basePath


def appli_init_loop(screen, menu=None, game=None, game_map=None, param=None):
    """Loop when the application is launch to init the robot.

    Args:
        screen: Pygame screen object on which everything is blitted.
        menu: Menu Object that contains everything related to the menu.
        game: game Object that contains everything related to the core application.
        game_map: Map object that represents the map part of the application.
        param: Any additionnal parameter, due to callback (legacy).
    """
    with open('pleeplee/.config', 'r') as f:
        g_s = f.readline()
        garden_size = float(g_s)
        factor_size = 900 / garden_size

    game_map = Map(pygame.Surface((950, 950), pygame.SRCALPHA))
    game_engine = GameEngine(screen)
    game_menu = MenuInit(pygame.Surface((350, 950), pygame.SRCALPHA), screen)
    white = (255, 255, 255)

    screen.fill(white)
    game_map.init_map("map.capture_init")

    while True: # Main game loop
        events = pygame.event.get()

        # Update
        time_passed = fps_clock.tick(FPS)
        game_menu.update(screen, game_engine, game_map, events)

        # Handle events
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Draw scene
        game_map.draw_on(screen)
        game_menu.draw_on(screen)
        game_engine.draw_stuff_on()

        pygame.display.flip()
        fps_clock.tick(30)

def appli_fetch_loop(screen, menu=None, game=None, game_map=None, param=None):
    """Loop when the application is launch to fetch the data of the robot
    and let the user interact with it.

    Args:
        screen: Pygame screen object on which everything is blitted.
        menu: Menu Object that contains everything related to the menu.
        game: game Object that contains everything related to the core application.
        game_map: Map object that represents the map part of the application.
        param: Any additionnal parameter, due to callback (legacy).
    """
    with open('pleeplee/.config', 'r') as f:
        g_s = f.readline()
        garden_size = float(g_s)
        factor_size = 900 / garden_size

    game_map = Map(pygame.Surface((950, 950), pygame.SRCALPHA))
    game_engine = GameEngine(screen)
    game_menu = MenuFetch(pygame.Surface((350, 950), pygame.SRCALPHA), screen)
    white = (255, 255, 255)

    screen.fill(white)
    mapPath = os.path.join(basePath, '../fetch/map.capture_init')
    plant_info = game_map.init(mapPath)
    game_engine.set_obstacles()
    game_engine.set_plant(plant_info)
    game_menu.init_buttons(game_engine)
    while True: # Main game loop
        events = pygame.event.get()

        # Update
        time_passed = fps_clock.tick(FPS)
        game_menu.update(screen, game_engine, game_map, events)

        # Handle events
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Draw scene
        game_map.draw_on(screen)
        game_menu.draw_on(screen)
        game_engine.draw_stuff_on()

        pygame.display.flip()
        fps_clock.tick(30)
