from cords import set_cord
from entity.player import Player
from draw import *
from maping import next_level
from defs import *
level_number = 1


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
level = next_level(level_number)
player = Player(level)
pygame.mouse.set_visible(False)
keys = pygame.key.get_pressed()
textures = textures_load()

# Цикл
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # Проверяем выход из игры
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.tp()
    if player.end:
        level_number += 1
        level = next_level(level_number)
        player.__init__(level)
        player.end = 0
    mouse_pos = pygame.mouse.get_pos()
    player.movement()
    cam_pos = player.pos
    player.colision_player(level[0])
    player.event()
    player.pos_face_move()

    screen.fill(BLACK)
    # set_cord(screen, player, mouse_pos)
    draw_second_plan(screen, level[0], cam_pos, textures)
    # draw_map(screen, level[0], cam_pos, textures)
    draw_player(screen, player, mouse_pos, textures)
    draw_first_plan(screen, level[0], cam_pos, textures, player)
    draw_text(screen, str(clock), 20, 0, 0 )
    pygame.display.flip()


pygame.quit()




# player.shoot(list=ListofBullet)
    # for l in ListofBullet:
    #     l.movement()
    #     i = l.collision()
    #     if i:
    #         ListofBullet.remove(l)