import pygame

import config
import utils
from ambient import Background
from entities import Player


def main():
    pygame.init()

    screen = utils.init_screen(config.GAME_TITLE, config.ICON_PATH, config.SCREEN_SIZE)
    clock = pygame.time.Clock()

    bg = Background(config.BG_PATH, *config.SCREEN_SIZE, config.SCROLLING_SPEED)
    player = Player.from_config()

    running = True
    while running:
        bg.update()
        player.update()

        bg.draw(screen)
        player.draw(screen)

        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                running = False

        pygame.display.update()
        clock.tick(config.FRAME_RATE)

    utils.exit_game()


if __name__ == '__main__':
    main()
