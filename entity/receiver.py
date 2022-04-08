from settings import *


class Receiver():
    def __init__(self, pos):
        self.x , self.y = pos
        self.event_id = 0
        self.active = False
        self.stop = False

    @property
    def pos(self):
        return self.x, self.y

    def check_laser(self, lasers):
        if self.stop:
            return
        else:
            if lasers == []:
                self.active = False
            for laser in lasers:
                if (laser[0] == (self.x + 1, self.y)) and (laser[1] == 0):
                    self.active = True
                    self.stop = True
                    return
                if (laser[0] == (self.x - 1, self.y)) and (laser[1] == 1):
                    self.active = True
                    self.stop = True
                    return
                if (laser[0] == (self.x, self.y + 1)) and (laser[1] == 0):
                    self.active = True
                    self.stop = True
                    return
                if (laser[0] == (self.x, self.y - 1)) and (laser[1] == 1):
                    self.active = True
                    self.stop = True
                    return
                else:
                    self.active = False
                    self.stop = True
