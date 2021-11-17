from settings import *
import pygame


def draw_map(screen, world_map, cam_pos, textures):
    a_pos = (-cam_pos[0] + Half_WIDHT, -cam_pos[1] + Half_HEIGHT)
    for i in range(0, 100):
        for t in range(0, 100):
            for l in textures_id:
                if world_map[i][t] == l[0]:
                    image = pygame.transform.scale(textures.get(l[1]), (int(TILE_x), int(TILE_y)))
                    # draw_text(screen, f'{x} {y}', 20, x*TILE_x+30, y*TILE_y)
                    screen.blit(image, (i * TILE_x + a_pos[0], t * TILE_y + a_pos[1]))


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
