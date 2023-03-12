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
        self.hit_box: pygame.rect.Rect = pygame.rect.Rect(0, 0, consts.PLAYER_BOX_WIDTH, consts.PLAYER_BOX_HEIGHT)

    def move(self, direction: int):
        if direction == 1:
            global_variables.offset += self.speed
        elif direction == -1:
            global_variables.offset -= self.speed
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

    def check_collisions(self):
        pass


