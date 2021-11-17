from settings import *

def map():
    y = []
    x = []
    for i in range(0, 100):
        y.append(0)
    for t in range(0, 100):
        x.append(y.copy())
    return x


def scan(text_map):
    n = 0
    spawn_pos = 0,0
    end_pos = 0,0
    world_map = map()
    for j, row in enumerate(text_map):
        if row == '@\n':
            for t, row2 in enumerate(text_map):
                if row2 == 'jump =\n':
                    jump = int(text_map.readline(t + j + 1))
                    return world_map, spawn_pos, end_pos, jump
        for i, char in enumerate(row):
            if char == '\n':
                break
            world_map[i][j] = char
            if char == 'S':
                spawn_pos = (i * TILE_x + TILE_x / 2, j * TILE_y + TILE_y / 2)
            if char == 'E':
                end_pos = (i,j)


def next_level(number):
    text_level = open(f'levels/level_{number}', 'r')
    s = scan(text_level)
    text_level.close()
    return s

