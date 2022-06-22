import random

import pygame
import sys
import time

# стартуем в файле модули пайгейм
pygame.init()

# размер окна
display_width = 800  # параметр ширины
display_height = 600  # параметр высоты

# окно игры
gameDisplay = pygame.display.set_mode((display_width, display_height))  # размер
pygame.display.set_caption("Don't crush my car, dude!")  # название
bg = pygame.image.load("images/space.jpg")


# цвета
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

# кадры в секунду
clock = pygame.time.Clock()

# игрок
carImg = pygame.image.load("images/car.png")  # картинка для игрока
carImg = pygame.transform.scale(carImg, (70, 80))  # задаем размер картинки, если большая
car_width = 73
carImg2 = pygame.image.load("images/car2.png")  # картинка для игрока
carImg2 = pygame.transform.scale(carImg2, (50, 80))  # задаем размер картинки, если большая
murder = pygame.transform.scale((pygame.image.load('images/14Um.gif')), (130,90))


# функция для появляющихся элементов на дороге
def things(thingx, thingy, thingw, thingh):
    gameDisplay.blit(murder, (thingx, thingy, thingw, thingh))


# отрисовка авто
def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def car2(w, h):
    gameDisplay.blit(carImg2, (w, h))


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))


# обработка текста
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


# вывод текста на экран
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def crash():
    message_display('GAME OVER!')

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(bg, (0, 0))
        largeText = pygame.font.Font('freesansbold.ttf', 80)
        TextSurf, TextRect = text_objects("Don't crash my car", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))


        button("GO!", 150, 450, 100, 50, green, bright_green, game_loop)


        pygame.display.update()
        clock.tick(15)


# функция для запуска игры
def game_loop():
    # размещение
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    w = (display_width * 0.25)
    h = (display_height * 0.8)

 # параметры для появления things

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 5
    thing_width = 100
    thing_height = 100

    # базовое значение для dodged
    dodged = 0

    x_change = 0
    w_change = 0  # позиция
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()
                sys.exit()

            # блок для обработки нажатия на клавиши
            if event.type == pygame.KEYDOWN:
                # если нажали на esc, то окно закр.
                if event.key == pygame.K_ESCAPE:
                    crashed = True
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_LEFT:
                    x_change = -5 - dodged

                if event.key == pygame.K_RIGHT:
                    x_change = 5 + dodged
                if event.key == pygame.K_a:
                    w_change = -5 - dodged

                if event.key == pygame.K_d:
                    w_change = 5 + dodged


            # условия для движения
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_d or event.key == pygame.K_a:
                    x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_d or event.key == pygame.K_a:
                    w_change = 0

        # смена позиции
        x += x_change
        w += w_change

        # фон
        gameDisplay.blit(bg, (0, 0))
        # вызов things
        things(thing_startx, thing_starty, thing_width, thing_height)
        thing_starty += thing_speed # скорость +

        # создаем машину
        car(x, y)
        car2(w, h)
        things_dodged(dodged)

        # задаем границы
        if x > display_width - car_width or x < 0:
            gameExit = True
            crash()
        if w > display_width - car_width or w < 0:
            gameExit = True
            crash()


        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width - 60)
            dodged += 1
            thing_speed += 1
            # thing_width += (dodged * 1.2)

        if y < thing_starty + thing_height:
            print('y crossover')

            if thing_startx < x < thing_startx + thing_width or thing_startx < x + car_width < thing_startx + thing_width:
                print('x crossover')
                crash()
            if thing_startx < w < thing_startx + thing_width or thing_startx < w + car_width < thing_startx + thing_width:
                print('x crossover')
                crash()

        # проверяем на обновления дисплея
        pygame.display.update()
        # кадры в секунду = 60
        clock.tick(60)


game_intro()
game_loop()
pygame.quit()
quit()