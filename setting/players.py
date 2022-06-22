import pygame
# машины
from setting.display import gameDisplay

carImg = pygame.image.load("images/car.png")  # картинка для игрока
carImg = pygame.transform.scale(carImg, (70, 80))  # задаем размер картинки, если большая
car_width = 73                                      # разиер машины
carImg2 = pygame.image.load("images/car2.png")  # картинка для игрока
carImg2 = pygame.transform.scale(carImg2, (50, 80))  # задаем размер картинки, если большая

# отрисовка авто
def car(x, y):
    gameDisplay.blit(carImg, (x, y))
def car2(w, h):
    gameDisplay.blit(carImg2, (w, h))