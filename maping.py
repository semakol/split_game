from settings import *

def map(X, Y):
    y = []
    x = []
    for i in range(0, Y+2):
        y.append(0)
    for t in range(0, X+2):
        x.append(y.copy())
    return x


def scan(text_map, text_map2):
    m = -1
    spawn_pos = 0, 0
    end_pos = 0, 0
    r = 0
    f = text_map.readlines()
    for j in range(0,len(f)):
        if  f[j] == '@\n':
            if f[j+1] == 'size =\n':
                size = (int(f[j+2]), int(f[j+3]))
            if f[j+1] == 'jump =\n':
                jump = int(f[j+2])
        if f[j] == '@s\n':
            r = j
            break
    world_map = map(size[0],size[1])
    for j in range(r+2,len(f)):
        m += 1
        for i, char in enumerate(f[j]):
            world_map[i][m] = char
            if char == 'S':
                spawn_pos = (i * TILE_x + TILE_x / 2, m * TILE_y + TILE_y / 2)
            if char == 'E':
                end_pos = (i,m)
    return world_map, spawn_pos, end_pos, jump, size

# def scan(text_map):
#     spawn_pos = 0,0
#     end_pos = 0,0
#     world_map = map()
#     for j, row in enumerate(text_map):
#         if row == '@\n':
#             for t, row2 in enumerate(text_map):
#                 if row2 == 'jump =\n':
#                     jump = int(text_map.readline(t + j + 1))
#                     return world_map, spawn_pos, end_pos, jump
#         for i, char in enumerate(row):
#             if char == '\n':



def next_level(number):
    text_level = open(f'levels/level_{number}', 'r')
    text_level2 = open(f'levels/level_{number}', 'r')
    s = scan(text_level, text_level2)
    text_level.close()
    text_level2.close()
    return s

