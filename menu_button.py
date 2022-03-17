import pygame
from draw import draw_text
from settings import *

class Menu_button():
    def __init__(self, rectangle, event, title):
        self.rectangle = rectangle
        self.event = event
        self.title = title
        self.color = BLACK
        self.border = 3

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.rectangle[0], self.rectangle[1], self.rectangle[2], self.rectangle[3]), self.border)
        x = Half_WIDHT
        y = self.rectangle[1] + self.rectangle[3] // 2
        draw_text(screen, self.title, int(40 * SCALE_x), x, y, BLUE, True, True)

    def click(self, mouse_pos, mouse_click):
        if (self.rectangle[0] < mouse_pos[0]) \
            & (self.rectangle[0] + self.rectangle[2] > mouse_pos[0]) \
            & (self.rectangle[1] < mouse_pos[1]) \
            & (self.rectangle[1] + self.rectangle[3] > mouse_pos[1]):
            self.border = 0
            if mouse_click[0]:
                self.color = GREEN
                return self.event
            else:
                self.color = BLACK
        else:
            self.border = 3
            self.color = BLACK
            return 'none'


