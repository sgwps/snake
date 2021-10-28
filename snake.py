import pygame
from collections import deque
import apple
from  draw_func import draw_snake
import surface

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
pos = deque()
direction = (1, 0)
speed = 5
size = 3
color = [255, 255, 255]


def start():
    global pos
    for i in range(3):
        pos.append((i, 0))


def move():
    global pos
    global size
    pos.append((pos[-1][0] + dir[0], pos[-1][1] + dir[1]))
    if not apple.check(pos[-1]):
        pos.popleft()
    else:
        size += 1


def check_border():
    border_x, border_y = surface.get_borders()
    global pos
    if pos[-1][0] >= border_x or pos[-1][1] >= border_y:
        return False
    return True


def change_direction(self, input):
    global direction
    if input == pygame.K_LEFT and direction != dirs[1]:
        direction = dirs[0]
    elif input == pygame.K_RIGHT and direction != dirs[0]:
        direction = dirs[1]
    elif input == pygame.K_UP and direction != dirs[3]:
        direction = dirs[2]
    elif input == pygame.K_DOWN and direction != dirs[2]:
        direction = dirs[3]


def draw_snake(self, screen):
    global pos
    for i in pos:
        # get s, x, y parameters from surface file
        s = 17.5
        x = 190
        y = 10
        print(190 + i[0] * s)

        pygame.draw.rect(screen, self.color, (x + i[0] * s, y + i[1] * s, s, s))




