from settings import *


class Laser():
    def __init__(self, pos):
        self.x, self.y = pos
        self.lasers = []
        self.on = False
        self.event_id = 0
        self.direction = 'up'
        self.image = 'laser_up'
        self.first = True
        self.laser_image = 'laser_line_v_0', 'laser_line_v_1'
        self.stop = False

    @property
    def pos(self):
        return self.x, self.y

    def images(self):
        if self.direction == 'up':
            self.image = 'laser_up'
            self.laser_image = 'laser_line_v_0', 'laser_line_v_1'
        elif self.direction == 'down':
            self.image = 'laser_down'
            self.laser_image = 'laser_line_v_0', 'laser_line_v_1'
        elif self.direction == 'left':
            self.image = 'laser_left'
            self.laser_image = 'laser_line_g_0', 'laser_line_g_1'
        else:
            self.image = 'laser_right'
            self.laser_image = 'laser_line_g_0', 'laser_line_g_1'

    def laser_on(self, level):
        if self.on:
            if not self.stop:
                while True:
                    if self.first:
                        if self.direction == 'up':
                            if level[0][1][self.x][self.y - 1] in stop_blocks:
                                return
                            for door in level[5]:
                                if not door.on:
                                    if door.pos == (self.x,self.y - 1):
                                        self.lasers.append(((self.x, self.y - 1), 0))
                                        self.stop = True
                                        return
                            for cube in level[6]:
                                if cube.pos == (self.x, self.y - 1):
                                    self.lasers.append(((self.x, self.y - 1), 0))
                                    self.stop = True
                                    return
                            self.lasers.append(((self.x, self.y - 1), 0))
                            self.lasers.append(((self.x, self.y - 1), 1))
                        elif self.direction == 'down':
                            if level[0][1][self.x][self.y + 1] in stop_blocks:
                                return
                            for door in level[5]:
                                if not door.on:
                                    if door.pos == (self.x ,self.y + 1):
                                        self.lasers.append(((self.x , self.y + 1), 1))
                                        self.stop = True
                                        return
                            for cube in level[6]:
                                if cube.pos == (self.x, self.y + 1):
                                    self.lasers.append(((self.x, self.y + 1), 1))
                                    self.stop = True
                                    return
                            self.lasers.append(((self.x, self.y + 1), 0))
                            self.lasers.append(((self.x, self.y + 1), 1))
                        elif self.direction == 'left':
                            if level[0][1][self.x - 1][self.y] in stop_blocks:
                                return
                            for door in level[5]:
                                if not door.on:
                                    if door.pos == (self.x - 1,self.y):
                                        self.lasers.append(((self.x - 1, y), 1))
                                        self.stop = True
                                        return
                            for cube in level[6]:
                                if cube.pos == (self.x - 1, self.y):
                                    self.lasers.append(((self.x - 1, self.y), 1))
                                    self.stop = True
                                    return
                            self.lasers.append(((self.x - 1, self.y), 0))
                            self.lasers.append(((self.x - 1, self.y), 1))
                        elif self.direction == 'right':
                            if level[0][1][self.x + 1][self.y] in stop_blocks:
                                return
                            for door in level[5]:
                                if not door.on:
                                    if door.pos == (self.x + 1,self.y):
                                        self.lasers.append(((self.x + 1, y), 0))
                                        self.stop = True
                                        return
                            for cube in level[6]:
                                if cube.pos == (self.x + 1, self.y):
                                    self.lasers.append(((self.x + 1, self.y), 0))
                                    self.stop = True
                                    return
                            self.lasers.append(((self.x + 1, self.y), 0))
                            self.lasers.append(((self.x + 1, self.y), 1))
                        self.first = False
                    else:
                        x = self.lasers[len(self.lasers) - 1][0][0]
                        y = self.lasers[len(self.lasers) - 1][0][1]
                        if self.direction == 'up':
                            if level[0][1][x][y - 1] in stop_blocks:
                                return
                            for door in level[5]:
                                if not door.on:
                                    if door.pos == (self.x, self.y - 1):
                                        self.lasers.append(((self.x, y - 1), 0))
                                        self.stop = True
                                        return
                            for cube in level[6]:
                                if cube.pos == (self.x, self.y - 1):
                                    self.lasers.append(((self.x, self.y - 1), 0))
                                    self.stop = True
                                    return
                            self.lasers.append(((x, y - 1), 0))
                            self.lasers.append(((x, y - 1), 1))
                        elif self.direction == 'down':
                            if level[0][1][x][y + 1] in stop_blocks:
                                return
                            for door in level[5]:
                                if not door.on:
                                    if door.pos == (x,y + 1):
                                        self.lasers.append(((x, y + 1), 1))
                                        self.stop = True
                                        return
                            for cube in level[6]:
                                if cube.pos == (x, y + 1):
                                    self.lasers.append(((x, y + 1), 1))
                                    self.stop = True
                                    return
                            self.lasers.append(((x, y + 1), 0))
                            self.lasers.append(((x, y + 1), 1))
                        elif self.direction == 'left':
                            if level[0][1][x - 1][y] in stop_blocks:
                                return
                            for door in level[5]:
                                if not door.on:
                                    if door.pos == (x - 1,y):
                                        self.lasers.append(((x - 1, y), 1))
                                        self.stop = True
                                        return
                            for cube in level[6]:
                                if cube.pos == (x - 1, y):
                                    self.lasers.append(((x - 1, y), 1))
                                    self.stop = True
                                    return
                            self.lasers.append(((x - 1, y), 0))
                            self.lasers.append(((x - 1, y), 1))
                        elif self.direction == 'right':
                            if level[0][1][x + 1][y] in stop_blocks:
                                return
                            for door in level[5]:
                                if not door.on:
                                    if door.pos == (x + 1,y):
                                        self.lasers.append(((x + 1, y), 0))
                                        self.stop = True
                                        return
                            for cube in level[6]:
                                if cube.pos == (x + 1, y):
                                    self.lasers.append(((x + 1, y), 0))
                                    self.stop = True
                                    return
                            self.lasers.append(((x + 1, y), 0))
                            self.lasers.append(((x + 1, y), 1))
        else:
            self.lasers.clear()
            self.first = True
            self.stop = False
