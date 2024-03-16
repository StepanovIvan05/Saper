import pygame
import random
from field import Field
import regiatrstion_screen
import button

# Инициализация Pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)
background_image = pygame.image.load('1679767165_7fon-club-p-more-raznikh-tsvetov-21.jpg')

# Размеры окна
WINDOW_WIDTH = pygame.display.Info().current_w
WINDOW_HEIGHT = pygame.display.Info().current_h

field = Field(20, 20, 40)

# Смещение в центр
DELTA_WIDTH = WINDOW_WIDTH // 2 - field.get_game_width() // 2
DELTA_HEIGHT = WINDOW_HEIGHT // 2 - field.get_game_height() // 2

# Создание окна
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
registration_screen = regiatrstion_screen.RegistrationScreen()
objects = []
pygame.display.set_caption('Сапер')
objects.append(button.Button(30, 30, 400, 50, "classic"))
objects.append(button.Button(30, 140, 400, 50, "treug"))


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
            window.blit(field.get_field(x, y), (x * field.get_cell_size() +
                                                DELTA_WIDTH, y * field.get_cell_size() + DELTA_HEIGHT))


# Основной игровой цикл
def main():
    while True:
        registration_screen.display(window)
        game_over = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif objects[0].is_pressed:
                while not game_over:
                    objects[0].is_pressed = False
                    for game_event in pygame.event.get():
                        if game_event.type == pygame.QUIT:
                            game_over = True
                            pygame.quit()
                        elif game_event.type == pygame.MOUSEBUTTONDOWN:
                            if game_event.button == 1:
                                x, y = ((game_event.pos[0] - DELTA_WIDTH) // field.get_cell_size(),
                                        (game_event.pos[1] - DELTA_HEIGHT) // field.get_cell_size())
                                if (x >= field.get_rows() or x < 0) or (y >= field.get_cols() or y < 0):
                                    continue
                                elif not field.is_generated:
                                    field.generate_field(x, y)
                                    game_over = field.open_cell(x, y)
                                else:
                                    game_over = field.open_cell(x, y)
                                if field.num_open_cell():
                                    print("win")
                                    game_over = True

                    window.blit(background_image, (0, 0))
                    draw_field()
                    pygame.display.flip()

        for object in objects:
            object.process(window)
        pygame.display.flip()


if __name__ == "__main__":
    main()
