import pygame


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1000, 500))
    pygame.display.set_caption('Hit the Platypus!')
    screen.fill((40, 155, 225))
    pygame.display.flip()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

pygame.quit()
