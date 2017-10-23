#!/usr/bin/env python3.5

import pygame
import sys
import time

from pygame.locals import *
from button import *
from main import *

screen_width = 1100
screen_height = 950
FPS = 40
fps_clock = pygame.time.Clock()

def draw_menu(screen, menu_img):
    menu = pygame.image.load(menu_img).convert_alpha()
    screen.blit(menu, (0, 0))


def menu_loop(screen):

    button_init = Button(screen_width * 0.50, screen_width * 0.50, 232, 93,
                         "../assets/buttons/button_initialisation_a.png",
                         "../assets/buttons/button_initialisation.png",
                         appli_init_loop)
    button_fetch = Button(screen_width * 0.50, screen_width * 0.60, 232, 93,
                          "../assets/buttons/button_fetch_a.png",
                          "../assets/buttons/button_fetch.png",
                          appli_fetch_loop)

    while True: # Menu game loop
        # Update
        time_passed = fps_clock.tick(FPS)
        button_init.update(screen, None, None, None)
        button_fetch.update(screen, None, None, None)

        # Draw menu
        draw_menu(screen, "../assets/misc/maison.jpg")
        button_init.draw(screen)
        button_fetch.draw(screen)

        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
