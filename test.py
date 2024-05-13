import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка экрана
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Маска изображения с смещением")

# Загрузка изображения
image = pygame.image.load("C:/Users/413/Downloads/hexagon-fill-svgrepo-com.svg").convert_alpha()

# Создание поверхности для рисования изображения с смещением
offset_surface = pygame.Surface((image.get_width(), image.get_height()), pygame.SRCALPHA)
offset_surface.fill((0, 0, 0, 0))  # Заполнение поверхности прозрачным цветом
offset_x, offset_y = 50, 50  # Смещение по оси X и Y

# Отрисовка изображения на поверхности с смещением
offset_surface.blit(image, (offset_x, offset_y))

# Создание маски изображения
mask = pygame.mask.from_surface(image)

# Смещение маски на основе смещения отрисовки изображения
mask_offset = pygame.mask.from_surface(offset_surface)

# Основной цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Проверка событий нажатия кнопки мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Получение координат мыши
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Проверка, попадает ли нажатие в маску изображения с смещением
            if mask_offset.get_at((mouse_x - offset_x, mouse_y - offset_y)):
                print("Нажатие на изображение!")

    # Очистка экрана
    screen.fill((255, 255, 255))
    # Отрисовка изображения с смещением
    screen.blit(offset_surface, (0, 0))

    # Обновление экрана
    pygame.display.flip()
