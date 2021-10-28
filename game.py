import pygame

import apple
import snake
import surface
import end_srceen


class Game:
    screen_size = [1080, 720]
    run = True
    g = True

    def __init__(self):
        self.screen = pygame.display.set_mode(Game.screen_size)
        snake.start()

    def event_getter(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game.run = False
            if event.type == pygame.KEYDOWN:
                snake.change_direction(event.key)


    def main_loop(self):
        while Game.run and Game.g:
            self.event_getter()
            snake.move()


            print(snake.pos)
            if not snake.check_border():
                Game.g = False
                end_srceen.draw(self.screen)
            else:
                surface.draw_surface(self.screen)
                snake.draw_snake(self.screen)
                apple.draw(self.screen)
            pygame.display.flip()
            pygame.time.delay(100)
        while Game.run:
            self.event_getter()
            end_srceen.draw(self.screen)
            pygame.display.flip()
            pygame.time.delay(100)

