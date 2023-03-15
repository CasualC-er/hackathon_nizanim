import pygame
from constants import *
from global_variables import *

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

    def draw_field(self, screen):
        for key in self.field_dictionary:
            x = key[0]
            y = key[1]

            if self.field_dictionary[key] == FLOOR:
                img = pygame.image.load("images/flor.jpg")
                img = pygame.transform.scale(img, (BLOCK_SIZE, BLOCK_SIZE))
                screen.blit(img, (x + block_offset, y))
