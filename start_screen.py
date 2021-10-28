import pygame

def draw(screen):
        screen.fill([173, 255, 47])
        font1 = pygame.font.SysFont("Pokemon GB.ttf", 100)
        font2 = pygame.font.SysFont("Pokemon GB.ttf", 40)
        text1 = font1.render("o_0   SNAKE   &_O", 0, [255,0,0])
        text2 = font2.render("!!! Press SPACE To Start !!!", 0, [255,0,0])
        
        screen.blit(text1, (90,180))
        screen.blit(text2, (215,320))

        # двойная буферизация (переворот)
        pygame.display.flip()
        # задержка
        pygame.time.delay(10)

