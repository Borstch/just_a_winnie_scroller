from random import randrange

import pygame

import config
import utils
from ambient import Background
from entities import Player
from events import INSTANTIATE_ROW
from generation import get_row


def main():
    pygame.init()

    pygame.time.set_timer(INSTANTIATE_ROW, randrange(2000, 3500))

    screen = utils.init_screen(config.GAME_TITLE, config.ICON_PATH, config.SCREEN_SIZE)
    clock = pygame.time.Clock()

    bg = Background(config.BG_PATH, *config.SCREEN_SIZE, config.SCROLLING_SPEED)
    player = Player.from_config()
    rows = []

    running = True
    while running:
        bg.update()
        player.update()

        for row in rows:
            for entity in row:
                entity.update()

        bg.draw(screen)
        player.draw(screen)

        for row in rows:
            for entity in row:
                entity.draw(screen)

        for event in pygame.event.get():
            if event.type == INSTANTIATE_ROW:
                rows.clear()
                rows.append(get_row())
            elif event.type == pygame.QUIT:
                running = False

        pygame.display.update()
        clock.tick(config.FRAME_RATE)

    utils.exit_game()


if __name__ == '__main__':
    main()
