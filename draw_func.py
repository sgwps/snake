import pygame
def draw_snake(self, screen, surface_color):
    screen.fill(surface_color)
    # for pos in self.dir:
    for i in range(self.len):
        # я так паонял, что dir это массив который отображает количество сегментов и соответсвенно длинну змеюки, но если не так то поменяй
        # Не совсем, это направления, а dir - текущие направление (поэтому он кортеж, дабы ничего не пошло по одному месту в случае чего)
        pygame.draw.rect(screen, self.color, (self.pos[0] - (i*self.dir[0]), self.pos[1] - (i*self.dir[1]), 1, 1))
        # на pos[0] pos[1] это координаты левого верхнего я не совсем понял совпадает ли у меня и у тебя это, если что опять же поменяй
        # Думаю, что должно быть так, так что да
