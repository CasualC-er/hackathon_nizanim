from Class.Block import Block
from global_variables import *


class Obstacle(Block):
    def __init__(self, speed, on_the_screen):
        self.speed = speed
        self.on_the_screen = on_the_screen
        Block.__init__(self, speed, on_the_screen)



