
from entity.player import Player
from draw import *
from maping import next_level
from defs import *
import pygame
level_number = 1


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
level = next_level(level_number)
textures = textures_load()
player = Player(level, textures)
pygame.mouse.set_visible(False)
keys = pygame.key.get_pressed()
time = 0
#buffer = buffer_draw(level[4],level[0][0])


# Цикл
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    time += 1
    # Ввод процесса (события)
    for event in pygame.event.get():
        # Проверяем выход из игры
        if event.type == pygame.QUIT:
            running = False
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
#        buffer = buffer_draw(level[4], level[0][0])
    mouse_pos = pygame.mouse.get_pos()
    player.movement()
    cam_pos = player.pos
    player.colision_player(level, level[4])
    player.event()

    screen.fill(BLACK)
    # draw_map(screen, level[0], cam_pos, textures)
    draw(screen, level[0], level[4], player, cam_pos, textures, level[5], level[6])
    pygame.draw.circle(screen, BLUE, standart_pos, 3 * SCALE_x)
    draw_text(screen, str(clock), 20, 0, 0 )
    draw_text(screen, str(time/80) + ' s', 20, 200, 0)
    pygame.draw.circle(screen, BLUE, mouse_pos, 3 * SCALE_x)
    pygame.display.flip()


pygame.quit()




# player.shoot(list=ListofBullet)
    # for l in ListofBullet:
    #     l.movement()
    #     i = l.collision()
    #     if i:
    #         ListofBullet.remove(l)