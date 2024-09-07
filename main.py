import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")

# Загрузка иконки и изображений
icon = pygame.image.load("img/тир.png")
pygame.display.set_icon(icon)
target_image = pygame.image.load("img/мишень.png")

# Параметры мишени
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Цвет мишени
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Инициализация переменных
score = 0
font = pygame.font.Font(None, 36)  # Шрифт для отображения очков
running = True

# Основной игровой цикл
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            # Проверка попадания по мишени
            if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:
                score += 1  # Увеличиваем счет на 1
                # Перемещаем мишень на новое случайное место
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    # Очистка экрана
    screen.fill((255, 255, 255))  # Белый фон
    # Отображение мишени
    screen.blit(target_image, (target_x, target_y))

    # Отображение счета
    score_text = font.render(f"Очки: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
