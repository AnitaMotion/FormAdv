import pygame

# Platform class
class Platform:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)

# Level class
class Level:
    def __init__(self):
        self.platforms = [
            Platform(50, 500, 200, 20),
            Platform(300, 400, 200, 20),
            Platform(550, 300, 200, 20),
        ]

    def draw(self, screen):
        for platform in self.platforms:
            platform.draw(screen)
