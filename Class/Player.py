import pygame

import global_variables
import constants as consts
from Class.Block import Block
# from Class.FinishLine import FinishLine
from Class.Obstacle import Obstacle


class Player:
    def __init__(self, speed: float,
                 sprites: list):
        self.is_grounded: bool = True
        self.is_jumping: bool = False
        self.y = consts.PLAYER_START_Y
        self.touching_enemy = False
        self.touching_goal = False
        self.speed = speed
        self.sprites = sprites
        self.position: list[int, int] = [0, 0]
        self.in_block_height: int = 0

    def move(self, direction: int):
        if direction == 1:
            global_variables.block_offset += self.speed
        elif direction == -1:
            global_variables.block_offset -= self.speed
        else:
            raise RuntimeError("Invalid direction")

    @staticmethod
    def check_collisions(field: dict, position: tuple[int, int]):
        if position in field:
            if isinstance(field[position], Obstacle):
                return "O"
#            if isinstance(field[position], FinishLine):
#               return "F"
            if type(field[position]) == type(Block("","")):
                return "B"

    def calculate_grid_position(self):
        return global_variables.block_offset, self.y // consts.BLOCK_SIZE

    def die(self):
        pass

    def finish(self):
        pass

