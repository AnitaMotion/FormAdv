import pygame

# Player class
class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 60)
        self.speed = 5
        self.jump_power = -15
        self.velocity_y = 0
        self.gravity = 0.8
        self.on_ground = False

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = self.jump_power
            self.on_ground = False

    def update(self, platforms):
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.velocity_y = 0
                    self.on_ground = True

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), self.rect)
