import pygame
from collections import deque
import apple
# from  draw_func import draw_snake
import surface

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
pos = deque()
direction = (1, 0)
speed = 5
size = 3
color = [255, 255, 255]


def start():
    global pos
    for i in range(size):
        pos.append((i, 0))


def move():
    global pos
    global size
    pos.append((pos[-1][0] + direction[0], pos[-1][1] + direction[1]))
    if not apple.check():
        pos.popleft()
    else:
        size += 1


def check_border():
    border_x, border_y = surface.get_borders()
    global pos
    print(pos[-1])
    if pos[-1][0] > 39 or pos[-1][0] < 0 or pos[-1][1] > 39 or pos[-1][1] < 0:
        return False
    return True


def change_direction(Input):
    global direction
    if Input == pygame.K_LEFT and direction != dirs[1]:
        direction = dirs[0]
    elif Input == pygame.K_RIGHT and direction != dirs[0]:
        direction = dirs[1]
    elif Input == pygame.K_UP and direction != dirs[3]:
        direction = dirs[2]
    elif Input == pygame.K_DOWN and direction != dirs[2]:
        direction = dirs[3]


def draw_snake(screen):
    global pos
    for i in pos:
        s, x, y = surface.get_params()
        print(190 + i[0] * s)
        pygame.draw.rect(screen, color, (x + i[0] * s, y + i[1] * s, s, s))
