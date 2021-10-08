'''
import pygame
pygame.init()
from pygame import draw as dr

fps = 30
screen = pygame.displey.set_mode((300, 200))
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

clock = pygame.time.clock()
clock.tick(tick)

import pygame
from pygame.draw import *

'

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (255, 0, 255), (100, 100, 200, 200))
rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)
polygon(screen, (255, 255, 0), [(100,100), (200,50),
                               (300,100), (100,100)])
polygon(screen, (0, 0, 255), [(100,100), (200,50),
                               (300,100), (100,100)], 5)
circle(screen, (0, 255, 0), (200, 175), 50)
circle(screen, (255, 255, 255), (200, 175), 50, 5)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
'''
import pygame
from pygame.draw import *

pygame.init()

surf1 = pygame.Surface((100,100))

FPS = 30
screen = pygame.display.set_mode((400, 400))
'''
x1 = 100; y1 = 100
x2 = 300; y2 = 200
N = 10
color = (255, 255, 255)
rect(screen, color, (x1, y1, x2 - x1, y2 - y1), 2)
h = (x2 - x1) // (N + 1)
x = x1 + h
for i in range(N):
    line(screen, color, (x, y1), (x, y2))
    x += h
'''
rect(surf1, (255,255,255), (0, 0, 90, 90), 2)
pygame.transform.rotate(surf1, 45)
screen.blit(pygame.transform.rotate(surf1, 45), (100,100))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

