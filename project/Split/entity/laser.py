from settings import *


class Laser():
    def __init__(self, pos, reverse=False):
        self.x, self.y = pos
        self.lasers = []
        self.on = False
        self.event_id = 0
        self.direction = 'up'
        self.image = 'laser_up'
        self.first = True
        self.laser_image = 'laser_line_v_0', 'laser_line_v_1', 'laser_line_g_0', 'laser_line_g_1'
        self.stop = False
        self.time = 0
        self.reverse = reverse

    @property
    def pos(self):
        return self.x, self.y

    def images(self):
        if self.direction == 'up':
            self.image = 'laser_up'
        elif self.direction == 'down':
            self.image = 'laser_down'
        elif self.direction == 'left':
            self.image = 'laser_left'
        else:
            self.image = 'laser_right'

    def laser_on(self, level):
        if self.on:
            if not self.stop:
                self.wh = True
                self.time = 0
                while self.wh and self.time < 100:
                    if self.first:
                        if self.direction == 'up':
                            self.laser_check(self.x, self.y, level, 0, -1, 0, 0)
                        elif self.direction == 'down':
                            self.laser_check(self.x, self.y, level, 0, 1, 1, 1)
                        elif self.direction == 'left':
                            self.laser_check(self.x, self.y, level, -1, 0, 1, 2)
                        elif self.direction == 'right':
                            self.laser_check(self.x, self.y, level, 1, 0, 0, 3)
                        self.first = False
                    else:
                        self.time += 1
                        x = self.lasers[len(self.lasers) - 1][0][0]
                        y = self.lasers[len(self.lasers) - 1][0][1]
                        if self.lasers[len(self.lasers) - 1][2] == 0:
                            self.laser_check(x, y, level, 0, -1, 0, 0)
                        elif self.lasers[len(self.lasers) - 1][2] == 1:
                            self.laser_check(x, y, level, 0, 1, 1, 1)
                        elif self.lasers[len(self.lasers) - 1][2] == 2:
                            self.laser_check(x, y, level, -1, 0, 1, 2)
                        elif self.lasers[len(self.lasers) - 1][2] == 3:
                            self.laser_check(x, y, level, 1, 0, 0, 3)

        else:
            self.lasers.clear()
            self.first = True
            self.stop = False

    def laser_check(self, x, y, level, x1, y1, d, d2):
        if level[0][1][x + x1][y + y1] in stop_blocks:
            self.wh = False
            self.stop = True
            return
        for door in level[5]:
            if not door.on:
                if door.pos == (x + x1, y + y1):
                    self.lasers.append(((x + x1, y + y1), d, d2))
                    self.stop = True
                    self.wh = False
                    return
        for cube in level[6]:
            if cube.pos == (x + x1, y + y1):
                self.lasers.append(((x + x1, y + y1), d, d2))
                if cube.laser:
                    if cube.quant:
                        if not cube.stuck:
                            if (cube.direction in [1, 2]):
                                self.lasers.append(((cube.cube_link.x, cube.cube_link.y), 0, cube.direction))
                            elif (cube.direction in [0, 3]):
                                self.lasers.append(((cube.cube_link.x, cube.cube_link.y), 1, cube.direction))
                            return
                    else:
                        if (cube.direction in [1, 2]):
                            self.lasers.append(((x + x1, y + y1), 0, cube.direction))
                        elif (cube.direction in [0, 3]):
                            self.lasers.append(((x + x1, y + y1), 1, cube.direction))
                        return
                self.stop = True
                self.wh = False
                return
        self.lasers.append(((x + x1, y + y1), 0, d2))
        self.lasers.append(((x + x1, y + y1), 1, d2))