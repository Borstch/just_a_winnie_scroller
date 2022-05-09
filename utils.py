import sys
from typing import Tuple, Optional
from pathlib import Path

import pygame

import config


def load_image(image_path: Path, *, width: Optional[int] = None, height: Optional[int] = None) -> pygame.Surface:
    image = pygame.image.load(str(image_path))
    if width is not None and height is not None:
        return pygame.transform.scale(image, (width, height))
    return image


def init_screen(title: str, icon_path: Path, screen_size: Tuple[int, int]):
    icon = load_image(icon_path)
    pygame.display.set_icon(icon)
    pygame.display.set_caption(title)
    return pygame.display.set_mode(size=screen_size)


def exit_game() -> None:
    sys.exit()


def get_screen_center() -> Tuple[int, int]:
    width, height = config.SCREEN_SIZE
    return width // 2, height // 2
