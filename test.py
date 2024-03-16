import pygame

class MenuScreen:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)

    def display(self, screen):
        screen.fill((255, 255, 255))
        text = self.font.render("Main Menu", True, (0, 0, 0))
        screen.blit(text, (200, 200))

class RegistrationScreen:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)

    def display(self, screen):
        screen.fill((255, 255, 255))
        text = self.font.render("Registration Screen", True, (0, 0, 0))
        screen.blit(text, (150, 200))

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    clock = pygame.time.Clock()

    menu_screen = MenuScreen()
    registration_screen = RegistrationScreen()
    current_screen = "menu"  # Начальный экран - меню

    running = True
    while running:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Переключение между экранами при нажатии пробела
                    if current_screen == "menu":
                        current_screen = "registration"
                    else:
                        current_screen = "menu"

        if current_screen == "menu":
            menu_screen.display(screen)
        elif current_screen == "registration":
            registration_screen.display(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
