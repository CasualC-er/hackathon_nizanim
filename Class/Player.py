import pygame

import global_variables
import constants as consts


class Player:
    def __init__(self, speed: float,
                 sprites: list):
        self.y = consts.PLAYER_START_Y
        self.jumpCount = 10
        self.jumping = False
        self.touching_enemy = False
        self.touching_goal = False
        self.speed = speed
        self.sprites = sprites
        # both are grid (size: 1 unit by 1 unit, pos: 0, 0 on the grid)
        self.hit_box: tuple[int, int] = (1, 1)
        self.position: tuple[int, int] = (0, 0)

    def move(self, direction: int):
        if direction == 1:
            global_variables.block_offset += self.speed
        elif direction == -1:
            global_variables.block_offset -= self.speed
        else:
            raise RuntimeError("Invalid direction")

    def jump(self):
        if self.jumping:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= self.jumpCount ** 2 * 0.1 * neg
                self.jumpCount -= 1
            else:
                self.jumping = False
                self.jumpCount = 10

    def check_collisions(self, field: dict):
        if self.position in field:
            if isinstance(field[self.position], int):
                self.die()

    def die(self):
        pass


