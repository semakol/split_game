import pygame

from settings import *

class Doors():

    def __init__(self, pos, old_version):
        self.x , self.y = pos
        self.version = old_version
        self.direction = 0
        self.image = 'door_g'
        self.open = 0

    def directions(self):
        if self.direction:
            self.image = 'door_v'

    @property
    def pos(self):
        return self.x, self.y
