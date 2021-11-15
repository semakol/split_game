import pygame

from defs import angel_face,cords_face, spawn_bullet
from settings import *
from maping import world_map, spawn_pos, end_pos


class Player():

    def __init__(self):
        self.angel = 0
        self.x, self.y = spawn_pos
        self.speed = standart_speed
        self.pos_face = standart_pos
        self.size = 12
        self.dimension = 1
        self.stuck = 0
        self.end_pos = end_pos

    @property
    def pos(self):
        return self.x, self.y

    def angel(self):
        return self.angel

    def pos_face_move(self):
        self.angel = angel_face(standart_pos, pygame.mouse.get_pos())
        self.pos_face = cords_face(standart_pos, self.angel, SCALE_x, self.size)

    def movement(self):
        if self.stuck == 1: return
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed


    def colision_player(self):
        for i in range(0, 100):
            for t in range(0, 100):
                if world_map[i][t] == 'W':
                    x = i * TILE_x
                    y = t * TILE_y
                    event = 0
                elif world_map[i][t] == 'E':
                    x = i * TILE_x
                    y = t * TILE_y
                    event = 1
                if (x < self.x) \
                    & (x + TILE_x > self.x) \
                    & (y < self.y) \
                    & (y + TILE_y > self.y):
                    self.stuck = 1
                    return
                else: self.stuck = 0

                if      (x - self.size < self.x) \
                        & (x + TILE_x + self.size > self.x) \
                        & (y - self.size < self.y) \
                        & (y + TILE_y + self.size > self.y):
                    if event == 0:
                        if not ((x < self.x) & (x + TILE_x > self.x)):
                            if x + TILE_x / 2 > self.x:
                                self.x -= self.speed
                            if x + TILE_x / 2 < self.x:
                                self.x += self.speed

                        elif not ((y < self.y) & (y + TILE_y > self.y)):
                            if y + TILE_y / 2 > self.y:
                                self.y -= self.speed
                            if y + TILE_y / 2 < self.y:
                                self.y += self.speed
                    if event == 1:
                        self.x = 0
                        self.y = 0

    def shoot(self, list):
        key = pygame.mouse.get_pressed()
        if key[0]:
            spawn_bullet(list,self)

    def tp(self):
        if self.dimension == 1:
            self.x += 21 * TILE_x
            self.dimension = 2
            return
        if self.dimension == 2:
            self.x -= 21 * TILE_x
            self.dimension = 1
            return



