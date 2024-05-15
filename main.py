import pygame
import random
from field import Field
import regiatrstion_screen
import levels_screen
import button

# Инициализация Pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)
background_image = pygame.image.load('1679767165_7fon-club-p-more-raznikh-tsvetov-21.jpg')
font = pygame.font.Font(None, 36)
text = font.render("Время: ", True, WHITE)

# Размеры окна
WINDOW_WIDTH = pygame.display.Info().current_w
WINDOW_HEIGHT = pygame.display.Info().current_h

# Положение надписи
text_rect = text.get_rect()
text_rect.center = (WINDOW_WIDTH // 2, 18)

field = Field(20, 20, 20)

# Смещение в центр
DELTA_WIDTH = WINDOW_WIDTH // 2 - field.get_game_width() // 2
DELTA_HEIGHT = WINDOW_HEIGHT // 2 - field.get_game_height() // 2

# Создание окна
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

registration_screen = regiatrstion_screen
levels_screen = levels_screen

objects = []
level_buttons = []

pygame.display.set_caption('Сапер')

objects.append(button.Button(WINDOW_WIDTH // 2 - 200, WINDOW_HEIGHT // 2 - 75, 400, 50, "Levels", 40))
objects.append(button.Button(WINDOW_WIDTH // 2 - 200, WINDOW_HEIGHT // 2 + 25, 400, 50, "Exit", 40))

level_buttons.append(button.Button(WINDOW_WIDTH // 2 - 200, WINDOW_HEIGHT // 2 - 175, 400, 50, "Square", 40))
level_buttons.append(button.Button(WINDOW_WIDTH // 2 - 200, WINDOW_HEIGHT // 2 - 75, 400, 50, "Rhombus", 40))
level_buttons.append(button.Button(WINDOW_WIDTH // 2 - 200, WINDOW_HEIGHT // 2 + 25, 400, 50, "To menu", 40))

exit_button = button.Button(0, 0, 200, 25, "Go back", 20)


# Функция для создания игрового поля
def create_grid():
    grid = [[0 for _ in range(field.get_cols())] for _ in range(field.get_rows())]
    for _ in range(field.get_nun_mines()):
        x, y = random.randint(0, field.get_cols() - 1), random.randint(0, field.get_rows() - 1)
        while grid[y][x] == -1:
            x, y = random.randint(0, field.get_cols() - 1), random.randint(0, field.get_rows() - 1)
        grid[y][x] = -1
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= x + i < field.get_cols() and 0 <= y + j < field.get_rows() and grid[y + j][x + i] != -1:
                    grid[y + j][x + i] += 1
    return grid


# Функция для отображения игрового поля
def draw_field():
    for y in range(field.get_rows()):
        for x in range(field.get_cols()):
            if not field.get_field_form(y + 1, x + 1):
                continue
            window.blit(field.get_field(x, y), (x * field.get_cell_size() +
                                                DELTA_WIDTH, y * field.get_cell_size() + DELTA_HEIGHT))


def game_process(i):
    clock = pygame.time.Clock()
    elapsed_time = 0
    running = False
    game_over = False
    win = False
    exit_button.is_pressed = False
    field.set_field_form(i)
    while not exit_button.is_pressed:
        for game_event in pygame.event.get():
            if game_event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
            elif game_event.type == pygame.MOUSEBUTTONDOWN and not game_over and not win:
                if game_event.button == 1:
                    x, y = ((game_event.pos[0] - DELTA_WIDTH) // field.get_cell_size(),
                            (game_event.pos[1] - DELTA_HEIGHT) // field.get_cell_size())
                    if (x >= field.get_rows() or x < 0) or (y >= field.get_cols() or y < 0):
                        continue
                    elif not field.is_generated:
                        running = True
                        field.generate_field(x, y)
                        game_over = field.open_cell(x, y)
                    else:
                        game_over = field.open_cell(x, y)
                    win = field.num_open_cell()
                elif game_event.button == 3:
                    x, y = ((game_event.pos[0] - DELTA_WIDTH) // field.get_cell_size(),
                            (game_event.pos[1] - DELTA_HEIGHT) // field.get_cell_size())
                    if (x >= field.get_rows() or x < 0) or (y >= field.get_cols() or y < 0):
                        continue
                    elif field.is_generated:
                        field.flagging(x, y)
        if running and not win and not game_over:
            elapsed_time += clock.get_time() / 1000
        window.blit(background_image, (0, 0))
        exit_button.process(window)
        text = font.render("Time: {:.2f} sec".format(elapsed_time), True, WHITE)
        window.blit(text, text_rect)
        draw_field()
        pygame.display.flip()
        clock.tick(60)
    field.__init__(20, 20, 20)


def choice_level():
    ex = False
    while not ex:
        levels_screen.display(window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or level_buttons[2].is_pressed:
                level_buttons[2].is_pressed = False
                ex = True
            else:
                for i in range(2):
                    if level_buttons[i].is_pressed:
                        game_process(i)
                        level_buttons[i].is_pressed = False

        for obj in level_buttons:
            obj.process(window)
        pygame.display.flip()


# Основной игровой цикл
def main():
    ex = False
    while not ex:
        registration_screen.display(window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or objects[1].is_pressed:
                ex = True
            elif objects[0].is_pressed:
                objects[0].is_pressed = False
                choice_level()

        for obj in objects:
            obj.process(window)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
