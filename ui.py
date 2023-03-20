import json


from main import *


def title_screen():
    screen_color = draw_screen.screen_colour_and_cover_colour()
    screen = screen_maker(screen_color)
    pygame.init()
    running = True
    caunt = 0
    x, y = 0, 0
    i = 0
    screen.fill(screen_color)
    draw_board_layer_music_on(screen)
    level(screen, i)
    music_on = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                continue
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(f"{x=}, {y=}")

        if 300 <= x <= 400 and 300 <= y <= 400:
            caunt += 1
            if caunt % 2 == 0:
                draw_board_layer_music_on(screen)
                music_on = True
            else:
                draw_board_layer_music_off(screen)
                music_on = False
            x, y = 0, 0

        if 300 <= x <= 400 and 150 <= y <= 250 :
            if __name__ == '__main__':
                main()

        if 450 <= x <= 600:
            if 150 <= y <= 250:
                i = 0
            elif 250 <= y <= 350:
                i = 1
            elif 350 <= y <= 450:
                i = 2
        screen.fill(screen_color)
        if music_on:
            draw_board_layer_music_on(screen)
        else:
            draw_board_layer_music_off(screen)
        level(screen, i)
        pygame.display.flip()
        with open("settings.json", "r") as settings:
            settings_dict = json.load(settings)
            settings_dict["music_on"] = music_on
            settings_dict["difficulty"] = i
        with open("settings.json", "w") as settings:
            json.dump(settings_dict, settings)

    pygame.quit()


title_screen()
