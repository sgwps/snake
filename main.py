import pygame
from game import Game


def main():
    pygame.init()
    g = Game()
    g.main_loop()


if __name__ == "__main__":
    main()
