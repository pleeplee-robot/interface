#!/usr/bin/env python3.5

import pygame
import sys
import time
import json

from pygame.locals import *
from light_beacon import *

screen_width = 1100
screen_height = 950
FPS = 40
fps_clock = pygame.time.Clock()

def blit_on(surface, texture_name):
        img = pygame.image.load(texture_name).convert_alpha()
        rect = img.get_rect()

        surface_h = surface.get_height()
        surface_w = surface.get_width()

        nrows = int(surface_h / rect.height) + 1
        ncols = int(surface_w / rect.width) + 1

        for y in range(nrows):
            for x in range(ncols):
                rect.topleft = ((x * rect.width), (y * rect.height))
                surface.blit(img, rect)


def game_quit(screen=None, menu=None, game=None, game_map=None):
        pygame.quit()
        sys.exit()


def swap_t_is_chosing_color(screen, menu, game_engine, game_map=None):
        menu.is_color_chosing = False;

def swap_c_is_chosing_color(screen, menu, game_engine, game_map=None):
        menu.is_color_chosing = True;

def add_balise(screen, menu, game_engine, game_map=None):
        coord = menu.text_input.input_string.split(";")
        color = menu.color_input.input_string
        if len(coord) != 2:
                menu.text_input.text_color = (255, 0, 0)
        elif (color != "red" and color != "blue" and color != "green"
              and color != "yellow" and color != "purple" and color != "orange" and color != "white"):
                menu.color_input.text_color = (255, 0, 0)
        else:
                try:
                        pos_x = int(coord[0])
                        pos_y = int(coord[1])

                        if pos_x < 0 or pos_x >= 900 or pos_y < 0 or pos_y >= 900:
                                menu.text_input.text_color = (255, 0, 0)
                                return
                except:
                        menu.text_input.text_color = (255, 0, 0)
                        return
                lu_beacon = LightBeacon(screen,
                                        '../assets/misc/light_beacon_' + color + '.png',
                                        '../assets/misc/light_beacon_' + color + '.png',
                                         (pos_x + 25, pos_y + 25),
                                        color)

                menu.color_input.text_color = (0, 0, 0)
                menu.text_input.text_color = (0, 0, 0)
                menu.time_passed = 0
                game_engine.balises.append(lu_beacon)

def add_more_balise(screen, menu, game_engine, game_map=None):
        coord = menu.text_input.input_string.split(";")
        color = menu.color_input.input_string
        if len(coord) != 2:
                menu.text_input.text_color = (255, 0, 0)
        elif (color != "red" and color != "blue" and color != "green"
              and color != "yellow" and color != "purple" and color != "orange" and color != "white"):
                menu.color_input.text_color = (255, 0, 0)
        else:
                try:
                        pos_x = int(coord[0])
                        pos_y = int(coord[1])

                        if pos_x < 0 or pos_x >= 900 or pos_y < 0 or pos_y >= 900:
                                menu.text_input.text_color = (255, 0, 0)
                                return
                except:
                        menu.text_input.text_color = (255, 0, 0)
                        return
                lu_beacon = LightBeacon(screen,
                                        '../assets/misc/light_beacon_' + color + '.png',
                                        '../assets/misc/light_beacon_' + color + '.png',
                                         (pos_x + 25, pos_y + 25),
                                        color)

                menu.color_input.text_color = (0, 0, 0)
                menu.text_input.text_color = (0, 0, 0)
                menu.time_passed = 0
                game_engine.balises_additionnals.append(lu_beacon)

def undo_balise(screen, menu, game_engine, game_map=None):
        if (len(game_engine.balises) > 0):
                game_engine.balises.pop()

def undo_more_balise(screen, menu, game_engine, game_map=None):
        if (len(game_engine.balises_additionnals) > 0):
                game_engine.balises_additionnals.pop()


def done_balise(screen, menu, game_engine, game_map=None):
        points = []
        for b in game_engine.balises:
                points.append(b.init_pos)

        if len(points) >= 3:
                pygame.draw.polygon(game_map.surface, (255, 255, 255), points)
                pygame.display.flip()
                game_map.mask_grass_on_durt()

                try:
                        with open(game_engine.outfile_json, "rt") as fp:
                                data = json.load(fp)
                except IOError:
                        data = {}

                data['balises'] = []

                for b in game_engine.balises:
                        str_pos = str(b.pos.x - 25 ) + ',' + str(b.pos.y - 25)
                        data['balises'].append({
                                'position' : str_pos,
                                'color' : b.color
                                })

                with open(game_engine.outfile_json, 'w+') as outfile:
                        json.dump(data, outfile)

                map_data = []
                with open('map.capture_init', 'r') as map_file:
                        map_data = list(map_file.read().replace('\n', ''))
                        for b in game_engine.balises:
                                map_data[900 * (b.pos.y - 25) + b.pos.x - 25] = 'B'
                        map_file.close()

                with open('map.capture_init', 'w+') as f:
                        map_str = ''.join(map_data)
                        f.write(map_str)
                        f.close()

                menu.time_passed = 0
                menu.button_afterdone()


def finish_balise(screen, menu, game_engine, game_map=None):
        data = {}

        with open(game_engine.outfile_json, "rt") as fp:
                data = json.load(fp)

        data['balises_additionnals'] = []

        for b in game_engine.balises_additionnals:
                str_pos = str(b.pos.x - 25 ) + ',' + str(b.pos.y - 25)
                data['balises_additionnals'].append({
                        'position' : str_pos,
                        'color' : b.color
                })

        with open(game_engine.outfile_json, 'wt') as outfile:
                json.dump(data, outfile)

        map_data = []
        with open('map.capture_init', 'r') as map_file:
                map_data = list(map_file.read().replace('\n', ''))
                for b in game_engine.balises_additionnals:
                        map_data[900 * (b.pos.y - 25) + b.pos.x - 25] = 'B'
                map_file.close()

        with open('map.capture_init', 'w+') as f:
                map_str = ''.join(map_data)
                f.write(map_str)
                f.close()

        pygame.quit()
        sys.exit()
