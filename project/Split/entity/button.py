import pygame
from defs import update
from settings import *

class Button():

    def __init__(self, pos):
        self.x , self.y = pos
        self.active = 0
        self.image = 'button'
        self.event_id = 0

    @property
    def pos(self):
        return self.x, self.y

    def on(self):
        self.active = 1
        self.image = 'button_on'

    def off(self):
        self.active = 0
        self.image = 'button'

    def on_off(self, player_pos, level):
        active = self.active
        if self.x == player_pos[0] and self.y == player_pos[1]:
            self.on()
            if self.active != active:
                update(level)
            return
        for cube in level[6]:
            if self.x == cube.pos[0] and self.y == cube.pos[1]:
                self.on()
                if self.active != active:
                    update(level)
                return
        self.off()
        if self.active != active:
            update(level)

