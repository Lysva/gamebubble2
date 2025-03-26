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