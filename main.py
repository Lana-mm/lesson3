import pygame
import random
from PIL import Image

# Функция для загрузки GIF и разбивки на кадры
def load_gif(filename):
    img = Image.open(filename)
    frames = []
    try:
        while True:
            frame = img.copy()
            frame = frame.convert('RGBA')  # Конвертируем в RGBA
            frames.append(pygame.image.fromstring(frame.tobytes(), frame.size, frame.mode))
            img.seek(len(frames))  # Переходим к следующему кадру
    except EOFError:
        pass  # Достигнут конец анимации
    return frames

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

# Инициализация переменных
score = 0
font = pygame.font.Font(None, 36)
running = True

# Загрузка GIF
fireworks_frames = load_gif("img/салют1.gif")
fireworks_index = 0
fireworks_timer = 0
fireworks_duration = 10  # Длительность отображения фейерверка в кадрах

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
                # Проверяем, делится ли счет на 10
                if score % 10 == 0:
                    # Сбрасываем таймер для фейерверка
                    fireworks_index = 0
                    fireworks_timer = fireworks_duration

    # Очистка экрана
    screen.fill((255, 255, 255))  # Белый фон
    # Отображение мишени
    screen.blit(target_image, (target_x, target_y))
    # Отображение счета
    score_text = font.render(f"Очки: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    # Отображение фейерверка
    if fireworks_timer > 0 and fireworks_index < len(fireworks_frames):
        screen.blit(fireworks_frames[fireworks_index],
                    (SCREEN_WIDTH // 2 - fireworks_frames[fireworks_index].get_width() // 2,
                     SCREEN_HEIGHT // 2 - fireworks_frames[fireworks_index].get_height() // 2))
        fireworks_timer -= 1
        if fireworks_timer % (fireworks_duration // len(fireworks_frames)) == 0:
            fireworks_index += 1

    # Обновление экрана
    pygame.display.flip()
    pygame.time.delay(100)  # Задержка для снижения скорости цикла

# Завершение работы Pygame
pygame.quit()