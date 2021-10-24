import pygame

class Game:
    screen_size = [1080, 720]
    run = True

    def __init__(self):
        self.screen = pygame.display.set_mode(Game.screen_size)


    def main_loop(self):
        while Game.run:
            raise NotImplementedError
