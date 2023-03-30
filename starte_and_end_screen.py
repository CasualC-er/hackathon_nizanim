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
        play_text = font.render('PLAY / ', True, TEXT_COLOR)
        screen.blit(play_text, [20, 60])
        character_text = font.render('CHOSE YOURE CHARACTER :', True, TEXT_COLOR)
        screen.blit(character_text, [180, 60])

        img = pygame.image.load("texture/Characters/character_0000.png")
        img = pygame.transform.scale(img, (170, 170))
        screen.blit(img, (700, 110))

        img = pygame.image.load("texture/Characters/character_0002.png")
        img = pygame.transform.scale(img, (170, 170))
        screen.blit(img, (700, 300))

        img = pygame.image.load("texture/Characters/character_0005.png")
        img = pygame.transform.scale(img, (170, 170))
        screen.blit(img, (510, 300))

        img = pygame.image.load("texture/Characters/character_0007.png")
        img = pygame.transform.scale(img, (170, 170))
        screen.blit(img, (510, 110))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                if 20 < pos[0] < 120 and 60 < pos[1] < 90:
                    return True
                if 520 < pos[0] < 650 and 120 < pos[1] < 270:
                    return 7
                if 720 < pos[0] < 830 and 120 < pos[1] < 270:
                    return 0
                if 530 < pos[0] < 650 and 300 < pos[1] < 460:
                    return 5
                if 710 < pos[0] < 800 and 850 < pos[1] < 460:
                    return 2
        pygame.display.flip()


def end_screen():
    pygame.init()
    screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Jumping Lad')
    finish = False
    val = True
    while not finish:
        font = pygame.font.SysFont('Ariel', 60)
        welcome_text = font.render('YOU ARE DEAD !! HAHAHAHA', True, TEXT_COLOR)
        screen.blit(welcome_text, [20, 20])
        play_text = font.render('PLAY AGAIN', True, TEXT_COLOR)
        screen.blit(play_text, [20, 60])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
                val = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                if 20 < pos[0] < 270 and 60 < pos[1] < 100:
                    val = True
                    finish = True
                    print("o 1")

        pygame.display.flip()
    print("2")
    return val
