import pygame
from defs import update
from settings import *

class Doors():

    def __init__(self, pos, old_version, reverse=False):
        self.x , self.y = pos
        self.version = old_version
        self.direction = 0
        self.image = 'door_g_close'
        self.image2 = 'air'
        self.on = False
        self.event_id = 0
        self.can_open = True
        self.reverse = reverse

    def directions(self):
        if self.direction:
            self.image = 'door_v_close'

    @property
    def pos(self):
        return self.x, self.y

    def open_check(self, player_p_pos, level):
        on = self.on
        if self.can_open:
            if player_p_pos == self.pos:
                self.on = True
            else:
                self.on = False
        if self.on:
            if self.direction == 1:
                self.image = 'door_v_open_1'
                self.image2 = 'door_v_open_2'
            if self.direction == 0:
                self.image = 'door_g_open'
        elif not self.on:
            if self.direction == 1:
                self.image = 'door_v_close'
                self.image2 = 'air'
            if self.direction == 0:
                self.image = 'door_g_close'
        if on != self.on:
            update(level)



        # self.open = not self.open
        # if (self.image == 'door_g_open') or (self.image == 'door_g_close'):
        #     self.image = 'door_g_open' if self.image == 'door_g_close' else 'door_g_close'
        # if (self.image == 'door_v_open_1') or (self.image == 'door_v_close'):
        #     self.image = 'door_v_open_1' if self.image == 'door_v_close' else 'door_v_close'
        #     self.image2 = 'door_v_open_2' if self.image2 == 'air' else 'air'
