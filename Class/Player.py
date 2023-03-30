import pygame
import datetime

import global_variables
import constants as consts


class Player:
    def __init__(self,
                 sprites: list):
        self.is_grounded: bool = True
        self.is_jumping: bool = False
        self.y = consts.PLAYER_START_Y
        self.touching_enemy = False
        self.touching_goal = False
        self.sprites = sprites
        self.position: list[int, int] = [0, 0]
        self.in_block_height: int = 0

    def calculate_grid_position(self):
        return global_variables.block_offset, self.y // consts.BLOCK_SIZE

    def die(self):
        pass

    def finish(self):
        self.y = consts.PLAYER_START_Y
        global_variables.block_offset[0] = 0

    def draw(self, screen: pygame.Surface, texture=0):
        t = datetime.datetime.now().time()
        texture *= 2
        # rec = pygame.Rect(consts.PLAYER_X, self.y, consts.PLAYER_BOX_WIDTH, consts.PLAYER_BOX_HEIGHT)
        x = texture + (int(t.second) % 2)
        rec = pygame.image.load(f"texture/Characters/character_000{x}.png")
        img = pygame.transform.scale(rec, (consts.PLAYER_BOX_WIDTH, consts.PLAYER_BOX_HEIGHT))
        screen.blit(img, (consts.PLAYER_X, self.y))
