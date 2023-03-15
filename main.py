import pygame
from global_variables import *
from constants import *

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Jumping Lad')
    screen.fill((40, 155, 225))
    test_level = Level(TEST_LEVEL, TEST_LEVEL_BACKGROUND)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        test_level.draw_level(screen)
        pygame.display.flip()

pygame.quit()
