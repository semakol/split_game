
class Mob():
    def __init__(self):
        self.angel = 0
        self.y, self.x = 1
        self.speed = 1
        self.pos_face = 1
        self.size = 12
        self.speedShoting = 0

    def movement(self):
        self.speed = 0