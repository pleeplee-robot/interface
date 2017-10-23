#!/usr/bin/env python3.5

import pygame
import sys
import time

from pygame.locals import *
from button import *
from main import *

screen_width = 1300
screen_height = 950
FPS = 40
fps_clock = pygame.time.Clock()

class MenuFetch:

    # surface should be a surface of the size of 350x950
    def __init__(self, surface_e, screen):
        # get a surface
        self.surface = surface_e
        self.surface.fill((255, 255, 255))
        self.plant_im = None
        self.title = "Fetch"
        self.text_input = None

        self.buttons = []

        #self.init_buttons()
        self.init_menu(screen)
        self.time_passed = 0
        self.is_color_chosing = False

    def draw_on(self, screen):
        # Render background
        if self.plant_im != None:
            self.surface.blit(self.plant_im, (5,50))
        screen.blit(self.surface, (950, 0))

        # Render buttons

        if self.plant_im != None:
            for b in self.buttons:
                b.draw(screen)
        else:
            for i in range(0, len(self.buttons) - 3):
                self.buttons[i].draw(screen)
        if self.text_input != None:
            screen.blit(self.text_input.get_surface(), self.text_input.init_pos)

    def init_menu(self, screen):
        # Render texture background
        blit_on(self.surface, "../assets/textures/brick.jpg")

        # Render title
        myfont = pygame.font.Font("../fonts/Capture_it.ttf", 20)
        title_surface = myfont.render(self.title, False, (255, 255, 255))
        self.surface.blit(title_surface, (8, 0))

        # Render instructions
        # msg_surface = myfont.render("min: 0 | max: 899 | unit: cm/px",
        #                             False, (0, 255, 55))
        # self.surface.blit(msg_surface, (8, 48))
        # msg_surface = myfont.render("Color: red, blue, green, yellow, purple",
        #                             False, (255, 155, 255))
        # self.surface.blit(msg_surface, (8, 65))
        # msg_surface = myfont.render("           orange, white",
        #                             False, (255, 155, 255))
        # self.surface.blit(msg_surface, (8, 79))

        # msg_surface = myfont.render("coordinate:",
        #                             False, (255, 255, 255))
        # self.surface.blit(msg_surface, (55, 110))

        # msg_surface = myfont.render("color:",
        #                             False, (255, 255, 255))
        # self.surface.blit(msg_surface, (210, 110))


        # Render buttons
        #for b in self.buttons:
        #    b.draw(screen)

    def update(self, screen, game_engine, game_map, events):
        # update text
        if self.text_input != None:
            self.text_input.update(events)

        self.time_passed += fps_clock.tick(FPS)

        # update buttons
        if self.time_passed >= 150:
            if self.plant_im != None:
                for b in self.buttons:
                    b.update(screen, self, game_engine, game_map)
            else:
                for i in range(0, len(self.buttons) - 3):
                    self.buttons[i].update(screen, self, game_engine, game_map)

        fps_clock.tick(30)

    def init_buttons(self, game_engine):
        for p in game_engine.plants:
            button_plant = Button(p.pos_x + 25, p.pos_y + 25, p.width, p.height,
                                  "../assets/misc/plant_a.png",
                                  "../assets/misc/plant.png", show_plant, p)
            self.buttons.append(button_plant)

        button_quit = Button(1000, 800, 232, 93,
                             "../assets/buttons/button_quit_a.png",
                             "../assets/buttons/button_quit.png",
                             game_quit)

        button_finish = Button(1000, 700, 232, 93,
                               "../assets/buttons/button_finish_a.png",
                               "../assets/buttons/button_finish.png",
                               game_quit)

        text_input_button = Button(969, 323, 95, 30,
                                   None,
                                   None,
                                   None)

        button_set = Button(1000, 400, 232, 93,
                            "../assets/buttons/button_set_a.png",
                            "../assets/buttons/button_set.png",
                            set_water)

        button_remove = Button(1000, 500, 232, 93,
                               "../assets/buttons/button_remove_a.png",
                               "../assets/buttons/button_remove.png",
                               remove_plant)


        self.buttons.append(button_quit)
        self.buttons.append(button_finish)
        self.buttons.append(text_input_button)
        self.buttons.append(button_set)
        self.buttons.append(button_remove)
