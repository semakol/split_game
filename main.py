
from entity.player import Player
from draw import *
from maping import next_level
from defs import *
import pygame
level_number = 1
from menu import game_menu
from menu_button import Menu_button
from game import main_game


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
textures = textures_load()
keys = pygame.key.get_pressed()

menu_buttons = [
    Menu_button((POS_MENU[0],POS_MENU[1],POS_MENU[2],POS_MENU[3]//4-5*SCALE_y), 'start', 'Продолжить'),
    Menu_button((POS_MENU[0],POS_MENU[1]+POS_MENU[3]//4,POS_MENU[2],POS_MENU[3]//4-5*SCALE_y), 'new_game', 'Новая игра'),
    Menu_button((POS_MENU[0],POS_MENU[1]+POS_MENU[3]//2,POS_MENU[2],POS_MENU[3]//4-5*SCALE_y), 'settings', 'Настройки'),
    Menu_button((POS_MENU[0],POS_MENU[1]+POS_MENU[3]//4*3,POS_MENU[2],POS_MENU[3]//4-5*SCALE_y), 'exit', 'Выход')
]

level = next_level(level_number)
player = Player(level, textures)
time = 0
menu = True
game = False

running = True
while running:
    clock.tick(FPS)
    time += 1
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    events = pygame.event.get()
    for event in events:
        # Проверяем выход из игры
        if event.type == pygame.QUIT:
            running = False

    #

    if menu:
        screen.fill((190, 190, 190))
        for menu_button in menu_buttons:
            menu_button.draw(screen)
            menu_event = menu_button.click(mouse_pos, mouse_click)
            if menu_event != 'none':
                if menu_event == 'exit':
                    pygame.event.post(pygame.event.Event(256))
                if menu_event == 'start':
                    game, menu = True, False
        pygame.display.flip()

    #

    if game:
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
        draw_text(screen, str(clock), 20, 0, 0, RED)
        draw_text(screen, str(time / 80) + ' s', 20, 200, 0, RED)
        pygame.draw.circle(screen, BLUE, mouse_pos, 3 * SCALE_x)
        pygame.display.flip()

