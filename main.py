from random import randrange

import pygame

import config
import utils
from ambient import Background
from entities import Player, Bee, Honey
from events import INSTANTIATE_ROW
from generation import get_row


def main():
    pygame.init()

    pygame.time.set_timer(INSTANTIATE_ROW, randrange(4000, 5000))

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

                if player.is_collide(entity):
                    if isinstance(entity, Bee):
                        running = False
                        print("[DEBUG] Player hit bee")
                    elif isinstance(entity, Honey):
                        player.score += 1
                        row.pop(row.index(entity))
                        print(f"[DEBUG] Player score is now {player.score}")

        bg.draw(screen)
        player.draw(screen)

        for row in rows:
            for entity in row:
                entity.draw(screen)

        for event in pygame.event.get():
            if event.type == INSTANTIATE_ROW:
                rows.append(get_row(config.SCROLLING_SPEED))
            elif event.type == pygame.QUIT:
                running = False

        for row in rows:
            for entity in row:
                if not entity.is_on_screen(screen):
                    row.pop(row.index(entity))

        pygame.display.update()
        clock.tick(config.FRAME_RATE)

    utils.exit_game()


if __name__ == '__main__':
    main()
