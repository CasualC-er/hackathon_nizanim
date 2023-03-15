import pygame

import global_variables
import constants as consts
from Class.Block import Block
from Class.FinishLine import FinishLine
from Class.Obstacle import Obstacle


class Player:
    def __init__(self, speed: float,
                 sprites: list):
        self.y = consts.PLAYER_START_Y
        self.touching_enemy = False
        self.touching_goal = False
        self.speed = speed
        self.sprites = sprites
        # both are grid (size: 1 unit by 1 unit, pos: 0, 0 on the grid)
        self.position: tuple[int, int] = (0, 0)
        self.in_block_height: int = 0

    def move(self, direction: int):
        if direction == 1:
            global_variables.block_offset += self.speed
        elif direction == -1:
            global_variables.block_offset -= self.speed
        else:
            raise RuntimeError("Invalid direction")

    def is_grounded(self):
        under = (self.position[0], self.position[1]-1)
        return Player.check_collisions(global_variables.test_level, under) == "B"

    @staticmethod
    def check_collisions(field: dict, position: tuple[int, int]):
        if position in field:
            if isinstance(field[position], Obstacle):
                return "O"
            if isinstance(field[position], FinishLine):
                return "F"
            if type(field[position]) == Block:
                return "B"

    def die(self):
        pass

    def finish(self):
        pass

