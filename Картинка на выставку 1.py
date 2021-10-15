import pygame
import math
from pygame.draw import *
from pygame.locals import *

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (0, 255, 255)
brown = (165, 42, 21)
lightbrown = (198, 50, 25)
black = (0,0,0)
sand = (255, 255, 0)
white = (255,255,255)
lightgray = (200, 200, 200)
peach = (255,127,80)
widtha = 600
heighta = 400


def draw_image(window):
    '''
    Рисует картинку с пляжиком и лодочками при помощи pygame.draw.
    При это библиотека pygame уже должна быть инициализирована
    '''
    
    draw_bg(screen, widtha, heighta)
    
    clouds(screen, widtha*12//100, heighta*16//100 , 20, 0.3, 0.3)
    clouds(screen, widtha*30//100, heighta*40//100 , 10, 0.3, 0.3)
    clouds(screen, widtha*48//100, heighta*8//100 , 30, 0.3, 0.3)
    
    sun(widtha-2*rs//3, 2*rs//3 , rs)
    
    boat(widtha*70//100, heighta*63//100, widtha*15//100, 1, 1)
    boat(widtha*35//100, heighta*52//100, widtha*5//100, 1, 1)

    umbre(widtha//7, heighta*9//10, 1.5)
    umbre(widtha*3//7, heighta*17//20, 1)
    
    
    
def draw_bg(window, width, height):
    rect(screen, cyan, (0, 0, width, height/2))
    rect(screen, blue, (0, height//2, width, height//4))
    rect(screen, sand, (0, height*3//4, width, height//4))
    
    
def clouds(screen, x, y, r, width, height):
    #ellipse(screen, white, rect(screen, red,(x, y, r*width, r*height)), 0)
    for i in range(3):
        circle(screen, white, ( x+r + r*i, y+2*r ), r)
        circle(screen, black, ( x+r + r*i, y+2*r ), r, 1)        
        circle(screen, white, ( x+int(1.5*r) + r*i, y+r ), r)
        circle(screen, black, ( x+int(1.5*r) + r*i, y+r ), r, 1)
    circle(screen,white, (x+4*r,y+2*r),r)
    circle(screen,black, (x+4*r,y+2*r),r,1)
    
def sun(x,y,r):
    circle(screen, sand, (x,y), r)

def boat(x,y,r,kx,ky):
    
    rect(screen, brown, (x-r,y-r//6, 2*r, r//3))
    rect(screen, black, (x-r,y-r//6, 2*r, r//3), 1)
    polygon(screen, brown, [(x+r,y-r//6), (x+9*r//5, y-r//6), (x+r, y+r//6)])
    polygon(screen, black, [(x+r,y-r//6), (x+9*r//5, y-r//6), (x+r, y+r//6)], 1)
    
    
    a = []
    for i in range(181):
        a.append((x-r*4//3+(r//3)*i//180, y-r//6 + (r//3) * ((180**2-(180-i)**2)**0.5)/180))
    a.append((x-r, y-r//6))
    
    
    polygon(screen, brown, a)
    polygon(screen, black, a, 1)

    
    rect(screen, black, (x-r//4, y-r//6 - r*3//2, r//10, r*3//2))
    circle(screen, black, (x + r + r//5, y - r//23),r//10)
    circle(screen, white, (x + r + r//5, y - r//23),r//12)
    polygon(screen, white, [(x - r//4 + r//10, y - r//6 - r*3//2),
                            (x + r*3//4      , y - r//6 - r*3//4),
                            (x - r//4 + r//10, y - r//6         ),
                            (x + 1*r//10     , y - r//6 - r*3//4)])
    polygon(screen, black, [(x - r//4 + r//10, y - r//6 - r*3//2),
                            (x + r*3//4      , y - r//6 - r*3//4),
                            (x - r//4 + r//10, y - r//6         ),
                            (x + 1*r//10     , y - r//6 - r*3//4)], 1)


def umbre(x, y, s):
    a=heighta*s

    ns = 1

    b = [(x - 16*a*ns//120, y - a//4   ), (x - a//120      , y - 6*a//20), (x + a//120      , y - 6*a//20), (x + 16*a*ns//120, y - a//4   )]           
    rect(screen, lightbrown, (x - a//120, y - a//4,
                              a//60     , a//4    ))
    polygon(screen, peach, b)
    for i in range(5):
        ns = i/4
        polygon(screen, black, [(x - a//120 - a*ns//8, y - a//4   ),
                                (x - a//120          , y - 6*a//20),
                                (x + a//120          , y - 6*a//20),
                                (x + a//120 + a*ns//8, y - a//4   )] , 1)
                             
    
rs = 60 #радиус солнца (кстати юзлес, надо заменить на долю от ширины картинки, но в 4:18 я лучше доделаю основную часть))) 
fps = 30
pygame.init()
screen = pygame.display.set_mode((widtha,heighta))
#surf = pygame.Surface((300, 100))

pygame.display.update()

clock = pygame.time.Clock()

clock.tick(fps)


'''
draw_bg(screen, widtha, heighta)
clouds(screen, widtha/5, heighta/8 , 50, 1, 1)
'''
#pygame.Surface.blit(screen, surf, (100,100))
draw_image(screen)
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
