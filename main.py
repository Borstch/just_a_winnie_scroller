import config
from game import Game


def main():
    game = Game(
        config.GAME_TITLE,
        config.ICON_PATH,
        config.BG_PATH,
        config.SCREEN_SIZE,
        config.SCROLLING_SPEED,
        config.FRAME_RATE,
    )
    game.main_loop()
    game.exit()


if __name__ == '__main__':
    main()
