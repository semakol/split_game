

# Экран
WIDTH = 1280
HEIGHT = 720
FPS = 80
Half_HEIGHT = HEIGHT // 2
Half_WIDHT = WIDTH // 2
TILE_y = HEIGHT / 10
TILE_x = WIDTH / 20
SCALE_x = WIDTH / 1280
SCALE_y = HEIGHT / 720

# Начальные параметры
standart_pos = (Half_WIDHT, Half_HEIGHT)
standart_speed = 2

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

textures_id= [
    ['W', 'Wall', 1],
    ['.', 'floor', 2],
    ['E', 'floor_end', 2],
    ['S', 'floor_start', 2]
]