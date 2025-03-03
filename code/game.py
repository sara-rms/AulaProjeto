#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.level import Level
from code.menu import Menu
from const import WIN_WIDTH, WIN_HEIGTH, MENU_OPTION


class Game:
    def __init__(self):
        self.window = None
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGTH))
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()
            print(f"menu_return: {menu_return}")  # Adicionei para depuração
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, name='Level1', game_mode=menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
            else:
                pass

        # while True:
        #   menu = Menu(self.window)
        #  menu_return = menu.run()
        # if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:

        #    level = Level(self.window, name='Level1',game_mode=menu_return)

        #   level_return = level.run()
        # elif menu_return == MENU_OPTION[4]:
        #   pygame.quit()
        #  quit()
        # else:
        #    pass

    def run(self):
        pass


def game():
    return None
