import pygame

from defs import angel_face, cords_face, spawn_bullet
from settings import *


class Player():

    def __init__(self, level):
        self.angel = 0
        self.x, self.y = level[1]
        self.speed = standart_speed
        self.pos_face = standart_pos
        self.size = 12
        self.dimension = 1
        self.stuck = 0
        self.end_pos = level[2]
        self.end = 0
        self.jump = level[3]

    @property
    def pos(self):
        return self.x, self.y

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

    def colision_player(self, world_map):
        for i in range(0, 100):
            for t in range(0, 100):
                x = i * TILE_x
                y = t * TILE_y
                if world_map[i][t] == 'W':
                    if (x < self.x) \
                            & (x + TILE_x > self.x) \
                            & (y < self.y) \
                            & (y + TILE_y > self.y):
                        self.stuck = 1
                        return
                    else:
                        self.stuck = 0
                        if (x - self.size < self.x) \
                                & (x + TILE_x + self.size > self.x) \
                                & (y - self.size < self.y) \
                                & (y + TILE_y + self.size > self.y):
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

    def shoot(self, list):
        key = pygame.mouse.get_pressed()
        if key[0]:
            spawn_bullet(list, self)

    def tp(self):
        if self.dimension == 1:
            self.x += self.jump * TILE_x
            self.dimension = 2
            return
        if self.dimension == 2:
            self.x -= self.jump * TILE_x
            self.dimension = 1
            return

    def event(self):
        x = self.end_pos[0] * TILE_x
        y = self.end_pos[1] * TILE_y
        if (x - self.size < self.x) \
                & (x + TILE_x + self.size > self.x) \
                & (y - self.size < self.y) \
                & (y + TILE_y + self.size > self.y):
            self.end = 1