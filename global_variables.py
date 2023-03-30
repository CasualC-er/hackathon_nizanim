import pygame
from constants import *
from Class.Level import Level

block_offset = [0]
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
test_level = Level(TEST_LEVEL, TEST_LEVEL_BACKGROUND)
test_level_2 = Level(TEST_LEVEL_2, TEST_LEVEL_BACKGROUND_2)
levels = [test_level, test_level_2]
