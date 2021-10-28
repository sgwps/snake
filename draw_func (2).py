import pygame
def draw_snake(self, screen, surface_color):
    screen.fill(surface_color)
    for pos in self.dir:  # я так паонял, что dir это массив который отображает количество сегментов и соответсвенно длинну змеюки, но если не так то поменяй
        pygame.draw.rect(screen, self.snake_color, (pos[0], pos[1], 10, 10))  # на pos[0] pos[1] это координаты левого верхнего я не совсем понял совпадает ли у меня и у тебя это, если что опять же поменяй
