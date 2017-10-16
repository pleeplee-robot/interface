#!/usr/bin/env python3.5

import pygame
import sys
import time
import pygame_textinput

from menu import *
from game_engine import *
from pygame.locals import *
from g_map import *
from menu_init import *
from light_beacon import *

FPS = 40
fps_clock = pygame.time.Clock()

screen_width = 1300
screen_height = 950

def appli_init_loop(screen, menu=None, game=None, game_map=None):
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

def appli_fetch_loop(screen):
    game_map = Map(pygame.Surface((950, 950), pygame.SRCALPHA))
    game_map.init("map.capture")

    lu_beacon = LightBeacon(screen, '../assets/misc/light_beacon_red.png', (25, 25))
    ld_beacon = LightBeacon(screen, '../assets/misc/light_beacon_red.png', (25, 800))
    ru_beacon = LightBeacon(screen, '../assets/misc/light_beacon_red.png', (800, 25))
    rd_beacon = LightBeacon(screen, '../assets/misc/light_beacon_red.png', (800, 800))
    beacons = [lu_beacon, ld_beacon, ru_beacon, rd_beacon]

    white = (255, 255, 255)

    while True: # Main game loop
        # Update
        time_passed = fps_clock.tick(FPS)

        screen.fill(white)

        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Draw scene
        game_map.draw_on(screen)

        # Draw entity
        for i in range(0, len(beacons)):
            beacons[i].draw()

        pygame.display.flip()
    return

def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Hello World!')

    # Run the menu
    menu_loop(screen)

if __name__ == "__main__":
    sys.exit(main())
