from entity.player import Player
from draw import *
from maping import next_level
from defs import *
import pygame
from menu_button import Menu_button
from scripts import level_scripts

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
pygame.display.set_icon(pygame.image.load('icon.png'))
clock = pygame.time.Clock()
textures = textures_load()
level_number = 1
scripts = [0]

menu_buttons = [
    Menu_button((POS_MENU[0], POS_MENU[1], POS_MENU[2], POS_MENU[3] // 3 - 5 * SCALE_y), 'start', 'Продолжить'),
    Menu_button((POS_MENU[0], POS_MENU[1] + POS_MENU[3] // 3, POS_MENU[2], POS_MENU[3] // 3 - 5 * SCALE_y), 'levels',
                'Уровни'),
    Menu_button((POS_MENU[0], POS_MENU[1] + POS_MENU[3] // 3 * 2, POS_MENU[2], POS_MENU[3] // 3 - 5 * SCALE_y), 'exit',
                'Выход')
]

Logo = pygame.transform.scale(pygame.image.load('resources/Logo.png'), (int(560 * SCALE_x) ,int(200 * SCALE_y))).convert_alpha()

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

level = next_level(level_number, textures)
player = Player(level, textures)
time = 0
timer_16 = 0
menu = True
game = False
level_menu = False
end = False
k_space = [False]
tp_script = [True]

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
                if menu_event == 'levels':
                    menu, level_menu = False, True
        screen.blit(Logo, (int(Half_WIDHT- Logo.get_size()[0] // 2), int((200 * SCALE_y) - Logo.get_size()[1] // 2)))
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
                level = next_level(level_button.event, textures)
                level_number = level_button.event
                player.__init__(level, textures)
                player.end = False
                time = 0
                scripts.clear()
                scripts.append(False)
                tp_script[0] = True
                level_menu, game = False, True
        pygame.display.flip()
    #

    if game:
        time += 1
        timer_16 += 1
        timer_16 = 0 if timer_16 >= 16 * FPS else timer_16
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    if tp_script[0]:
                        if player.tp_on:
                            player.time_reload = 0
                            player.tp()
                            player.tp_on = False
                if event.key == pygame.K_SPACE:
                    k_space[0] = True
                if event.key == pygame.K_e:
                    update(level)
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
            try:
                level = next_level(level_number, textures)
            except BaseException:
                game, end = False, True
            player.__init__(level, textures)
            player.end = 0
            update(level)
            time = 0
            player.tp_on = False
            scripts.clear()
            scripts.append(False)
            tp_script[0] = True
        mouse_pos = pygame.mouse.get_pos()
        player.movement()
        player.images(timer_16)
        cam_pos = player.pos
        player.colision_player(level, level[4])
        player.event()
        for cube in level[6]:
            cube.quants(level[6], level[3], level)
        for button in level[7]:
            button.on_off(player.p_pos, level)
        for door in level[5]:
            door.open_check(player.p_pos, level)
        event_check(level[8], level)
        for laser in level[9]:
            laser.laser_on(level)
        for receiver in level[11]:
            receiver.check_laser(level[9])

        screen.fill(BLACK)
        player.tp_reload()
        draw_2(screen, level[0], level[4], player, cam_pos, textures, level[5], level[6], level[7], level[9], level[10],
               (keys[pygame.K_LALT] or keys[pygame.K_RALT]), level[11])
        draw_reload(screen, player.time_reload, player.tp_reload_time)
        level_scripts(level_number, player, screen, level, scripts, k_space, tp_script)
        # draw_text(screen, str(clock), 20, 0, 0, RED)
        # draw_text(screen, str(time / FPS) + ' s', 20, 200, 0, RED)
        draw_text(screen, f'Уровень: {level_number}', int(20 * SCALE_x), 20, 0, WHITE)
        # pygame.draw.circle(screen, BLUE, mouse_pos, 3 * SCALE_x)
        pygame.display.flip()

    if end:
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    end, menu = False, True
        screen.fill((190, 190, 190))
        draw_text(screen, 'Спасибо, что поиграли в игру', int(50 * SCALE_x), Half_WIDHT, Half_HEIGHT, BLUE, True,
                  True)
        draw_text(screen, '"ESC"', int(30 * SCALE_x), Half_WIDHT, HEIGHT - int(100 * SCALE_y), BLUE, True, True)
        pygame.display.flip()
pygame.quit()
