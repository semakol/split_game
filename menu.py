from settings import *
import pygame
from draw import draw_text

def game_menu(screen, menu_buttons, mouse_pos, mouse_click):

    screen.fill((190,190,190))
    for menu_button in menu_buttons:
        menu_button.draw(screen)
        menu_event = menu_button.click(mouse_pos, mouse_click)
        if menu_event != 'none':
            if menu_event == 'exit':
                pygame.event.post(pygame.event.Event(256))
            if menu_event == 'start':
                pass
    pygame.display.flip()