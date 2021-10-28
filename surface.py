import pygame

x = 240
y = 60
s = 15

col1 = [170, 215, 81]
col2 = [162, 209, 73]


def get_params():
    return s, x, y


def get_borders():
    size = width, height = 1080, 720
    return size


def draw_surface(screen):
    col1 = [170, 215, 81]
    col2 = [162, 209, 73]
    pygame.draw.rect(screen, col1, (x, y, 600, 600))
    for i in range(1, 40, 2):
        for j in range(0, 40, 2):
            pygame.draw.rect(screen, col2, (x + (i * s), y + (j * s), s, s))
    for i in range(0, 40, 2):
        for j in range(1, 40, 2):
            pygame.draw.rect(screen, col2, (x + (i * s), y + (j * s), s, s))

