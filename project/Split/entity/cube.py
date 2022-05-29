import pygame

from settings import *

class Cube():

    def __init__(self, pos, laser=False, quant=False, jump=0):
        self.x , self.y = pos
        self.jump = jump
        self.in_player = 0
        self.laser = laser
        self.quant = quant
        self.image = 'cube'
        self.direction = 0
        self.images()
        self.dimension = 1
        self.cube_link = 0
        self.stuck = 0


    @property
    def pos(self):
        return self.x, self.y

    def up(self, cubes, dim):
        self.in_player = 1
        self.x , self.y = (-1,-1)
        self.stuck = False
        if self.cube_link != 0:
            cubes.remove(self.cube_link)
        self.cube_link = 0
        self.dimension = dim

    def down(self, pos, dim):
        self.in_player = 0
        self.x, self.y = pos
        self.dimension = dim

    def quants(self, cubes, jump, level):
        if not self.in_player:
            if not self.stuck:
                if self.quant:
                    if self.dimension == 1:
                        if self.cube_link == 0:
                            for door in level[5]:
                                if self.x + jump == door.pos[0] and self.y == door.pos[1]:
                                    self.stuck = True
                                    return
                            for cube in level[6]:
                                if self.x + jump == cube.pos[0] and self.y == cube.pos[1]:
                                    self.stuck = True
                                    return
                            for laser in level[9]:
                                if self.x + jump == laser.pos[0] and self.y == laser.pos[1]:
                                    self.stuck = True
                                    return
                            if level[0][1][int(self.x + jump)][int(self.y)] in stop_blocks:
                                self.stuck = True
                                return
                            cubes.append(Cube((self.x + jump, self.y), quant=True, laser=self.laser))
                            cube_2 = cubes[len(cubes) - 1]
                            cube_2.cube_link = self
                            cube_2.direction = self.direction
                            cube_2.images()
                            self.cube_link = cube_2
                    elif self.dimension == 2:
                        if self.cube_link == 0:
                            for door in level[5]:
                                if self.x - jump == door.pos[0] and self.y == door.pos[1]:
                                    self.stuck = True
                                    return
                            for cube in level[6]:
                                if self.x - jump == cube.pos[0] and self.y == cube.pos[1]:
                                    self.stuck = True
                                    return
                            for laser in level[9]:
                                if self.x - jump == laser.pos[0] and self.y == laser.pos[1]:
                                    self.stuck = True
                                    return
                            if level[0][1][int(self.x - jump)][int(self.y)] in stop_blocks:
                                self.stuck = True
                                return
                            cubes.append(Cube((self.x - jump, self.y), quant=True, laser=self.laser))
                            cube_2 = cubes[len(cubes) - 1]
                            cube_2.cube_link = self
                            cube_2.direction = self.direction
                            cube_2.images()
                            self.cube_link = cube_2

    def images(self):
        if self.laser:
            if self.quant:
                if self.direction == 0:
                    self.image = 'cube_laser_q_up'
                elif self.direction == 1:
                    self.image = 'cube_laser_q_down'
                elif self.direction == 2:
                    self.image = 'cube_laser_q_left'
                elif self.direction == 3:
                    self.image = 'cube_laser_q_right'
            else:
                if self.direction == 0:
                    self.image = 'cube_laser_up'
                elif self.direction == 1:
                    self.image = 'cube_laser_down'
                elif self.direction == 2:
                    self.image = 'cube_laser_left'
                elif self.direction == 3:
                    self.image = 'cube_laser_right'
        elif self.quant:
            self.image = 'cube_q'