import pygame.transform

from setting.display import gameDisplay

murder = pygame.transform.scale((pygame.image.load('images/14Um.gif')), (130, 90))

# функция для появляющихся элементов на дороге
def things(thingx, thingy, thingw, thingh):
    gameDisplay.blit(murder, (thingx, thingy, thingw, thingh))