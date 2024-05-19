import pygame


def onclick_function():
    print("pressed")


class Button:
    def __init__(self, x, y, width, height, button_text='Button', button_size=40):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.is_pressed = False
        self.fillColors = {
            'normal': '#1e90ff',
            'hover': '#0000cd',
            'pressed': '#000080',
        }
        self.image1 = pygame.transform.scale(pygame.image.load("images/rect833.png"), (self.width, self.height))
        self.image2 = pygame.transform.scale(pygame.image.load("images/rect834.png"), (self.width, self.height))
        self.image3 = pygame.transform.scale(pygame.image.load("images/rect835.png"), (self.width, self.height))

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = (pygame.font.Font("images/PIXY.ttf", button_size).
                           render(button_text, True, (20, 20, 20)))

    def process(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        self.buttonSurface.blit(self.image1, (0, 0))
        if self.buttonRect.collidepoint(mouse_pos):
            self.buttonSurface.blit(self.image2, (0, 0))
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.blit(self.image3, (0, 0))
                self.is_pressed = True
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)
