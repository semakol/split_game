import pygame
import math
from settings import *
from entity.bullet import Bullet
import random


def angel_face(t1, t2):
    dx = t2[0] - t1[0]
    dy = t2[1] - t1[1]
    if dx == 0:
        dx = 1

    pre_angel = math.fabs(math.degrees(math.atan2(dy, dx)))
    if (pre_angel >= 90):
        pre_angel = pre_angel - 90
    xt = round((90 - pre_angel) / 90, 3)
    yt = round(pre_angel / 90, 3)
    if (dx > 0) & (dy >= 0):
        angel = xt, yt
    elif (dx < 0) & (dy > 0):
        angel = -yt, xt
    elif (dx > 0) & (dy < 0):
        angel = xt, -yt
    else:
        angel = -yt, -xt
    return angel


def cords_face(t1, angel, len, size):
    x = t1[0] + angel[0] * size * len
    y = t1[1] + angel[1] * size * len
    return (x, y)

def spawn_bullet(list,output):
    e = Bullet()
    e.setup(output=output)
    list.append(e)


