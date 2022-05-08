import pygame

import config
import utils


def main():
    pygame.init()
    screen = utils.init_screen(config.GAME_TITLE, config.ICON_PATH, config.SCREEN_SIZE)
    while True:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                utils.exit_game()


if __name__ == '__main__':
    main()
