from pathlib import Path

import pygame

import utils


class Background:
    def __init__(self, bg_path: Path, width: int, height: int, movement_speed: float):
        self._bg = utils.load_image(bg_path, width=width, height=height)
        self._vertical_speed = movement_speed

        self._height = float(height)
        self._first_bg_y = -self._height
        self._second_bg_y = 0.0

    def update(self, scrolling_speed: float) -> None:
        self._vertical_speed = scrolling_speed

        self._first_bg_y += self._vertical_speed
        self._second_bg_y += self._vertical_speed

        if self._first_bg_y > self._height:
            self._first_bg_y = -self._height

        if self._second_bg_y > self._height:
            self._second_bg_y = -self._height

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self._bg, (0, self._first_bg_y))
        screen.blit(self._bg, (0, self._second_bg_y))
