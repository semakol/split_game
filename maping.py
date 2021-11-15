from settings import *

def map():
    y = []
    x = []
    for i in range(0, 100):
        y.append(0)
    for t in range(0, 100):
        x.append(y.copy())
    return x


text_map = [
    'WWWWWWWWWWWWWWWWWWWW.WWWWWWWWWWWWWWWWWWWW',
    'WS..W....W.........W.W.W....W......W....W',
    'WWWWWWWWWWWWWWWWWW.W.W.WWWWWWWWWWWWWWWW.W',
    'W............W.....W.W.....W............W',
    'W.WWWWWWWWWWWWWWWWWW.W.WWWWWWWWWWWWWWWWWW',
    'W.......W..........W.W.............W....W',
    'WWWWWWWWWWWWWWWWWW.W.W.WWWWWWWWWWWWWWWW.W',
    'W....W.......W.....W.W..W....W..........W',
    'W....W.......W.....W.WE.W....W..........W',
    'WWWWWWWWWWWWWWWWWWWW.WWWWWWWWWWWWWWWWWWWW',
]

world_map = map()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        world_map[i][j] = char
        if char == 'S':
            spawn_pos = (i * TILE_x + TILE_x/2, j * TILE_y + TILE_y/2)
        if char == 'E':
            end_pos = (i * TILE_x + TILE_x/2, j * TILE_y + TILE_y/2)


# text_map = [
#     'WWWWWWWWWWWWWWWWWWWW',
#     'W..................W',
#     'WWWW...............W',
#     'W..................W',
#     'W.......WWW........W',
#     'W.......WWW........W',
#     'W..................W',
#     'W....WWWWWWWWW.....W',
#     'W..................W',
#     'WWWWWWWWWWWWWWWWWWWW',
# ]

# text_map = [
#     '....................',
#     '....................',
#     '....................',
#     '....................',
#     '..........W.........',
#     '....................',
#     '....................',
#     '....................',
#     '....................',
#     '....................',
# ]