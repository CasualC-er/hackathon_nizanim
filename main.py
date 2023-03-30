import pygame
from global_variables import *
from constants import *
from Class.Player import Player
from functions import *
from functions import villain_movement
from starte_and_end_screen import starte_screen


if starte_screen():
    if __name__ == '__main__':
        pygame.init()
        pygame.display.set_caption('Jumping Lad')
        pygame.mixer.init()
        pygame.mixer.music.load('sound/soundtrack0.wav')
        pygame.mixer.music.play(-1)
        p = Player([])

        moves = False
        run = True
        direct = 0
        added_y = 1
        starting_y = p.y

        current_level = 0

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        moves = True
                        direct = -1
                    if event.key == pygame.K_RIGHT:
                        moves = True
                        direct = 1
                    if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                        if player_rect_by_position_collides_with((PLAYER_X, p.y + 2), levels[current_level]):
                            p.is_jumping = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        moves = False
                    elif event.key == pygame.K_RIGHT:
                        moves = False
                    if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                        p.is_jumping = False

            if p.is_jumping:
                if (starting_y - p.y <= BLOCK_SIZE * 1
                    and not player_rect_by_position_collides_with((PLAYER_X, p.y - added_y),
                                                                  levels[current_level])) and p.y - added_y > 0:
                    added_y += 5 / added_y
                    p.y -= added_y
                else:
                    p.is_jumping = False
                    starting_y = p.y
                    added_y = 1

            if not player_rect_by_position_collides_with((PLAYER_X, p.y + 5), levels[current_level]) and not p.is_jumping:
                p.y += 5
            if not player_rect_by_position_collides_with((PLAYER_X, p.y + 1), levels[current_level]) and not p.is_jumping:
                p.y += 1

            if moves:
                if not player_rect_by_position_collides_with((PLAYER_X + 3, p.y), levels[current_level]) and direct == 1:
                    block_offset[0] -= PLAYER_SPEED
                if not player_rect_by_position_collides_with((PLAYER_X - 8.01, p.y),
                                                             levels[current_level]) and direct == -1:
                    block_offset[0] += PLAYER_SPEED

    #

            screen.fill(SCREEN_COLOR)
            levels[current_level].draw_level(screen)
            p.draw(screen)
            pygame.display.flip()

        pygame.quit()
