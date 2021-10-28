import pygame

import snake
import surface
from snake import Snake
from surface import draw_back

class Game:
    screen_size = [1080, 720]
    run = True

    def __init__(self):
        self.screen = pygame.display.set_mode(Game.screen_size)
        self.snake = snake.Snake()

    def event_getter(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game.run = False
            if event.type == pygame.KEYDOWN:
                self.snake.change_direction(event.key)


    def main_loop(self):
        while Game.run:
            self.event_getter()
            self.snake.move()
            surface.draw_back(self.screen)
            self.snake.draw_snake(self.screen)
            pygame.display.flip()
            pygame.time.delay(100)


