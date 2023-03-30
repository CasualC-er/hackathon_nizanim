import pygame
from constants import *


def starte_screen():
    pygame.init()
    screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Jumping Lad')
    finish = False

    while not finish:

        font = pygame.font.SysFont('Ariel', 60)
        welcome_text = font.render('WELCOME TO JUMPING LAD', True, TEXT_COLOR)
        screen.blit(welcome_text, [20, 20])
        play_text = font.render('PLAY', True, TEXT_COLOR)
        screen.blit(play_text, [20, 60])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if 20 < pos[0] < 120 and 60 < pos[1] < 90:
                    return True

        pygame.display.flip()


def end_screen():
    pygame.init()
    screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Jumping Lad')
    finish = False

    while not finish:

        font = pygame.font.SysFont('Ariel', 60)
        welcome_text = font.render('YOU ARE DEAD !! HAHAHAHA', True, TEXT_COLOR)
        screen.blit(welcome_text, [20, 20])
        play_text = font.render('PLAY AGAIN', True, TEXT_COLOR)
        screen.blit(play_text, [20, 60])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                if 20 < pos[0] < 270 and 60 < pos[1] < 100:
                    return True

        pygame.display.flip()
