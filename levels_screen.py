import pygame


def display(window, background_image):
    window.blit(background_image, (0, 0))


class LevelsScreen:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
