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

class MenuInit:

    # surface should be a surface of the size of 350x950
    def __init__(self, surface_e, screen):
        # get a surface
        self.surface = surface_e
        self.surface.fill((255, 255, 255))
        self.title = "Initialization"
        self.text_input = pygame_textinput.TextInput((1001, 140), 7)
        self.color_input = pygame_textinput.TextInput((1161, 140), 7)
        self.buttons = []

        self.init_buttons()
        self.init_menu(screen)
        self.time_passed = 0
        self.is_color_chosing = False

    def draw_on(self, screen):
        # Render background
        screen.blit(self.surface, (950, 0))

        # Render buttons
        for b in self.buttons:
            b.draw(screen)

        screen.blit(self.text_input.get_surface(), self.text_input.init_pos)
        screen.blit(self.color_input.get_surface(), self.color_input.init_pos)

    def init_menu(self, screen):
        # Render texture background
        blit_on(self.surface, "../assets/textures/brick.jpg")

        # Render title
        myfont = pygame.font.Font("../fonts/Capture_it.ttf", 20)
        title_surface = myfont.render(self.title, False, (255, 255, 255))
        self.surface.blit(title_surface, (8, 0))

        # Render instructions
        myfont = pygame.font.SysFont("comicsansms", 15)
        msg_surface = myfont.render("Enter coordinate of the balise in the form 0;899",
                                    False, (0, 255, 55))
        self.surface.blit(msg_surface, (8, 35))
        msg_surface = myfont.render("min: 0 | max: 899 | unit: cm/px",
                                    False, (0, 255, 55))
        self.surface.blit(msg_surface, (8, 48))
        msg_surface = myfont.render("Color: red, blue, green, yellow, purple",
                                    False, (255, 155, 255))
        self.surface.blit(msg_surface, (8, 65))
        msg_surface = myfont.render("           orange, white",
                                    False, (255, 155, 255))
        self.surface.blit(msg_surface, (8, 79))

        msg_surface = myfont.render("coordinate:",
                                    False, (255, 255, 255))
        self.surface.blit(msg_surface, (55, 110))

        msg_surface = myfont.render("color:",
                                    False, (255, 255, 255))
        self.surface.blit(msg_surface, (210, 110))


        # Render buttons
        for b in self.buttons:
            b.draw(screen)

    def update(self, screen, game_engine, game_map, events):
        # update text
        if self.is_color_chosing:
            self.color_input.update(events)
        else:
            self.text_input.update(events)

        self.time_passed += fps_clock.tick(FPS)

        # update buttons
        if self.time_passed >= 150:
            for b in self.buttons:
                b.update(screen, self, game_engine, game_map)

        fps_clock.tick(30)

    def init_buttons(self):
        text_input_button = Button(1000, 140, 95, 30,
                                   None,
                                   None,
                                   swap_t_is_chosing_color)
        color_input_button = Button(1160, 140, 95, 30,
                                   None,
                                   None,
                                   swap_c_is_chosing_color)
        button_quit = Button(1000, 800, 232, 93,
                             "../assets/buttons/button_quit_a.png",
                             "../assets/buttons/button_quit.png",
                             game_quit)

        button_done = Button(1000, 700, 232, 93,
                             "../assets/buttons/button_done_a.png",
                             "../assets/buttons/button_done.png",
                             done_balise)

        button_add_balise = Button(1000, 200, 232, 93,
                                   "../assets/buttons/button_add_balise_a.png",
                                   "../assets/buttons/button_add_balise.png",
                                   add_balise)

        button_undo = Button(1000, 300, 232, 93,
                            "../assets/buttons/button_undo_balise_a.png",
                             "../assets/buttons/button_undo_balise.png",
                             undo_balise)

        self.buttons.append(text_input_button)
        self.buttons.append(color_input_button)
        self.buttons.append(button_quit)
        self.buttons.append(button_undo)
        self.buttons.append(button_add_balise)
        self.buttons.append(button_done)

    def button_afterdone(self):
        self.buttons.pop()
        self.buttons.pop()
        self.buttons.pop()

        button_undo = Button(1000, 300, 232, 93,
                            "../assets/buttons/button_undo_balise_a.png",
                             "../assets/buttons/button_undo_balise.png",
                             undo_more_balise)

        button_finish = Button(1000, 700, 232, 93,
                             "../assets/buttons/button_finish_a.png",
                             "../assets/buttons/button_finish.png",
                               finish_balise)

        button_add_more_balise = Button(1000, 200, 232, 93,
                                        "../assets/buttons/button_add_more_a.png",
                                        "../assets/buttons/button_add_more.png",
                                        add_more_balise)

        self.buttons.append(button_undo)
        self.buttons.append(button_finish)
        self.buttons.append(button_add_more_balise)
