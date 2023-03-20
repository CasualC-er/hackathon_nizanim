import pygame
from global_variables import *
from constants import *
from Class.Player import Player

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Jumping Lad')
    p = Player([])
    moves = False
    direct = 1
    run = True
    added_y = 1
    current_level = test_level
    starting_y = p.y
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
                    p.is_jumping = False

        if p.is_jumping:
            if starting_y - p.y <= BLOCK_SIZE*3:
                added_y += 1/added_y
                p.y -= added_y
            else:
                jumping = False
        if not p.is_jumping and not p.is_grounded:
            pass
        if moves:
            block_offset[0] += PLAYER_SPEED*direct
        screen.fill((40, 155, 225))
        current_level.draw_level(screen)
        p.draw(screen)
        pygame.display.flip()

pygame.quit()
