import pygame

def draw():
    # инициализируем библиотеку PyGame
    pygame.init()
    pygame.font.init()

    window_size = width, height = 1080, 720
    screen = pygame.display.set_mode(window_size)

    run = True
    while run:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Отрисовка
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


if __name__ == "__main__":
    main()