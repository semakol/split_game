import pygame
from settings import *
from draw import *



def set_cord(sur, player, mouse):
    scale = 50
    for i in range(0, (HEIGHT // scale)):
        pygame.draw.circle(sur, WHITE, (1, i * scale), 1)
        draw_text(sur, str(i * scale), 22, 15, i * scale - 3)
    for i in range(0, (WIDTH // scale)):
        pygame.draw.circle(sur, WHITE, (i * scale, 1), 1)
        draw_text(sur, str(i * scale), 22, i * scale, 10)
    pygame.draw.line(sur, WHITE, (player.pos[0], 0), (player.pos[0], HEIGHT), 1)
    pygame.draw.line(sur, WHITE, (0, player.pos[1]), (WIDTH, player.pos[1]), 1)
    pygame.draw.line(sur, BLUE, player.pos, mouse, 1)
    draw_text(sur, f'player {player.pos}', 22, 100, 30)
    draw_text(sur, f'mouse {mouse}', 22, 100, 50)
    draw_text(sur, f'angel {player.angel}', 22, 100, 70)

