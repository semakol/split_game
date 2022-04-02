import pygame

from settings import *

class Cube():

    def __init__(self, pos, laser=False):
        self.x , self.y = pos
        self.in_player = 0
        self.laser = laser
        self.image = 'cube' if not laser else 'laser_cube'

    @property
    def pos(self):
        return self.x, self.y

    def up(self):
        self.in_player = 1
        self.x , self.y = (-1,-1)

    def down(self, pos):
        self.in_player = 0
        self.x, self.y = pos
