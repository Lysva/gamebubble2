import os
os.environ['PYGBAG_PWA'] = '0'  # Отключаем PWA-режим
import pygame
import asyncio

# Настройки игры
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Game")

# Цвета
BLUE = (0, 100, 255)
WHITE = (255, 255, 255)

async def main():
    # Создаём кнопку
    button = pygame.Rect(300, 300, 200, 50)
    
    running = True
    while running:
        # Заливаем фон
        screen.fill((0, 0, 50))  # Тёмно-синий
        
        # Рисуем кнопку
        pygame.draw.rect(screen, BLUE, button, border_radius=10)
        font = pygame.font.SysFont('Arial', 30)
        text = font.render("СТАРТ", True, WHITE)
        screen.blit(text, (350, 310))
        
        # Обрабатываем клики
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    print("Кнопка нажата!")
        
        pygame.display.flip()
        await asyncio.sleep(0)

pygame.init()
asyncio.run(main())
# В main.py
async def main():
    # ... инициализация ...
    
    start_button = pygame.Rect(300, 300, 200, 50)
    font = pygame.font.SysFont('Arial', 30)
    
    while True:
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Левая кнопка мыши
                    mouse_click = True
        
        # Отрисовка кнопки
        pygame.draw.rect(screen, (0, 100, 255), start_button)
        text = font.render("START", True, (255, 255, 255))
        screen.blit(text, (start_button.x + 50, start_button.y + 10))
        
        # Проверка клика
        if mouse_click and start_button.collidepoint(mouse_pos):
            print("Кнопка нажата!")  # Должно появиться в консоли
            # Здесь код запуска игры
        
        await asyncio.sleep(0)
