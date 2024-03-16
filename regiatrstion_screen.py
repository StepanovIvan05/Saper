import pygame


class RegistrationScreen:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)

    def display(self, window):
        window.fill((255, 255, 255))
