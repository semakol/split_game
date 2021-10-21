import math

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


def spawn_bullet(list, output):
    e = Bullet(output)
    list.append(e)
