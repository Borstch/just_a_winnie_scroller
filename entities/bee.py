from random import randint

import pygame

import config
from .entity import Entity


class Bee(Entity):
    def __init__(self, x: float, y: float, scrolling_speed: float):
        super(Bee, self).__init__(x, y, self.WIDTH, self.HEIGHT)
        self._scrolling_speed = scrolling_speed

        self._swing_speed = self._SWING_SPEED if randint(0, 2) else -self._SWING_SPEED
        self._swings_count = 0

    def update(self, scrolling_speed: float) -> None:
        self._scrolling_speed = scrolling_speed
        self._y += self._scrolling_speed
        self._swing()

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, color=(255, 0, 0), rect=(self._x, self._y, self._width, self._height))

    def _swing(self) -> None:
        self._y += self._swing_speed

        self._swings_count += 1
        if self._swings_count % self._SWING_FLIP_COEF == 0:
            self._swing_speed = -self._swing_speed
    
    _SWING_SPEED = 0.3
    _SWING_FLIP_COEF = config.FRAME_RATE * 1.5
    WIDTH = 50
    HEIGHT = 50
