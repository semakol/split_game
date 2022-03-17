from settings import *
import pygame
from draw import *
from defs import event_check
from maping import next_level

def main_game(player, time, level_number, level, screen, textures, clock, events):
    time += 1
    # Ввод процесса (события)
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.tp()
            if event.key == pygame.K_e:
                player.action(level)
            if event.key == pygame.K_r:
                if player.with_cube == 0:
                    player.cube_up(level)
                    continue
                else:
                    player.cube_down(level)
                    continue

    if player.end:
        level_number += 1
        level = next_level(level_number)
        player.__init__(level, textures)
        player.end = 0
        time = 0
    mouse_pos = pygame.mouse.get_pos()
    player.movement()
    player.images()
    cam_pos = player.pos
    player.colision_player(level, level[4])
    player.event()
    event_check(level[8])
    for button in level[7]:
        button.on_off(level[6], player.p_pos())
    for door in level[5]:
        door.open_check()

    screen.fill(BLACK)
    draw(screen, level[0], level[4], player, cam_pos, textures, level[5], level[6], level[7])
    pygame.draw.circle(screen, BLUE, standart_pos, 3 * SCALE_x)
    draw_text(screen, str(clock), 20, 0, 0 , RED)
    draw_text(screen, str(time/80) + ' s', 20, 200, 0, RED)
    pygame.draw.circle(screen, BLUE, mouse_pos, 3 * SCALE_x)
    pygame.display.flip()
#