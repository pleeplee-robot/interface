#!/usr/bin/env python3

import pygame
import sys
import time
import os

from pygame.locals import *
from .button import Button
from .pygame_textinput import TextInput
from .globals import (screen_width, screen_height, FPS, fps_clock,
                      fontPath, assetsPath)
from .tool import (swap_c_is_chosing_color, swap_t_is_chosing_color,
        game_quit, finish_balise, done_balise, undo_balise, add_balise,
        add_more_balise, blit_on)


class MenuInit:

    # surface should be a surface of the size of 350x950
    def __init__(self, surface_e, screen):
        # get a surface
        self.surface = surface_e
        self.surface.fill((255, 255, 255))
        self.title = "Initialization"
        self.text_input = TextInput((1001, 140), 7)
        self.color_input = TextInput((1161, 140), 7)
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
        brickTexture = os.path.join(assetsPath, 'textures/brick.jpg')
        blit_on(self.surface, brickTexture)

        # Render title
        myFontPath = os.path.join(fontPath, 'Capture_it.ttf')
        myfont = pygame.font.Font(myFontPath, 20)
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
        buttonQuitA = os.path.join(assetsPath, 'buttons/button_quit_a.png')
        buttonQuit = os.path.join(assetsPath, 'buttons/button_quit.png')
        button_quit = Button(1000, 800, 232, 93, buttonQuitA, buttonQuit,
                game_quit)

        buttonDoneA = os.path.join(assetsPath, 'buttons/button_done_a.png')
        buttonDone = os.path.join(assetsPath, 'buttons/button_done.png')
        button_done = Button(1000, 700, 232, 93,
                             buttonDoneA, buttonDone, done_balise)

        buttonAddA = os.path.join(assetsPath, 'buttons/button_add_balise_a.png')
        buttonAdd = os.path.join(assetsPath, 'buttons/button_add_balise.png')
        button_add_balise = Button(1000, 200, 232, 93,
                                   buttonAddA, buttonAdd, add_balise)

        buttonUndoA = os.path.join(assetsPath,
                'buttons/button_undo_balise_a.png')
        buttonUndo = os.path.join(assetsPath, 'buttons/button_undo_balise.png')
        button_undo = Button(1000, 300, 232, 93,
                             buttonUndoA, buttonUndo, undo_balise)

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

        buttonUndoA = os.path.join(assetsPath,
                'buttons/button_undo_balise_a.png')
        buttonUndo = os.path.join(assetsPath, 'buttons/button_undo_balise.png')
        button_undo = Button(1000, 300, 232, 93,
                             buttonUndoA, buttonUndo, undo_more_balise)

        buttonFinishA = os.path.join(assetsPath, 'buttons/button_finish_a.png')
        buttonFinish = os.path.join(assetsPath, 'buttons/button_finish.png')
        button_finish = Button(1000, 700, 232, 93,
                               buttonFinishA, buttonFinish, finish_balise)

        buttonAddA = os.path.join(assetsPath, 'buttons/button_add_more_a.png')
        buttonAdd = os.path.join(assetsPath, 'buttons/button_add_more.png')
        button_add_more_balise = Button(1000, 200, 232, 93,
                                        buttonAddA, buttonAdd, add_more_balise)

        self.buttons.append(button_undo)
        self.buttons.append(button_finish)
        self.buttons.append(button_add_more_balise)
