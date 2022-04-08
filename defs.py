import math
import os
import sys
from draw import draw_text
import pygame

from settings import *


def angel_face(t1, t2):
    dx = t2[0] - t1[0]
    dy = t2[1] - t1[1]
    if dx == 0:
        dx = 1

    pre_angel = math.atan2(dy, dx)
    xt = math.cos(pre_angel)
    yt = math.sin(pre_angel)
    angel = xt, yt
    return angel


def cords_face(t1, angel, len, size):
    x = t1[0] + angel[0] * size * len
    y = t1[1] + angel[1] * size * len
    return (x, y)


def textures_load():
    path = 'resources/textures'
    filenames = [f for f in os.listdir(path) if f.endswith('.png')]
    images = {}
    for name in filenames:
        imagename = os.path.splitext(name)[0]
        img = pygame.image.load(os.path.join(path, name)).convert_alpha()
        if imagename in Cubes_textures:
            images[imagename] = pygame.transform.scale(img, (int(TILE_x), int(TILE_y)))
            continue
        images[imagename] = pygame.transform.scale(img, (
        int(TILE_x * img.get_size()[0] / 16), int(TILE_y * img.get_size()[1] / 16)))
    return images


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


def event_check(event_link, level):
    for event in event_link:
        if event[1].active:
            event[0].on = True if not event[0].reverse else False
        if not event[1].active:
            event[0].on = False if not event[0].reverse else True



def count_level():
    files = os.listdir(path="levels")
    files_on = []
    for i in range(0, len(files)):
        if 'level' in files[i]:
            files_on.append(files[i])
    return len(files_on)


def chop_frames(image):
    width, height = image.get_size()
    h, w = TILE_y, TILE_x

    row = 0
    frames = []
    # итерация по строкам
    for j in range(0, int(height / h)):
        # производим итерацию по элементам строки
        for i in range(0, int(width / w)):
            # добавляем  в список отдельные кадры
            frames.append(image.subsurface(pygame.Rect(i * w, row, w, h)))
        # смещаемся на высоту кадра, т.е. переходим на другую строку
        row += int(h)

    return frames


def message(screen, text):
    f1 = pygame.font.SysFont('arial', int(15 * SCALE_x))
    text1 = f1.render(text, True, WHITE)
    text2 = pygame.font.SysFont('Pixel Times', int(15 * SCALE_x)).render('<Пробел>', True, WHITE)
    x = standart_pos[0] - text1.get_size()[0] // 2
    y = standart_pos[1] - 100 * SCALE_y - text1.get_size()[1] // 2
    pygame.draw.rect(screen, BLACK, (
    x - 10 * SCALE_x, y - 10 * SCALE_y, text1.get_size()[0] + 20 * SCALE_y, text1.get_size()[1] + 20 * SCALE_y))
    screen.blit(text1, (x, y))
    pygame.draw.rect(screen, WHITE, (
    x - 10 * SCALE_x, y - 10 * SCALE_y, text1.get_size()[0] + 20 * SCALE_y, text1.get_size()[1] + 20 * SCALE_y), 1)
    pygame.draw.rect(screen, WHITE, (
        x - 8 * SCALE_x, y - 8 * SCALE_y, text1.get_size()[0] + 16 * SCALE_y, text1.get_size()[1] + 16 * SCALE_y), 1)
    screen.blit(text2, (x + text1.get_size()[0] - text2.get_size()[0], y + text1.get_size()[1] + text2.get_size()[1]))

def update(level):
    for laser in level[9]:
        laser.stop = False
        laser.lasers.clear()
        laser.first = True
    for receiver in level[11]:
        receiver.stop = False
