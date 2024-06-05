import json
import os

import pygame
from field import Field
import regiatrstion_screen
import levels_screen
import button
from popup_window import PopupWindow

# Инициализация Pygame
pygame.init()

local_appdata_path = os.getenv('LOCALAPPDATA')
json_file_path = os.path.join(local_appdata_path, 'attempts.json')

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)
background_image = pygame.image.load('photo_2024-05-25_01-03-41.png')
background_game_image = pygame.image.load('photo_2024-05-23_16-29-22.png')


# Размеры окна
REAL_WIDTH = WINDOW_WIDTH = pygame.display.Info().current_w
REAL_HEIGHT = WINDOW_HEIGHT = pygame.display.Info().current_h
ROWS = 100
COLS = 100
NUM_MINES = 1
background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
background_game_image = pygame.transform.scale(background_game_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

# Создание окна
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Сапер')

if WINDOW_HEIGHT < WINDOW_WIDTH / 1.77777:
    WINDOW_WIDTH = WINDOW_HEIGHT * 1.77777
else:
    WINDOW_HEIGHT = WINDOW_WIDTH / 1.77777
levels_button_width = WINDOW_WIDTH / 4.8
levels_button_height = WINDOW_HEIGHT / 15
font = pygame.font.Font("images/PIXY.ttf",  int(WINDOW_HEIGHT / 30))

field = Field(ROWS, COLS, NUM_MINES, WINDOW_HEIGHT // 30)

registration_screen = regiatrstion_screen
levels_screen = levels_screen

objects = []
level_buttons = []

objects.append(button.Button(REAL_WIDTH // 2 - levels_button_width / 2, REAL_HEIGHT // 2 - levels_button_height * 1.125, levels_button_width, levels_button_height, "Levels", int(levels_button_height * 0.8)))
objects.append(button.Button(REAL_WIDTH // 2 - levels_button_width / 2, REAL_HEIGHT // 2 + levels_button_height * 0.125, levels_button_width, levels_button_height, "Exit", int(levels_button_height * 0.8)))

level_buttons.append(button.Button(REAL_WIDTH // 2 - levels_button_width / 2, REAL_HEIGHT // 2 - levels_button_height * 3.75, levels_button_width, levels_button_height, "Square", int(levels_button_height * 0.8)))
level_buttons.append(button.Button(REAL_WIDTH // 2 - levels_button_width / 2, REAL_HEIGHT // 2 - levels_button_height * 2.5, levels_button_width, levels_button_height, "Rhombus", int(levels_button_height * 0.8)))
level_buttons.append(button.Button(REAL_WIDTH // 2 - levels_button_width / 2, REAL_HEIGHT // 2 - levels_button_height * 1.25, levels_button_width, levels_button_height, "Snake", int(levels_button_height * 0.8)))
level_buttons.append(button.Button(REAL_WIDTH // 2 - levels_button_width / 2, REAL_HEIGHT // 2 + levels_button_height * 0, levels_button_width, levels_button_height, "Circle", int(levels_button_height * 0.8)))
level_buttons.append(button.Button(REAL_WIDTH // 2 - levels_button_width / 2, REAL_HEIGHT // 2 + levels_button_height * 1.25, levels_button_width, levels_button_height, "Heart", int(levels_button_height * 0.8)))
level_buttons.append(button.Button(REAL_WIDTH // 2 - levels_button_width / 2, REAL_HEIGHT // 2 + levels_button_height * 2.5, levels_button_width, levels_button_height, "Z", int(levels_button_height * 0.8)))
level_buttons.append(button.Button(REAL_WIDTH // 2 - levels_button_width / 2, REAL_HEIGHT // 2 + levels_button_height * 3.75, levels_button_width, levels_button_height, "To menu", int(levels_button_height * 0.8)))

exit_button = button.Button(0, 0, levels_button_width / 2, levels_button_height / 2, "Go back", int(levels_button_height * 0.4))
restart_button = button.Button(0, levels_button_height * 1.25 / 2, levels_button_width / 2, levels_button_height / 2, "Restart", int(levels_button_height * 0.4))


def get_score(i, attempts):

    text = font.render("Best attempts:", True, WHITE)
    text_rect = text.get_rect()
    height = WINDOW_HEIGHT / 60
    text_rect.center = (REAL_WIDTH * 0.9, height)
    window.blit(text, text_rect)
    if get_level_name(i) not in attempts:
        text = font.render("No attempts", True, WHITE)
        text_rect = text.get_rect()
        text_rect.center = (REAL_WIDTH * 0.9, height * 3)
        window.blit(text, text_rect)
        return
    attempts[get_level_name(i)].sort()
    if len(attempts[get_level_name(i)]) > 5:
        attempts[get_level_name(i)] = attempts[get_level_name(i)][:5]
    for score in attempts[get_level_name(i)]:
        height += WINDOW_HEIGHT / 30
        text = font.render("{:.2f} sec".format(score), True, WHITE)
        text_rect = text.get_rect()
        text_rect.center = (REAL_WIDTH * 0.9, height)
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
    delta_width = REAL_WIDTH // 2 - field.get_game_width() // 2
    delta_height = REAL_HEIGHT // 2 - field.get_game_height() // 2

    # Аннулирование времени
    clock = pygame.time.Clock()
    elapsed_time = 0

    # Установка начальных значений
    write_score = False
    running = False
    game_over = False
    win = False
    exit_button.is_pressed = False
    restart_button.is_pressed = False
    text = font.render("Time: 0.0", True, WHITE)
    is_end = False
    popup = PopupWindow(window, "You win!", WINDOW_WIDTH, WINDOW_HEIGHT, REAL_WIDTH, REAL_HEIGHT)
    restart = 0
    ex = False
    is_pressed = False
    # Игровой цикл
    while not ex:
        for game_event in pygame.event.get():
            if game_event.type == pygame.QUIT:
                pygame.quit()
            if game_event.type == pygame.MOUSEBUTTONDOWN:
                is_pressed = True
            if game_event.type == pygame.MOUSEBUTTONUP and is_pressed:
                if get_level_name(i) in attempts:
                    restart = popup.draw(win, elapsed_time, attempts[get_level_name(i)][0])
                else:
                    restart = popup.draw(win, elapsed_time, "No results")
                if exit_button.is_pressed and exit_button.buttonRect.collidepoint(pygame.mouse.get_pos()):
                    ex = True
                if restart_button.is_pressed and restart_button.buttonRect.collidepoint(pygame.mouse.get_pos()):
                    restart = 1

                if not win and not game_over:
                    if game_event.button == 1:
                        x, y = (int((game_event.pos[0] - delta_width) / field.get_cell_size()),
                                int((game_event.pos[1] - delta_height) / field.get_cell_size()))
                        if field.get_field_form(y, x) == 0:
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
                    is_pressed = False
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
        if win and not is_end:
            popup.show()
            is_end = True
        window.blit(background_game_image, (0, 0))
        exit_button.process(window)
        restart_button.process(window)
        # Положение надписи
        text_rect = text.get_rect()
        text_rect.center = (REAL_WIDTH // 2, REAL_HEIGHT / 60)
        window.blit(text, text_rect)
        get_score(i, attempts)
        draw_field(delta_width, delta_height)
        if get_level_name(i) in attempts:
            popup.draw(win, elapsed_time, attempts[get_level_name(i)][0])
        else:
            popup.draw(win, elapsed_time, "No results")
        pygame.display.flip()
        clock.tick(60)
        if restart:
            if restart == 3:
                popup.visible = False
            else:
                break
    field.__init__(ROWS, COLS, NUM_MINES, WINDOW_HEIGHT // 30)
    if restart == 1:
        game_process(i, attempts)


def choice_level(attempts):
    ex = False
    size = len(level_buttons) - 1
    is_pressed = False
    while not ex:
        # levels_screen.display(window, background_image)
        window.blit(background_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level_buttons[size].is_pressed = False
                ex = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                is_pressed = True

            elif event.type == pygame.MOUSEBUTTONUP and is_pressed:
                if level_buttons[size].is_pressed and level_buttons[size].buttonRect.collidepoint(pygame.mouse.get_pos()):
                    level_buttons[size].is_pressed = False
                    ex = True
                for i in range(size):
                    if level_buttons[i].is_pressed and level_buttons[i].buttonRect.collidepoint(pygame.mouse.get_pos()):
                        game_process(i, attempts)
                        level_buttons[i].is_pressed = False

        for obj in level_buttons:
            obj.process(window)
        pygame.display.flip()


# Основной игровой цикл
def main():
    attempts = load_attempts()
    ex = False
    is_pressed = False
    try:
        while not ex:
            # registration_screen.display(window, background_image)
            window.blit(background_image, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ex = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    is_pressed = True
                if event.type == pygame.MOUSEBUTTONUP and is_pressed:
                    if objects[0].is_pressed and objects[0].buttonRect.collidepoint(pygame.mouse.get_pos()):
                        objects[0].is_pressed = False
                        choice_level(attempts)
                    if objects[1].is_pressed and objects[1].buttonRect.collidepoint(pygame.mouse.get_pos()):
                        ex = True

            for obj in objects:
                obj.process(window)
            pygame.display.flip()
    except:
        pygame.quit()

    pygame.quit()


if __name__ == "__main__":
    main()
