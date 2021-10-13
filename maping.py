from settings import *

text_map = [
    'WWWWWWWWWWWWWWWWWWWW',
    'W..................W',
    'WWWW...............W',
    'W..................W',
    'W.......WWW........W',
    'W.......WWW........W',
    'W..................W',
    'W....WWWWWWWWW.....W',
    'W..................W',
    'WWWWWWWWWWWWWWWWWWWW',
]

world_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i, j))


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