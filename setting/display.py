import pygame

display_width = 800  # параметр ширины
display_height = 600  # параметр высоты

# окно игры
gameDisplay = pygame.display.set_mode((display_width, display_height))  # размер
pygame.display.set_caption("Don't crush my car, dude!")  # название
bg = pygame.image.load("images/space.jpg")