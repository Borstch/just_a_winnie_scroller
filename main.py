import config
from game import Game
from menu import Menu


def main():
    game = Game(
        config.GAME_TITLE,
        config.ICON_PATH,
        config.BG_PATH,
        config.BACKGROUND_SOUND_PATH,
        config.SCREEN_SIZE,
        config.SCROLLING_SPEED,
        config.SCROLLING_COEF,
        config.MAX_SCROLLING_SPEED,
        config.FRAME_RATE,
    )
    menu = Menu(game.screen, config.SCREEN_SIZE, game.main_loop, game.exit)
    menu.draw()


if __name__ == '__main__':
    main()
