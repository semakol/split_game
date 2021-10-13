import pygame

from defs import angel_face,cords_face, spawn_bullet
from settings import *
from maping import world_map


class Player():

    def __init__(self):
        self.angel = 0
        self.y, self.x = standart_pos
        self.speed = standart_speed
        self.pos_face = standart_pos
        self.size = 40
        self.speedShoting = 0

    @property
    def pos(self):
        return self.x, self.y

    def angel(self):
        return self.angel

    def pos_face(self):
        return self.pos_face

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        self.angel = angel_face((self.x, self.y), pygame.mouse.get_pos())
        self.pos_face = cords_face((self.x, self.y), self.angel, SCALE_x, self.size)

    def colision_player(self):
        for i in world_map:
            x = i[0] * TILE_x
            y = i[1] * TILE_y
            if      (x - self.size < self.x) \
                    & (x + TILE_x + self.size > self.x) \
                    & (y - self.size < self.y) \
                    & (y + TILE_y + self.size > self.y):
                if not ((x < self.x) & (x + TILE_x > self.x)):
                    if x + TILE_x / 2 > self.x:
                        self.x -= self.speed
                    if x + TILE_x / 2 < self.x:
                        self.x += self.speed

                if not ((y < self.y) & (y + TILE_y > self.y)):
                    if y + TILE_y / 2 > self.y:
                        self.y -= self.speed
                    if y + TILE_y / 2 < self.y:
                        self.y += self.speed

    def shoot(self, list):
        key = pygame.mouse.get_pressed()
        if key[0]:
            spawn_bullet(list,self)



