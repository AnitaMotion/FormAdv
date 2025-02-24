import pygame
from player import Player
from level import Level

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer Adventure")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize player and level
player = Player(100, HEIGHT - 100)
level = Level()

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys)
    
    level.draw(screen)
    player.draw(screen)
    player.update(level.platforms)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
