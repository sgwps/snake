import pygame
import snake
import surface
from random import randint


position = (6, 0)
# image =...
color = [255, 0, 0]


def change_position():
    global position
    position = (randint(0, 39), randint(0, 39))


def check():
    if position == snake.pos[-1]:
        change_position()
        return True
    else:
        return False


def draw(screen, radius = 5):
    s, x, y = surface.get_params()

    pygame.draw.circle(screen, color, (x + position[0] * s + 7, y + position[1] * s + 7), radius)