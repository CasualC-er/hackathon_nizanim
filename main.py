import pygame
from global_variables import *
from constants import *
from Class.Player import Player

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Jumping Lad')
    p = Player(1, [])
    moves = False
    direct = 1
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    moves = True
                    direct = 1
                if event.key == pygame.K_RIGHT:
                    moves = True
                    direct = -1
                if event.key == pygame.K_SPACE:
                    p.is_grounded = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    moves = False
                elif event.key == pygame.K_RIGHT:
                    moves = False
                if event.key == pygame.K_SPACE:
                    p.is_grounded = False
        if moves:
            block_offset[0] += PLAYER_SPEED*direct
        screen.fill((40, 155, 225))
        test_level.draw_level(screen)
        pygame.display.flip()

pygame.quit()
