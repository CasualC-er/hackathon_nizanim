import pygame
from constants import *


class Level:

    def __init__(self, field: list):
        self.field = field
        self.field_dictionary = self.create_dic()

    def create_dic(self):
        dic = {}
        for layer in range(len(self.field)):
            for tile in range(len(self.field[layer])):
                tile_char = self.field[layer][tile]
                if tile_char != ' ':
                    pos = (tile * BLOCK_SIZE, layer * BLOCK_SIZE)
                    dic[pos] = self.field[layer][tile]
        return dic

    def create_field(self, screen):
        for key in self.field_dictionary:
            x = key[0]
            y = key[1]

            if self.field_dictionary[key] == FLOOR:
                square = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(screen, (90, 50, 10), square)
