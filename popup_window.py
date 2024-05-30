import pygame
from button import Button

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)


class PopupWindow:
    def __init__(self, screen, message, width, height):
        self.screen = screen
        self.message = message
        self.font = pygame.font.Font("images/PIXY.ttf", height // 36)
        self.background_color = WHITE
        self.text_color = BLACK
        self.border_color = BLUE
        self.screen_width = width
        self.screen_height = height
        self.width = width / 5
        self.height = height / 5
        self.x = (width - self.width) // 2
        self.y = (height - self.height) // 2
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.visible = False
        self.restart_button = Button(self.x * 1.05, self.y * 1.38, width / 15, height / 25, "Restart", height * 6 // 250)
        # self.restart_button.image1 = pygame.transform.scale(pygame.image.load("images/sqt0.png"), (self.width, self.height))
        self.to_levels_button = Button(self.x * 1.28, self.y * 1.38, width / 15, height / 25, "To_levels", height * 6 // 250)
        self.close_button = Button(self.x + self.width - width / 60, self.y, width / 50, height / 25, "X",
                                       height * 10 // 250)

    def show(self):
        self.visible = True

    def hide(self):
        self.visible = False

    def draw(self, win, time, best_time):
        if self.visible:
            pygame.draw.rect(self.screen, self.border_color, self.rect)
            pygame.draw.rect(self.screen, self.background_color, self.rect.inflate(-10, -10))
            lines = self.message.split('\n')
            if win:
                lines.append('Your time: {:.2f} sec'.format(time))
            else:
                lines.append('Failed attempt')
            if best_time == "No results":
                lines.append(best_time)
            else:
                lines.append("Best time: {:.2f} sec".format(best_time))
            y_offset = self.y + self.screen_height // 40
            for line in lines:
                text_surface = self.font.render(line, True, self.text_color)
                text_rect = text_surface.get_rect(center=(self.screen_width // 2, y_offset))
                self.screen.blit(text_surface, text_rect)
                y_offset += self.screen_height // 36
            self.restart_button.process(self.screen)
            self.to_levels_button.process(self.screen)
            self.close_button.process(self.screen)
            if self.restart_button.is_pressed and self.restart_button.buttonRect.collidepoint(pygame.mouse.get_pos()):
                return 1
            if self.to_levels_button.is_pressed and self.to_levels_button.buttonRect.collidepoint(pygame.mouse.get_pos()):
                return 2
            if self.close_button.is_pressed and self.close_button.buttonRect.collidepoint(pygame.mouse.get_pos()):
                return 3
        return 0
