from settings import *
import pygame


def draw_map(screen, world_map):
    for x, y in world_map:
        pygame.draw.rect(screen, GREEN, (x * TILE_x, y * TILE_y, TILE_x, TILE_y), 2)
        # draw_text(screen, f'{x} {y}', 20, x*TILE_x+30, y*TILE_y)


def draw_player(screen, player, mouse_pos):
    pygame.draw.circle(screen, GREEN, player.pos, player.size * SCALE_x)
    pygame.draw.circle(screen, BLUE, mouse_pos, 3 * SCALE_x)
    pygame.draw.circle(screen, RED, player.pos_face, player.size / 2 * SCALE_x)


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def draw_bullet(surf, list):
    for l in list:
        pygame.draw.circle(surf, GREEN, l.pos, l.size)
