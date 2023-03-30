import global_variables
from constants import *
import pygame


class Level:

    def __init__(self, field: list, background: list):
        self.field = field
        self.field_grid_list = self.create_lis(field)
        self.field_pixel_list = self.create_pixel_lis()
        self.background_list = self.create_lis(background)
        self.finish_line_rect = self.create_finish_rec()
        self.collider_list = list()

    def create_lis(self, matrix: list):
        lis = []
        for layer in range(len(self.field)):
            for tile in range(len(self.field[layer])):
                tile_char = matrix[layer][tile]
                if tile_char != ' ' and tile_char != '':
                    pos = (tile * BLOCK_SIZE, layer * BLOCK_SIZE)
                    lis.append([pos, matrix[layer][tile]])
        return lis

    def create_finish_rec(self):
        for layer in range(len(self.field)):
            for tile in range(len(self.field[layer])):
                tile_char = self.field[layer][tile]
                if tile_char == 'FL':
                    return pygame.Rect(tile * BLOCK_SIZE, layer * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)

    def draw_level(self, surface: pygame.surface):
        self.draw_background(surface)
        self.draw_field(surface)

    def draw_field(self, surface: pygame.surface):
        self.collider_list = []
        for tile in self.field_grid_list:
            x = tile[0][0]
            y = tile[0][1]
            char = tile[1]

            if char != ' ':
                if char in FLOOR:
                    tile = pygame.rect.Rect(x + global_variables.block_offset[0], y, BLOCK_SIZE, BLOCK_SIZE)
                    self.collider_list.append(tile)
                if char == BRICK_FLOOR:
                    img = pygame.image.load("texture/Tiles/tile_0047.png")
                elif char == GRASS_FLOOR:
                    img = pygame.image.load("texture/Tiles/tile_0002.png")
                elif char == WATER_TOP:
                    img = pygame.image.load("texture/Tiles/tile_0033.png")
                elif char == FINISH_LINE:
                    img = pygame.image.load("texture/Tiles/tile_0088.png")
                img = pygame.transform.scale(img, (BLOCK_SIZE, BLOCK_SIZE))
                surface.blit(img, (x + global_variables.block_offset[0], y))

    def draw_background(self, surface: pygame.surface):
        for tile in self.background_list:
            x = tile[0][0]
            y = tile[0][1]
            char = tile[1]

            if char != ' ':
                if char == CLOUD_1:
                    img = pygame.image.load("texture/Background/background_cloudA.png")
                    img = pygame.transform.scale(img, (BLOCK_SIZE * 2, BLOCK_SIZE))
                elif char == CLOUD_2:
                    img = pygame.image.load("texture/Background/background_cloudB.png")
                    img = pygame.transform.scale(img, (BLOCK_SIZE * 2, BLOCK_SIZE))

                surface.blit(img, (x, y))

    def create_pixel_lis(self):
        lis = []
        for tile in self.field_grid_list:
            char = tile[1]
            lis.append(tile)
            for i in range(BLOCK_SIZE):
                pos = (tile[0][0] + i, tile[0][1])
                lis.append([pos, char])

        return lis
