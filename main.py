import pygame
from global_variables import *
from constants import *
from Class.Player import Player


def player_grounded(collider_rect: pygame.rect.Rect, level: Level):
    return collider_rect.collidelist(level.collider_list) != -1


def player_touching_wall_right(collider_rect: pygame.rect.Rect, level: Level):
    return collider_rect.collidelist(level.collider_list) != -1


def player_touching_wall_left(collider_rect: pygame.rect.Rect, level: Level):
    return collider_rect.collidelist(level.collider_list) != -1


def make_player_rect_by_position(pos: tuple[int, int]):
    return pygame.rect.Rect(pos[0], pos[1], PLAYER_BOX_WIDTH, PLAYER_BOX_HEIGHT)


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
                    box = make_player_rect_by_position((PLAYER_X - 1, p.y))
                    if not player_touching_wall_left(box, current_level):
                        moves = True
                        direct = 1
                    else:
                        moves = False
                if event.key == pygame.K_RIGHT:
                    box = make_player_rect_by_position((PLAYER_X + 1, p.y))
                    if not player_touching_wall_right(box, current_level):
                        moves = True
                        direct = -1
                    else:
                        moves = False
                if event.key == pygame.K_SPACE:
                    box = make_player_rect_by_position((PLAYER_X, p.y + 1))
                    if player_grounded(box, current_level) and not p.is_jumping:
                        p.is_jumping = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    moves = False
                elif event.key == pygame.K_RIGHT:
                    moves = False
                if event.key == pygame.K_SPACE:
                    p.is_jumping = False

        if p.is_jumping:
            if starting_y - p.y <= BLOCK_SIZE * 3:
                added_y += 1 / added_y
                p.y -= added_y
            else:
                p.is_jumping = False
                starting_y = p.y
                added_y = 1
        box = make_player_rect_by_position((PLAYER_X, p.y + 3))
        if not player_grounded(box, current_level) and not p.is_jumping:
            p.y += 3
        if moves:
            block_offset[0] += PLAYER_SPEED * direct
        screen.fill((40, 155, 225))
        current_level.draw_level(screen)
        p.draw(screen)
        pygame.display.flip()

pygame.quit()
