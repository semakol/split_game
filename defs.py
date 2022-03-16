import math
import os
import sys

import pygame

from settings import *
from entity.bullet import Bullet


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
        images[imagename] = pygame.transform.scale(img, (int(TILE_x),int(TILE_y*img.get_size()[1]/img.get_size()[0])))
    return images

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

def event_check(event_link):
    for event in event_link:
        if event[1].active:
            event[0].open = True
        if not event[1].active:
            event[0].open = False