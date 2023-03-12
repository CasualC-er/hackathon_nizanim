import pygame


class Player:
    def __init__(self, speed: float,
                 sprite=pygame.rect.Rect(0, 0, 20, 40)):
        self.grounded = False
        self.touching_enemy = False
        self.touching_goal = False
        self.speed = speed
        self.sprite = sprite

