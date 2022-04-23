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

    def check_laser(self, laser):
        if self.stop:
            return
        else:
            for l in laser:
                lasers = l.lasers
                if lasers == []:
                    self.active = False
                    self.stop = True
                    continue
                laser = lasers[len(lasers)-1], lasers[len(lasers)-2]
                if (((laser[0][0] == (self.x + 1, self.y)) and (laser[0][1] == 0) and (laser[0][2] == 2)) or
                        ((laser[1][0] == (self.x + 1, self.y)) and (laser[1][1] == 0) and (laser[1][2] == 2))):
                    self.active = True
                    self.stop = True
                    return
                elif ((laser[0][0] == (self.x - 1, self.y)) and (laser[0][1] == 1) and (laser[0][2] == 3)) or \
                        ((laser[1][0] == (self.x - 1, self.y)) and (laser[1][1] == 1) and (laser[1][2] == 3)):
                    self.active = True
                    self.stop = True
                    return
                elif ((laser[0][0] == (self.x, self.y + 1)) and (laser[0][1] == 1) and (laser[0][2] == 0)) or \
                        ((laser[1][0] == (self.x, self.y + 1)) and (laser[1][1] == 1) and (laser[1][2] == 0)):
                    self.active = True
                    self.stop = True
                    return
                elif ((laser[0][0] == (self.x, self.y - 1)) and (laser[0][1] == 0) and (laser[0][2] == 1)) or \
                        ((laser[1][0] == (self.x, self.y - 1)) and (laser[1][1] == 0) and (laser[1][2] == 1)):
                    self.active = True
                    self.stop = True
                    return
                else:
                    self.active = False
                    self.stop = True
