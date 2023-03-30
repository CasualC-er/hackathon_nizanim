import pygame
# from main import *
from constants import *
from Class.Level import Level


def player_rect_by_position_collides_with(pos: tuple[int, int], level: Level):
    return pygame.rect.Rect(pos[0], pos[1], PLAYER_BOX_WIDTH, PLAYER_BOX_HEIGHT).collidelist(level.collider_list) != -1


def start_screen_maker(color):
    pygame.init()
    start_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('')
    start_screen.fill(color)
    pygame.display.flip()
    return start_screen


def mouse_in_button(button, mouse_pos):
    if button.x_pos + button.width > mouse_pos[0] > button.x_pos and \
            button.y_pos < mouse_pos[1] < button.y_pos + button.height:
        return True


def villain_pos(current_level):
    pos = [0, 0]
    for row in range(ROW):
        for col in range(COL):
            if current_level[row][col] == 'V':
                pos = [row, col]
                return pos
            else:
                pass


def villain_movement(current_level):
    while True:
        pos = villain_pos(current_level)

        for i in range(5):
            current_level[pos[0]][pos[1]] = ' '
            if pos[1] + 1 < COL and current_level[pos[0]][pos[1]] == ' ':
                current_level[pos[0]][pos[1] + 1] = 'V'
            else:
                break

        for j in range(10):
            current_level[pos[0]][pos[1]] = ' '
            if pos[1] - 1 < COL and current_level[pos[0]][pos[1]] == ' ':
                current_level[pos[0]][pos[1] - 1] = 'V'
            else:
                break
