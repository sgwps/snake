import pygame

def draw(screen):



    screen.fill([173, 255, 47])
    font = pygame.font.SysFont("Pokemon GB.ttf", 100)
    text = font.render("!!!  END !!!", 0, [255,0,0])

    screen.blit(text, (220,250))



