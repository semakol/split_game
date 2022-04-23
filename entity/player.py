import pygame
from numba import njit

from defs import chop_frames, update
from settings import *




class Player():

    def __init__(self, level, textures):
        self.angel = 0
        self.x, self.y = level[1]
        self.speed = standart_speed * SCALE_x
        self.pos_face = standart_pos
        self.size = 10 * SCALE_x
        self.dimension = 1
        self.dim_dir = level[12]
        self.direction = 'down'
        self.stuck = False
        self.end_pos = level[2]
        self.end = 0
        self.jump = level[3]
        self.frames = chop_frames(textures['player_animation'])
        self.with_cube = 0
        self.tp_on = True
        self.tp_reload_time = 0.8
        self.time_reload = 0
        self.in_walk = False
        self.image = self.frames[0]

    @property
    def pos(self):
        return self.x, self.y

    @property
    def p_pos(self):
        return int(self.x // TILE_x), int(self.y // TILE_y)

    def movement(self):
        if self.stuck == True: return
        keys = pygame.key.get_pressed()
        self.in_walk = False
        if keys[pygame.K_w]:
            self.y -= self.speed
            self.direction = 'up'
            self.in_walk = True
        if keys[pygame.K_s]:
            self.y += self.speed
            self.direction = 'down'
            self.in_walk = True
        if keys[pygame.K_d]:
            self.x += self.speed
            self.direction = 'right'
            self.in_walk = True
        if keys[pygame.K_a]:
            self.x -= self.speed
            self.direction = 'left'
            self.in_walk = True

    def images(self, time):
        if self.in_walk and (not self.stuck):
            if self.with_cube:
                if self.with_cube.laser:
                    if self.with_cube.quant:
                        timer = (time * 4 // FPS) % 4
                        if self.direction == 'up':
                            self.image = self.frames[111 + timer]
                        if self.direction == 'down':
                            self.image = self.frames[81 + timer]
                        if self.direction == 'left':
                            self.image = self.frames[91 + timer]
                        if self.direction == 'right':
                            self.image = self.frames[101 + timer]
                    else:
                        timer = (time * 4 // FPS) % 4
                        if self.direction == 'up':
                            self.image = self.frames[71 + timer]
                        if self.direction == 'down':
                            self.image = self.frames[41 + timer]
                        if self.direction == 'left':
                            self.image = self.frames[51 + timer]
                        if self.direction == 'right':
                            self.image = self.frames[61 + timer]
                elif self.with_cube.quant:
                    timer = (time * 4 // FPS) % 4
                    if self.direction == 'up':
                        self.image = self.frames[76 + timer]
                    if self.direction == 'down':
                        self.image = self.frames[46 + timer]
                    if self.direction == 'left':
                        self.image = self.frames[56 + timer]
                    if self.direction == 'right':
                        self.image = self.frames[66 + timer]
                else:
                    timer = (time * 4 // FPS) % 4
                    if self.direction == 'up':
                        self.image = self.frames[36 + timer]
                    if self.direction == 'down':
                        self.image = self.frames[6 + timer]
                    if self.direction == 'left':
                        self.image = self.frames[16 + timer]
                    if self.direction == 'right':
                        self.image = self.frames[26 + timer]
            else:
                timer = (time * 4 // FPS) % 4
                if self.direction == 'up':
                    self.image = self.frames[31 + timer]
                if self.direction == 'down':
                    self.image = self.frames[1 + timer]
                if self.direction == 'left':
                    self.image = self.frames[11 + timer]
                if self.direction == 'right':
                    self.image = self.frames[21 + timer]
        else:
            if self.with_cube:
                if self.with_cube.laser:
                    if self.with_cube.quant:
                        if self.direction == 'up':
                            self.image = self.frames[110]
                        if self.direction == 'down':
                            self.image = self.frames[80]
                        if self.direction == 'left':
                            self.image = self.frames[90]
                        if self.direction == 'right':
                            self.image = self.frames[100]
                    else:
                        if self.direction == 'up':
                            self.image = self.frames[70]
                        if self.direction == 'down':
                            self.image = self.frames[40]
                        if self.direction == 'left':
                            self.image = self.frames[50]
                        if self.direction == 'right':
                            self.image = self.frames[60]
                elif self.with_cube.quant:
                    if self.direction == 'up':
                        self.image = self.frames[75]
                    if self.direction == 'down':
                        self.image = self.frames[45]
                    if self.direction == 'left':
                        self.image = self.frames[55]
                    if self.direction == 'right':
                        self.image = self.frames[65]
                else:
                    if self.direction == 'up':
                        self.image = self.frames[35]
                    if self.direction == 'down':
                        self.image = self.frames[5]
                    if self.direction == 'left':
                        self.image = self.frames[15]
                    if self.direction == 'right':
                        self.image = self.frames[25]
            else:
                if self.direction == 'up':
                    self.image = self.frames[30]
                if self.direction == 'down':
                    self.image = self.frames[0]
                if self.direction == 'left':
                    self.image = self.frames[10]
                if self.direction == 'right':
                    self.image = self.frames[20]

    def colision_player(self, level, size):
        for i in range(0, size[0]):
            for t in range(0, size[1]):
                x = i * TILE_x
                y = t * TILE_y
                if not ((level[0][1][i][t] in stop_blocks) | (level[0][0][i][t] == ' ') | (level[0][1][i][t] == 'N')):
                    continue
                if (x < self.x) \
                        & (x + TILE_x > self.x) \
                        & (y < self.y) \
                        & (y + TILE_y > self.y):
                    self.stuck = True
                    return
                else:
                    self.stuck = False
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
            if not door.on:
                if door.direction == 0:
                    x = door.pos[0] * TILE_x
                    y = door.pos[1] * TILE_y + (TILE_y // 2.4)
                    if (x < self.x) \
                            & (x + TILE_x > self.x) \
                            & (y < self.y) \
                            & ((y + TILE_y // 5) > self.y):
                        self.stuck = True
                        return
                    else:
                        self.stuck = False
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
                        self.stuck = True
                        return
                    else:
                        self.stuck = False
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
        for laser in level[9]:
            if (laser.direction == 'right') | (laser.direction == 'left'):
                x = laser.pos[0] * TILE_x
                y = laser.pos[1] * TILE_y + (TILE_y // 2.2)
                if (x < self.x) \
                        & (x + TILE_x > self.x) \
                        & (y < self.y) \
                        & ((y + TILE_y // 5) > self.y):
                    self.stuck = True
                    return
                else:
                    self.stuck = False
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

            if (laser.direction == 'up') | (laser.direction == 'down'):
                x = laser.pos[0] * TILE_x + (TILE_x // 2.4)
                y = laser.pos[1] * TILE_y
                if (x < self.x) \
                        & ((x + TILE_x // 5) > self.x) \
                        & (y < self.y) \
                        & (y + TILE_y > self.y):
                    self.stuck = True
                    return
                else:
                    self.stuck = False
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
        if self.tp_on:
            if not self.dim_dir:
                if self.dimension == 1:
                    self.x += self.jump * TILE_x
                    self.dimension = 2
                    return
                if self.dimension == 2:
                    self.x -= self.jump * TILE_x
                    self.dimension = 1
                    return
            else:
                if self.dimension == 1:
                    self.y += self.jump * TILE_y
                    self.dimension = 2
                    return
                if self.dimension == 2:
                    self.y -= self.jump * TILE_y
                    self.dimension = 1
                    return

    def event(self):
        if self.p_pos == self.end_pos:
            self.end = 1

    # def action(self, level):
    #     x_p, y_p = self.p_pos
    #     for door in level[5]:
    #         if door.can_open:
    #             if x_p == door.pos[0] and y_p == door.pos[1]:
    #                 door.on = True if door.on == False else False
    #                 update(level)



    def cube_up(self, level):
        x_p , y_p = self.p_pos
        for cube in level[6]:
            if x_p == cube.pos[0] and y_p == cube.pos[1]:
                self.with_cube = cube
                cube.up(level[6], self.dimension)
                return

    def cube_down(self, level):
        x_p, y_p = self.p_pos
        for door in level[5]:
            if x_p == door.pos[0] and y_p == door.pos[1]:
                return
        for cube in level[6]:
            if x_p == cube.pos[0] and y_p == cube.pos[1]:
                return
        for laser in level[9]:
            if x_p == laser.pos[0] and y_p == laser.pos[1]:
                return
        if level[0][1][int(x_p)][int(y_p)] in stop_blocks:
            return
        if self.with_cube != 0:
            self.with_cube.down(self.p_pos, self.dimension)
            if self.direction == 'up':
                self.with_cube.direction = 0
            elif self.direction == 'down':
                self.with_cube.direction = 1
            elif self.direction == 'left':
                self.with_cube.direction = 2
            elif self.direction == 'right':
                self.with_cube.direction = 3
            self.with_cube.images()
            self.with_cube = 0

    def tp_reload(self):
        self.time_reload += 1
        if not self.tp_on:
            if self.time_reload >= self.tp_reload_time * FPS:
                self.tp_on = True


