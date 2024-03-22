import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Тир")

icon = pygame.image.load("img/тир.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 85
target_height = 85

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 225), random.randint(0, 225), random.randint(0, 225))

# Initialize the font module
pygame.font.init()
# Choose a font and size
font = pygame.font.Font(None, 36)

# Initialize the shot counter
shots = 0

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            shots += 1  # Increment the shot counter
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    # Render the shot counter
    shots_text = font.render(f"Shots: {shots}", True, (255, 255, 255))
    screen.blit(shots_text, (10, 10))

    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

pygame.quit()