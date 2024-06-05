import pygame
from button import Button

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)


class PopupWindow:
    def __init__(self, screen, message, width, height, real_width, real_height):
        self.screen = screen
        self.message = message
        self.font = pygame.font.Font("images/PIXY.ttf", int(height // 40))
        self.background_color = WHITE
        self.text_color = BLACK
        self.border_color = BLACK
        self.screen_width = real_width
        self.screen_height = height
        self.width = width / 5.1
        self.height = height / 2.5
        self.x = (real_width - self.width) // 2
        self.y = (real_height - self.height) // 2
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.visible = False
        self.background_image = pygame.image.load("images/pixphon5.png")
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))
        self.restart_button = Button(self.x + self.width * 0.14, self.y + self.height * 0.57, width / 7, height / 25, "Restart",
                                     int(height * 6 // 250))
        # self.restart_button.image1 = pygame.transform.scale(pygame.image.load("images/sqt0.png"), (self.width, self.height))
        self.to_levels_button = Button(self.x + self.width * 0.14, self.y + self.height * 0.7, width / 7, height / 25, "To levels",
                                       int(height * 6 // 250))
        self.close_button = Button(self.x + self.width * 0.14, self.y + self.height * 0.83, width / 7, height / 25, "open field",
                                   int(height * 6 // 250))

    def show(self):
        self.visible = True

    def hide(self):
        self.visible = False

    def draw(self, win, time, best_time):
        if self.visible:
            # Draw border
            pygame.draw.rect(self.screen, self.border_color, self.rect)

            # Draw background image
            self.screen.blit(self.background_image, self.rect.topleft)

            lines = self.message.split('\n')
            if win:
                lines.append('Your time: {:.2f} sec'.format(time))
            else:
                lines.append('Failed attempt')
            if best_time == "No results":
                lines.append(best_time)
            else:
                lines.append("Best time: {:.2f} sec".format(best_time))
            y_offset = self.y + self.screen_height // 15
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
            if self.to_levels_button.is_pressed and self.to_levels_button.buttonRect.collidepoint(
                    pygame.mouse.get_pos()):
                return 2
            if self.close_button.is_pressed and self.close_button.buttonRect.collidepoint(pygame.mouse.get_pos()):
                return 3
        return 0
