from random import randint

import pygame

import config
import utils
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
        screen.blit(self._sprite, self.hitbox)

    def _swing(self) -> None:
        self._y += self._swing_speed

        self._swings_count += 1
        if self._swings_count % self._SWING_FLIP_COEF == 0:
            self._swing_speed = -self._swing_speed
    
    _SWING_SPEED = 0.35
    _SWING_FLIP_COEF = config.FRAME_RATE * 2
    WIDTH = 50
    HEIGHT = 50
    _sprite = utils.load_image(config.BEE_SPRITE_PATH, width=WIDTH, height=HEIGHT)
