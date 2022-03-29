from entity.player import Player
from draw import *
from maping import next_level
from defs import *
import pygame
from menu_button import Menu_button

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
textures = textures_load()
level_number = 1
scripts = [0,0,0,0,0,0]

menu_buttons = [
    Menu_button((POS_MENU[0], POS_MENU[1], POS_MENU[2], POS_MENU[3] // 4 - 5 * SCALE_y), 'start', 'Продолжить'),
    Menu_button((POS_MENU[0], POS_MENU[1] + POS_MENU[3] // 4, POS_MENU[2], POS_MENU[3] // 4 - 5 * SCALE_y), 'levels',
                'Уровни'),
    Menu_button((POS_MENU[0], POS_MENU[1] + POS_MENU[3] // 2, POS_MENU[2], POS_MENU[3] // 4 - 5 * SCALE_y), 'settings',
                'Настройки'),
    Menu_button((POS_MENU[0], POS_MENU[1] + POS_MENU[3] // 4 * 3, POS_MENU[2], POS_MENU[3] // 4 - 5 * SCALE_y), 'exit',
                'Выход')
]

settings_buttons = [
    Menu_button((POS_MENU[0], POS_MENU[1], POS_MENU[2], POS_MENU[3] // 4 - 5 * SCALE_y), 'start', 'Продолжить')
]

count_level = count_level()

level_buttons = []

for t in range(0, count_level // 5 + 1):
    for i in range(0, 5):
        if count_level > (t * 5 + i):
            level_buttons.append(
                Menu_button(((280 + 144 * i) * SCALE_x, (0 + 144 * t) * SCALE_y, 144 * SCALE_x, 144 * SCALE_y),
                            i + 1 + 5 * t, f'{i + 1 + 5 * t}'))

level = next_level(level_number)
player = Player(level, textures)
time = 0
timer_16 = 0
setting = False
menu = True
game = False
level_menu = False

running = True
while running:
    clock.tick(FPS)
    keys = pygame.key.get_pressed()
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
                if menu_event == 'settings':
                    menu, setting = False, True
                if menu_event == 'levels':
                    menu, level_menu = False, True
        pygame.display.flip()

    #

    if setting:
        screen.fill((100, 100, 100))
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    setting, menu = False, True
        for settings_button in settings_buttons:
            settings_button.draw(screen)
            setting_event = settings_button.click(mouse_pos, mouse_click)
        pygame.display.flip()

    #

    if level_menu:
        screen.fill((100, 100, 100))
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    level_menu, menu = False, True
        for level_button in level_buttons:
            level_button.draw(screen)
            level_event = level_button.click(mouse_pos, mouse_click)
            if level_event != 'none':
                level = next_level(level_button.event)
                level_number = level_button.event
                player.__init__(level, textures)
                player.end = 0
                time = 0
                level_menu, game = False, True
        pygame.display.flip()
    #

    if game:
        time += 1
        timer_16 += 1
        timer_16 = 0 if timer_16 >= 16 * FPS else timer_16
        # Ввод процесса (события)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player.tp_on:
                        player.time_reload = 0
                        player.tp()
                        player.tp_on = False
                if event.key == pygame.K_e:
                    player.action(level)
                if event.key == pygame.K_r:
                    if player.with_cube == 0:
                        player.cube_up(level)
                        continue
                    else:
                        player.cube_down(level)
                        continue
                if event.key == pygame.K_ESCAPE:
                    game, menu = False, True

        if player.end:
            level_number += 1
            level = next_level(level_number)
            player.__init__(level, textures)
            player.end = 0
            time = 0
            player.tp_on = False
        mouse_pos = pygame.mouse.get_pos()
        player.movement()
        player.images(timer_16)
        cam_pos = player.pos
        player.colision_player(level, level[4])
        player.event()
        event_check(level[8])
        for button in level[7]:
            button.on_off(level[6], player.p_pos)
        for door in level[5]:
            door.open_check()

        screen.fill(BLACK)
        player.tp_reload()
        draw(screen, level[0], level[4], player, cam_pos, textures, level[5], level[6], level[7])
        draw_reload(screen, player.time_reload, player.tp_reload_time)
        if level_number == 1:
            if not scripts[0]:
                if player.p_pos == (5, 5):
                    player.stuck = True
                    player.tp_on = False
                    draw_text(screen, 'Нажми "Пробел" чтобы продолжить.', 20, standart_pos[0], standart_pos[1], GREEN, True, True)
                    if keys[pygame.K_SPACE]:
                        player.stuck = False
                        player.tp_on = True
                        scripts[0] = 1

        elif level_number == 2:
            pass
        elif level_number == 3:
            pass
        elif level_number == 4:
            pass
        elif level_number == 5:
            pass
        draw_text(screen, str(clock), 20, 0, 0, RED)
        draw_text(screen, str(time / FPS) + ' s', 20, 200, 0, RED)
        draw_text(screen, f'level: {level_number}', 20, 300, 0, RED)
        pygame.draw.circle(screen, BLUE, mouse_pos, 3 * SCALE_x)
        pygame.display.flip()
pygame.quit()
