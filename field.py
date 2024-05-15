import pygame
import cell
import random


class Field:
    MINE = pygame.image.load("images/mine.gif")
    MINED = pygame.image.load("images/minered.gif")
    NOMINE = pygame.image.load("images/nomine.gif")
    EMPTY = pygame.image.load("images/sq0.gif")
    ONE = pygame.image.load("images/sq1.gif")
    TWO = pygame.image.load("images/sq2.gif")
    THREE = pygame.image.load("images/sq3.gif")
    FOUR = pygame.image.load("images/sq4.gif")
    FIFE = pygame.image.load("images/sq5.gif")
    SIX = pygame.image.load("images/sq6.gif")
    SEVEN = pygame.image.load("images/sq7.gif")
    EIGHT = pygame.image.load("images/sq8.gif")
    CLOSE = pygame.image.load("images/sqt0.gif")
    FLAGGED = pygame.image.load("images/sqt1.gif")
    FIELD_FORM = []
    FORM1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    FORM2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
             [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
             [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
             [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
             [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    FIELD_FORM.append(FORM1)
    FIELD_FORM.append(FORM2)

    def __init__(self, rows, cols, num_mines):
        self.__cell_size = 15
        self.__num_mines = num_mines
        self.__rows = rows
        self.__cols = cols
        self.__game_height = self.__cell_size * self.__rows
        self.__game_width = self.__cell_size * self.__cols
        self.__field = [[cell.Cell(self.__cell_size, self.CLOSE, self.FLAGGED, self.NOMINE) for _ in range(self.__cols)] for _ in
                        range(self.__rows)]
        self.__field_num = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__field_count = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.is_generated = False
        self.__field_form = self.FIELD_FORM[0]

    def get_field_form(self, i, j):
        return self.__field_form[i][j]

    def get_cell_size(self):
        return self.__cell_size

    def get_rows(self):
        return self.__rows

    def get_cols(self):
        return self.__cols

    def get_game_height(self):
        return self.__game_height

    def get_game_width(self):
        return self.__game_width

    def get_nun_mines(self):
        return self.__num_mines

    def get_field(self, x, y):
        return self.__field[y][x].get_cell_image()

    def set_field_form(self, i):
        self.__field_form = self.FIELD_FORM[i]

    def generate_field(self, click_x, click_y):
        mine = 0
        while self.__num_mines > mine:
            x, y = random.randint(0, self.__cols - 1), random.randint(0, self.__rows - 1)
            if (abs(x - click_x) > 1 or abs(y - click_y) > 1) and not self.__field[y][x].get_is_mine() and self.__field_form[y + 1][x + 1] == 1:
                self.__field_num[y][x] = 1
                self.__field[y][x].set_is_mine(True)
                self.__field[y][x].set_cell_image(self.MINE)
                mine += 1
        self.is_generated = True
        for i in range(self.__rows):
            for j in range(self.__cols):
                sum_mine = 0
                if self.__field_form[i + 1][j + 1] == 0:
                    continue
                if self.__field_num[i][j] == 1:
                    self.__field[i][j].set_cell_image(self.MINE)
                    continue
                for k in range(-1, 2):
                    for m in range(-1, 2):
                        if 0 <= i + k < self.__rows and 0 <= j + m < self.__cols:
                            sum_mine += self.__field_num[i + k][j + m]
                self.__field_count[i][j] = sum_mine
                self.add_sprites(sum_mine, i, j)

    def open_cell(self, x, y):
        if self.__field_form[y + 1][x + 1] == 0:
            return False
        if self.__field[y][x].get_is_fagged():
            return False
        elif self.__field_num[y][x] == 1:
            self.__field[y][x].set_is_bombed(True)
            self.__field[y][x].set_is_opened(True)
            self.__field[y][x].set_cell_image(self.MINED)
            self.open_game_over_cell()
            return True
        else:
            self.open_empty_cell(x, y)
            return False

    def flagging(self, x, y):
        if self.__field_form[y + 1][x + 1] == 0:
            return
        if not self.__field[y][x].get_is_fagged():
            self.__field[y][x].set_is_flagged(True)
        else:
            self.__field[y][x].set_is_flagged(False)

    def add_sprites(self, sum_mine, i, j):
        if sum_mine == 1:
            self.__field[i][j].set_cell_image(self.ONE)
        if sum_mine == 2:
            self.__field[i][j].set_cell_image(self.TWO)
        if sum_mine == 3:
            self.__field[i][j].set_cell_image(self.THREE)
        if sum_mine == 4:
            self.__field[i][j].set_cell_image(self.FOUR)
        if sum_mine == 5:
            self.__field[i][j].set_cell_image(self.FIFE)
        if sum_mine == 6:
            self.__field[i][j].set_cell_image(self.SIX)
        if sum_mine == 7:
            self.__field[i][j].set_cell_image(self.SEVEN)
        if sum_mine == 8:
            self.__field[i][j].set_cell_image(self.EIGHT)
        if sum_mine == 0:
            self.__field[i][j].set_cell_image(self.EMPTY)

    def open_empty_cell(self, x, y):
        if self.__field_form[y + 1][x + 1] == 0:
            return
        self.__field[y][x].set_is_opened(True)
        if self.__field_count[y][x] == 0:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (0 <= x + i < self.__rows and 0 <= y + j < self.__cols and
                            self.__field[y + j][x + i].get_is_opened() == False and
                            self.__field_form[y + j + 1][x + i + 1] == 1):
                        self.open_empty_cell(x + i, y + j)

    def num_open_cell(self):
        summ = 0
        all_cells = 0
        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.__field[i][j].get_is_opened():
                    summ += 1
                if self.__field_form[i + 1][j + 1]:
                    all_cells += 1
        # print(summ, self.__cols * self.__rows - self.__num_mines)
        if summ == (all_cells - self.__num_mines):
            return True
        else:
            return False

    def open_game_over_cell(self):
        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.__field_form[i + 1][j + 1] == 1:
                    self.__field[i][j].set_is_opened(True)

