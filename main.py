import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.sey_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/тир.png")
pygame.display.set_icon(icon)

target_image = pygame.image.load("img/мишень.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(a: 0, b: 255), random.randint(a: 0, b: 255), random.randint(a: 0, b: 255))


running = True
while running:
    pass

pygame.quit()
