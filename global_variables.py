import pygame
from constants import *
from Class.Level import Level

block_offset = 0
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
test_level = Level(TEST_LEVEL, TEST_LEVEL_BACKGROUND)
