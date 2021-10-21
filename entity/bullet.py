from maping import world_map
from settings import *
import random

class Bullet():
    def __init__(self, output):
        self.angel = [output.angel[0], output.angel[1]]
        self.x, self.y = output.pos
        self.speed = 5
        self.size = 2
        self.output = output
        self.brust = 2
        self.brusting = random.random() * self.brust

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

