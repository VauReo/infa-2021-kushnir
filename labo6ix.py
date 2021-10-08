import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

pygame.display.update()
clock = pygame.time.Clock()
finished = False
keyspressed = []
while not finished:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            keypressed.append(

        elif event.type == pygame.KEYUP:
pygame.quit()
