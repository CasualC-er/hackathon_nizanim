from main import *
from constants import *


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


def start_screen():
    start_screen = start_screen_maker(SCREEN_COLOR)
    pygame.init()
    running = True
    screen.fill(SCREEN_COLOR)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                continue
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                mouse_pos = x, y
                print(f"{x=}, {y=}")
