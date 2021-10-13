from maping import world_map
from settings import *
import random

class Bullet():
    def __init__(self):
        self.angel = [0,0]
        self.y, self.x = 10, 10
        self.speed = 6
        self.size = 2
        self.output = 2
        self.brust = 2
        self.brusting = random.random() * self.brust


    def setup(self, output):
        self.output = output
        self.x, self.y = output.pos
        self.angel = [output.angel[0], output.angel[1]]


    @property
    def pos(self):
        return self.x, self.y

    def angel(self):
        return self.angel

    def movement(self):
        self.x += self.speed * self.angel[0]
        self.y += self.speed * self.angel[1]

    def collision(self):
        for x,y in world_map:
            x1 = x * TILE_x
            y1 = y * TILE_y
            if      (x1 - self.size < self.x) \
                    & (x1 + TILE_x + self.size > self.x) \
                    & (y1 - self.size < self.y) \
                    & (y1 + TILE_y + self.size > self.y):
                return True
        return False

