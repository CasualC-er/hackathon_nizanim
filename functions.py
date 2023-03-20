from main import *
from constants import *


def start_screen_maker(color):
    pygame.init()
    start_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('')
    start_screen.fill(color)
    pygame.display.flip()
    return start_screen


def start_screen():
    start_screen = start_screen_maker(SCREEN_COLOR)
    pygame.init()
    running = True
    screen.fill(SCREEN_COLOR)

