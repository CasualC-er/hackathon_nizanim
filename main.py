import pygame
from global_variables import *
from constants import *
from Class.Player import Player


def player_rect_by_position_collides_with(pos: tuple[int, int], level: Level):
    return pygame.rect.Rect(pos[0], pos[1], PLAYER_BOX_WIDTH, PLAYER_BOX_HEIGHT).collidelist(level.collider_list) != -1


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
                    if not player_rect_by_position_collides_with((PLAYER_X - PLAYER_SPEED, p.y), current_level):
                        moves = True
                        direct = 1
                    else:
                        moves = False
                if event.key == pygame.K_RIGHT:
                    if not player_rect_by_position_collides_with((PLAYER_X + PLAYER_SPEED, p.y), current_level):
                        moves = True
                        direct = -1
                    else:
                        moves = False
                if event.key == pygame.K_SPACE:
                    if player_rect_by_position_collides_with((PLAYER_X, p.y + 1), current_level):
                        p.is_jumping = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    moves = False
                elif event.key == pygame.K_RIGHT:
                    moves = False
                if event.key == pygame.K_SPACE:
                    p.is_jumping = False

        if p.is_jumping:
            if starting_y - p.y <= BLOCK_SIZE * 3 \
                    and not player_rect_by_position_collides_with((PLAYER_X,
                                                                   p.y - added_y),
                                                                  current_level):
                added_y += 1 / added_y
                p.y -= added_y
            else:
                p.is_jumping = False
                starting_y = p.y
                added_y = 1
        if not player_rect_by_position_collides_with((PLAYER_X,
                                                      p.y - added_y),
                                                     current_level) and not p.is_jumping:
            p.y += 1
        if moves:
            block_offset[0] += PLAYER_SPEED * direct
        screen.fill((40, 155, 225))
        current_level.draw_level(screen)
        p.draw(screen)
        pygame.display.flip()

pygame.quit()
