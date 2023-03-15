import pygame
from global_variables import *

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Jumping Lad')
    screen.fill((40, 155, 225))
    pygame.display.flip()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

pygame.quit()
