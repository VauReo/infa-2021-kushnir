import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 2
screen = pygame.display.set_mode((1600, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
myfont = pygame.font.SysFont("Arial", 50)

def new_ball():
    '''рисует новый шарик '''
    x = randint(100, 1100)
    y = randint(100, 900)
    r = 50 
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    return x, y
pygame.display.update()
clock = pygame.time.Clock()
finished = False
score = 0
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
	elif event.type == pygame.KEYDOWN
	   (b) = event.pos
    a = new_ball()
    if (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2) <= 2500:
	circle(screen, black, a)
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()

