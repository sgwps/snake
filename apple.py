import pygame
import snake


position = ()
# image =...
color = [255, 0, 0]


def change_position():
    pass
    # randint, пока не выпадает на точку змеи

def check(self):
    if position == snake.pos[-1]:
        change_position()
        return True
    else:
        return False

def draw(self, screen, radius = 5):
    pygame.draw.circle(screen, color, self.positions, radius)
    #pass

