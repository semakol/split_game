import pygame

from settings import *

class Doors():

    def __init__(self, pos, old_version):
        self.x , self.y = pos
        self.version = old_version
        self.direction = 0

    @property
    def pos(self):
        return self.x, self.y