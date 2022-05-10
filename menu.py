from typing import Tuple, Callable

import pygame
import pygame_menu

import config


_menu_background = pygame_menu.baseimage.BaseImage(
    image_path=config.MENU_BG_PATH,
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
    drawing_offset=(0, 0)
)
_menu_button_background = pygame_menu.baseimage.BaseImage(
    image_path=config.MENU_BUTTON_PATH,
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
    drawing_offset=(0, 0)
)
_menu_theme = pygame_menu.Theme(
    title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
    background_color=_menu_background,
    widget_background_color=_menu_button_background,
    widget_margin=(0, 15),
    widget_selection_effect=pygame_menu.widgets.NoneSelection(),
    widget_font=pygame_menu.font.FONT_MUNRO,
    widget_font_color=(140, 47, 14),
    widget_font_size=52,
)


class Menu:
    def __init__(
            self,
            screen: pygame.Surface,
            menu_size: Tuple[int, int],
            on_play: Callable[[], int],
            on_quit: Callable[[], None],
    ):
        self._screen = screen

        self._menu = pygame_menu.Menu("", *menu_size, theme=_menu_theme)
        self._score = self._menu.add.label("Score: 0", padding=(10, 15, 5, 30))
        self._menu.add.button("PLAY", self._run_game(on_play), padding=(10, 45, 5, 60))
        self._menu.add.button("QUIT", on_quit, padding=(10, 55, 5, 70))

    def draw(self) -> None:
        self._menu.mainloop(self._screen)

    def _run_game(self, runner: Callable[[], int]) -> Callable[[], None]:
        def run():
            score = runner()
            self._score.set_title(f"Score: {score}")
        return run
