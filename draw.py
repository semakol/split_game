from settings import *
import pygame




def draw_map(screen, world_map, cam_pos):
    for x, y in world_map:
        a_pos = (-cam_pos[0]+Half_WIDHT,-cam_pos[1]+Half_HEIGHT)
        pygame.draw.rect(screen, GREEN, (x * TILE_x + a_pos[0], y * TILE_y + a_pos[1], TILE_x, TILE_y), 2)
        # draw_text(screen, f'{x} {y}', 20, x*TILE_x+30, y*TILE_y)


def draw_player(screen, player, mouse_pos):
    pygame.draw.circle(screen, GREEN, standart_pos, player.size * SCALE_x)
    pygame.draw.circle(screen, BLUE, mouse_pos, 3 * SCALE_x)
    pygame.draw.circle(screen, RED, player.pos_face, player.size / 2 * SCALE_x)


def draw_text(surf, text, size, x, y):
    f1 = pygame.font.SysFont('arial', size)
    text1 = f1.render(text, True, (250, 0, 0))
    surf.blit(text1, (x, y))

def draw_bullet(surf, list):
    for l in list:
        pygame.draw.circle(surf, GREEN, l.pos, l.size)
