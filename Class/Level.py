import global_variables
from constants import *
import pygame


class Level:

    def __init__(self, field: list, background: list):
        self.field = field
        self.field_dictionary = self.create_dic(field)
        self.background_dictionary = self.create_dic(background)

    def create_dic(self, matrix):
        dic = {}
        for layer in range(len(self.field)):
            for tile in range(len(self.field[layer])):
                tile_char = matrix[layer][tile]
                if tile_char != ' ':
                    pos = (tile * BLOCK_SIZE, layer * BLOCK_SIZE)
                    dic[pos] = matrix[layer][tile]
        return dic

    def draw_level(self, surface):
        self.draw_background(surface)
        self.draw_field(surface)

    def draw_field(self, surface):
        for key in self.field_dictionary:
            x = key[0]
            y = key[1]
            char = self.field_dictionary[key]

            if char != ' ':
                if char == FLOOR:
                    img = pygame.image.load("images/flor.jpg")
                img = pygame.transform.scale(img, (BLOCK_SIZE, BLOCK_SIZE))
                surface.blit(img, (x + global_variables.block_offset[0], y))

    def draw_background(self, surface):
        for key in self.background_dictionary:
            x = key[0]
            y = key[1]
            char = self.background_dictionary[key]

            if char != ' ':
                if char == CLOUD_1:
                    img = pygame.image.load("images/cloud_1.png")
                elif char == CLOUD_2:
                    img = pygame.image.load("images/cloud_2.png")

                img = pygame.transform.scale(img, (BLOCK_SIZE, BLOCK_SIZE))
                surface.blit(img, (x, y))
