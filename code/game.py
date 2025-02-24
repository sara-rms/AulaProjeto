#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.menu import Menu
from const import WIN_WIDTH, WIN_HEIGTH


class Game:
    def __init__(self):
        self.window = None
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGTH))

    def run(self, ):


        while True:
            menu = Menu(self.window)
            menu.run()
            pass


def game():
    return None