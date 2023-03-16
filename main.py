import pygame
from global_variables import *
from constants import *

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Jumping Lad')

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    block_offset[0] += 30
                elif event.key == pygame.K_RIGHT:
                    block_offset[0] -= 30

        screen.fill((40, 155, 225))
        test_level.draw_level(screen)
        pygame.display.flip()

pygame.quit()
