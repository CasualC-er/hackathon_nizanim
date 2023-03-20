BLOCK_SIZE = 64
SCREEN_WIDTH = BLOCK_SIZE * 15
SCREEN_HEIGHT = BLOCK_SIZE * 8
SCREEN_COLOR = (40, 155, 225)

PLAYER_BOX_WIDTH = 20
PLAYER_BOX_HEIGHT = 40
PLAYER_SPEED = 5
PLAYER_START_Y = SCREEN_HEIGHT - BLOCK_SIZE - PLAYER_BOX_HEIGHT
PLAYER_X = SCREEN_WIDTH//4

BRICK_FLOOR = 'F'
GRASS_FLOOR = 'G'
BRICK_TILE = 'B'
FLOOR = [BRICK_FLOOR, GRASS_FLOOR, BRICK_TILE]

CLOUD_1 = 'C1'
CLOUD_2 = 'C2'
MOUNTAIN = 'M'

TEST_LEVEL = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'F', ' '],
    [' ', 'F', 'F', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', 'F', 'F', 'F', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'F', 'F', 'F', ' ', ' '],
    ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G']
]

TEST_LEVEL_BACKGROUND = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', 'C1', ' ', ' ', ' ', ' ', ' ', ' ', 'C2', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', 'C2', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C1', 'C1', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

START_BUTTON_X_POS = SCREEN_WIDTH / 2
START_BUTTON_Y_POS = 256
START_BUTTON_HEIGHT = 100
START_BUTTON_WIDTH = 300
