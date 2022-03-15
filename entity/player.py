import pygame

from settings import *


class Player():

    def __init__(self, level, textures):
        self.angel = 0
        self.x, self.y = level[1]
        self.speed = standart_speed * SCALE_x
        self.pos_face = standart_pos
        self.size = 5 * SCALE_x
        self.dimension = 1
        self.stuck = 0
        self.end_pos = level[2]
        self.end = 0
        self.jump = level[3]
        self.textures = textures
        self.image = self.textures['player_down']

    @property
    def pos(self):
        return self.x, self.y

    def movement(self):
        if self.stuck == 1: return
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= self.speed
            self.image = self.textures['player_up']
        if keys[pygame.K_s]:
            self.y += self.speed
            self.image = self.textures['player_down']
        if keys[pygame.K_d]:
            self.x += self.speed
            self.image = self.textures['player_right']
        if keys[pygame.K_a]:
            self.x -= self.speed
            self.image = self.textures['player_left']

    def colision_player(self, level, size):
        for i in range(0, size[0]):
            for t in range(0, size[1]):
                x = i * TILE_x
                y = t * TILE_y
                for world in level[0]:
                    if (world[i][t] == 'W') | (world[i][t] == 'w'):
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
        for door in level[5]:
            if not door.open:
                if door.direction == 0:
                    x = door.pos[0] * TILE_x
                    y = door.pos[1] * TILE_y + (TILE_y // 2.4)
                    if (x < self.x) \
                            & (x + TILE_x > self.x) \
                            & (y < self.y) \
                            & ((y + TILE_y // 5) > self.y):
                        self.stuck = 0
                        return
                    else:
                        self.stuck = 0
                        if (x - self.size < self.x) \
                                & (x + TILE_x + self.size > self.x) \
                                & (y - self.size < self.y) \
                                & (y + (TILE_y // 5) + self.size > self.y):
                            if not ((x < self.x) & (x + TILE_x > self.x)):
                                if x + TILE_x / 2 > self.x:
                                    self.x -= self.speed
                                if x + TILE_x / 2 < self.x:
                                    self.x += self.speed

                            elif not ((y < self.y) & (y + (TILE_y // 5) > self.y)):
                                if y + (TILE_y // 5) / 2 > self.y:
                                    self.y -= self.speed
                                if y + (TILE_y // 5) / 2 < self.y:
                                    self.y += self.speed

                if door.direction == 1:
                    x = door.pos[0] * TILE_x + (TILE_x // 2.4)
                    y = door.pos[1] * TILE_y
                    if (x < self.x) \
                            & ((x + TILE_x // 5) > self.x) \
                            & (y < self.y) \
                            & (y + TILE_y > self.y):
                        self.stuck = 1
                        return
                    else:
                        self.stuck = 0
                        if (x - self.size < self.x) \
                                & (x + TILE_x // 5 + self.size > self.x) \
                                & (y - self.size < self.y) \
                                & (y + TILE_y + self.size > self.y):
                            if not ((x < self.x) & (x + TILE_x // 5 > self.x)):
                                if x + TILE_x // 5 / 2 > self.x:
                                    self.x -= self.speed
                                if x + TILE_x // 5 / 2 < self.x:
                                    self.x += self.speed

                            elif not ((y < self.y) & (y + TILE_y > self.y)):
                                if y + TILE_y // 5 / 2 > self.y:
                                    self.y -= self.speed
                                if y + TILE_y // 5 / 2 < self.y:
                                    self.y += self.speed


    def tp(self):
        # /tp sema_kol school
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

    def action(self, level):
        x_p = self.x // TILE_x
        y_p = self.y // TILE_y
        for door in level[5]:
            if x_p == door.pos[0] and y_p == door.pos[1]:
                door.open_close()