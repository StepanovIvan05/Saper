import pygame
import random
from cell import Cell
from field import Field


class Game:
    def __init__(self, rows, cols, click_x, click_y):
        self.__rows = rows
        self.__cols = cols
        self.__click_x = click_x
        self.__click_y = click_y
