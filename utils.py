import sys
from typing import Tuple

import pygame


def load_image(image_path: str) -> pygame.Surface:
    return pygame.image.load(image_path)


def init_screen(title: str, icon_path: str, screen_size: Tuple[int, int]):
    icon = load_image(icon_path)
    pygame.display.set_icon(icon)
    pygame.display.set_caption(title)
    return pygame.display.set_mode(size=screen_size)


def exit_game() -> None:
    sys.exit()
