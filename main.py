import json
import os
import pygame
from field import Field
import regiatrstion_screen
import levels_screen
import button

# Инициализация Pygame
pygame.init()

local_appdata_path = os.getenv('LOCALAPPDATA')
json_file_path = os.path.join(local_appdata_path, 'attempts.json')

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)
background_image = pygame.image.load('kandinsky-download-1716062799610.png')
font = pygame.font.Font("images/PIXY.ttf", 36)

# Размеры окна
WINDOW_WIDTH = pygame.display.Info().current_w
WINDOW_HEIGHT = pygame.display.Info().current_h
ROWS = 100
COLS = 100
NUM_MINES = 10
background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

field = Field(ROWS, COLS, NUM_MINES)


# Создание окна
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Сапер')

registration_screen = regiatrstion_screen
levels_screen = levels_screen

objects = []
level_buttons = []

objects.append(button.Button(WINDOW_WIDTH // 2 - 200, WINDOW_HEIGHT // 2 - 75, 400, 50, "Levels", 40))
objects.append(button.Button(WINDOW_WIDTH // 2 - 200, WINDOW_HEIGHT // 2 + 25, 400, 50, "Exit", 40))

level_buttons.append(button.Button(WINDOW_WIDTH // 2 - 200, WINDOW_HEIGHT // 2 - 275, 400, 50, "Square", 40))
level_buttons.append(button.Button(WINDOW_WIDTH // 2 - 200, WINDOW_HEIGHT // 2 - 175, 400, 50, "Rhombus", 40))
level_buttons.append(button.Button(WINDOW_WIDTH // 2 - 200, WINDOW_HEIGHT // 2 - 75, 400, 50, "Snake", 40))
level_buttons.append(button.Button(WINDOW_WIDTH // 2 - 200, WINDOW_HEIGHT // 2 + 25, 400, 50, "Circle", 40))
level_buttons.append(button.Button(WINDOW_WIDTH // 2 - 200, WINDOW_HEIGHT // 2 + 125, 400, 50, "Heart", 40))
level_buttons.append(button.Button(WINDOW_WIDTH // 2 - 200, WINDOW_HEIGHT // 2 + 225, 400, 50, "CBO", 40))
level_buttons.append(button.Button(WINDOW_WIDTH // 2 - 200, WINDOW_HEIGHT // 2 + 325, 400, 50, "To menu", 40))

exit_button = button.Button(0, 0, 200, 25, "Go back", 20)


def get_score(i, attempts):

    text = font.render("Best attempts:", True, WHITE)
    text_rect = text.get_rect()
    text_rect.center = (WINDOW_WIDTH - 100, 18)
    window.blit(text, text_rect)
    if get_level_name(i) not in attempts:
        text = font.render("No attempts", True, WHITE)
        text_rect = text.get_rect()
        text_rect.center = (WINDOW_WIDTH - 100, 54)
        window.blit(text, text_rect)
        return
    height = 18
    attempts[get_level_name(i)].sort()
    if len(attempts[get_level_name(i)]) > 10:
        attempts[get_level_name(i)] = attempts[get_level_name(i)][:10]
    for score in attempts[get_level_name(i)]:
        height += 36
        text = font.render("{:.2f} sec".format(score), True, WHITE)
        text_rect = text.get_rect()
        text_rect.center = (WINDOW_WIDTH - 100, height)
        window.blit(text, text_rect)
    return text


def get_level_name(i):
    if i == 0:
        return 'Square'
    elif i == 1:
        return 'Rhombus'
    elif i == 2:
        return 'Snake'
    elif i == 3:
        return 'Circle'
    elif i == 4:
        return 'Heart'
    elif i == 5:
        return 'CBO'


# Функция для загрузки данных из файла в словарь
def load_attempts():
    attempts = {}
    try:
        with open(json_file_path, "r") as file:
            data = file.read()
            if data:  # Проверяем, не пуст ли файл
                attempts = json.loads(data)
    except FileNotFoundError:
        pass  # Если файл не найден, возвращаем пустой словарь
    return attempts


# Функция для сохранения данных из словаря в файл
def save_attempts(attempts):
    with open(json_file_path, "w") as file:
        json.dump(attempts, file, indent=4)


# Функция для отображения игрового поля
def draw_field(delta_width, delta_height):
    for y in range(field.get_rows()):
        for x in range(field.get_cols()):
            if not field.get_field_form(y, x):
                continue
            window.blit(
                pygame.transform.scale(field.get_field(x, y),
                                       (field.get_cell_size(), field.get_cell_size())),
                (x * field.get_cell_size() + delta_width, y * field.get_cell_size() + delta_height))


def game_process(i, attempts):
    # Обновление размеров по форме
    field.set_rows(len(field.FIELD_FORM[i]))
    field.set_cols(len(field.FIELD_FORM[i][0]))
    field.set_field_form(i)

    # Смещение в центр
    delta_width = WINDOW_WIDTH // 2 - field.get_game_width() // 2
    delta_height = WINDOW_HEIGHT // 2 - field.get_game_height() // 2

    # Аннулирование времени
    clock = pygame.time.Clock()
    elapsed_time = 0

    # Установка начальных значений
    write_score = False
    running = False
    game_over = False
    win = False
    exit_button.is_pressed = False
    text = font.render("Time: 0.0", True, WHITE)

    # Игровой цикл
    while not exit_button.is_pressed:
        for game_event in pygame.event.get():
            if game_event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
            elif game_event.type == pygame.MOUSEBUTTONDOWN and not game_over and not win:
                if game_event.button == 1:
                    x, y = ((game_event.pos[0] - delta_width) // field.get_cell_size(),
                            (game_event.pos[1] - delta_height) // field.get_cell_size())
                    if (y >= field.get_rows() or y < 0) or (x >= field.get_cols() or x < 0):
                        continue
                    elif not field.is_generated:
                        running = True
                        field.generate_field(x, y)
                        game_over = field.open_cell(x, y)
                    else:
                        game_over = field.open_cell(x, y)
                    win = field.num_open_cell()
                elif game_event.button == 3:
                    x, y = ((game_event.pos[0] - delta_width) // field.get_cell_size(),
                            (game_event.pos[1] - delta_height) // field.get_cell_size())
                    if (y >= field.get_rows() or y < 0) or (x >= field.get_cols() or x < 0):
                        continue
                    elif field.is_generated:
                        field.flagging(x, y)
        if running and not win and not game_over:
            elapsed_time += clock.get_time() / 1000
            text = font.render("Time: {:.2f} sec".format(elapsed_time), True, WHITE)
        elif win:
            text = font.render("Win! Your time: {:.2f} sec".format(elapsed_time), True, WHITE)
            if not write_score:
                if get_level_name(i) not in attempts:
                    attempts[get_level_name(i)] = []
                attempts[get_level_name(i)].append(elapsed_time)
                save_attempts(attempts)
                write_score = True
        elif game_over:
            text = font.render("Loss", True, WHITE)
        window.blit(background_image, (0, 0))
        exit_button.process(window)
        # Положение надписи
        text_rect = text.get_rect()
        text_rect.center = (WINDOW_WIDTH // 2, 18)
        window.blit(text, text_rect)
        get_score(i, attempts)
        draw_field(delta_width, delta_height)
        pygame.display.flip()
        clock.tick(60)
    field.__init__(ROWS, COLS, NUM_MINES)


def choice_level(attempts):
    ex = False
    size = len(level_buttons) - 1
    while not ex:
        levels_screen.display(window, background_image)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or level_buttons[size].is_pressed:
                level_buttons[size].is_pressed = False
                ex = True
            else:
                for i in range(size):
                    if level_buttons[i].is_pressed:
                        game_process(i, attempts)
                        level_buttons[i].is_pressed = False

        for obj in level_buttons:
            obj.process(window)
        pygame.display.flip()


# Основной игровой цикл
def main():
    attempts = load_attempts()
    ex = False
    while not ex:
        registration_screen.display(window, background_image)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or objects[1].is_pressed:
                ex = True
            elif objects[0].is_pressed:
                objects[0].is_pressed = False
                choice_level(attempts)

        for obj in objects:
            obj.process(window)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
