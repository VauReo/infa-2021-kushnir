import pygame
from pygame.draw import *
from random import randint
import json

pygame.init()

pygame.mouse.set_visible(False)

FPS = 576
freq = 40  # procentage of second, that means period of balls appereance
screen_rect = (1200, 900)

screen = pygame.display.set_mode(screen_rect)
pygame.display.set_caption("BALLS 2")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, YELLOW, GREEN, MAGENTA]

font = pygame.font.SysFont("Arial Black", 25)

lose = font.render('U LOSE! ', 0, MAGENTA)
loserect = [0, 0, 0, 0]
click = font.render('[click to play againg]', 0, MAGENTA)
click_rect = [0, 0, 0, 0]
win = font.render('U SURVIVED!', 0, MAGENTA)
winrect = [0, 0, 0, 0]
pause_txt = font.render('Paused [press esc to resume]', 0, MAGENTA)
pause_rect = [0, 0, 0, 0]


def new_ball():
    """рисует новый шарик """
    x = randint(200, 1000)
    y = randint(200, 700)
    r = randint(10, 100)
    color = COLORS[randint(0, 3)]
    vx = 0
    vy = 0
    circle(screen, color, (x, y), r)
    circle(screen, BLACK, (x, y), r, 5)
    objs.append([(x, y), r, color, (vx, vy)])
    return [(x, y), r, color, (vx, vy)]


def rvec_sq(mp, xy):
    a = (mp[0] - xy[0]) ** 2 + (mp[1] - xy[1]) ** 2
    return a


def distance(mp, objs):
    """проверяет, куда попадает мышка и обновляет shoted"""
    hited = []
    for i in range(len(objs)):
        if rvec_sq(mp, objs[i][0]) <= objs[i][1] ** 2:
            hited.append(i)
    return hited


def prin(objs, mousepos, score):
    """рисует окно и выводит на экран все объекты"""
    rect(screen, BLUE, (100, 100, 1000, 700))
    for i in objs:
        circle(screen, i[2], i[0], i[1])
        circle(screen, BLACK, i[0], i[1], 5)
    for i in range(len(mousetrail) - 1):
        circle(screen, CYAN, mousetrail[i], 12)
    circle(screen, WHITE, mousepos, 17)
    circle(screen, BLUE, mousepos, 16)
    screen.blit(font.render('Score: ' + str(score), 1, GREEN), (0, 0))
    screen.blit(font.render(str(combo) + 'x', 0, GREEN), (0, 870))


score = 0
maxscore = 0
combo = 0
max_combo = 0
time_alive = 0
new_log = '1'
objs = []
mousetrail = []
hited = []
mp = (600, 450)

pygame.display.update()
clock = pygame.time.Clock()
tickcounter = 0
funny = True
get_ready = 0
pause = 0
lost = 0
won = 0


while funny:
    clock.tick(FPS)

    if len(mousetrail) > 5:
        del mousetrail[0]
        mousetrail.append(pygame.mouse.get_pos())
    else:
        mousetrail.append(pygame.mouse.get_pos())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            funny = False
        elif event.type == pygame.MOUSEMOTION:
            mp = event.pos
        elif event.type == pygame.MOUSEBUTTONDOWN:  # заменить на xz
            hited = distance(mp, objs)
            if pause == 0 and lost == 0:
                if len(hited) > 0:
                    combo += 1
                    score += combo
                    del objs[hited[-1]]
                else:
                    max_combo = max(combo, max_combo)
                    combo = 0
            elif lost == 1:
                print
                if lost == 1 and (mp[0] > 456 and mp[0] < 744) and (mp[1] > 336 and mp[1] < 372):
                    with open('all scores', 'r') as f:
                        reader = json.load(f)
                    reader[new_log] = [maxscore, max_combo, time_alive]
                    print(reader)
                    with open('all scores', 'w') as f:
                        json.dump(reader, f)

            #print(loserect, '\n', click_rect)
            print(mp)
            print(pygame.time.get_ticks())
            if lost == 1 and (mp[0] > 456 and mp[0] < 744) and (mp[1] > 336 and mp[1] < 372):
                lost = 0
                score = 0
                combo = 0
                print('wtf')
        elif event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == 27 and lost == 0:
                pause = (pause + 1) % 2
    if pause == 0 and lost == 0:
        tickcounter += 1
        if tickcounter == freq * FPS // 100:
            if pygame.time.get_ticks() > 60000:
                won = 1
            else:
                tickcounter = 0
                a = new_ball()
        prin(objs, pygame.mouse.get_pos(), score)
    elif lost == 1:
        prin([], pygame.mouse.get_pos(), score)
        loserect = screen.blit(lose, (544.5, 300))
        click_rect = screen.blit(click, (456, 336))

    elif pause == 1:
        prin([], pygame.mouse.get_pos(), score)
        pause_rect = screen.blit(pause_txt, (400, 300))

    if len(objs) > 7:
        lost = 1
        objs = []
        maxscore = score


    # new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
