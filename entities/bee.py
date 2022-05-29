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

        self._fly_count = 0

    def update(self, scrolling_speed: float) -> None:
        self._scrolling_speed = scrolling_speed
        self._y += self._scrolling_speed
        self._swing()

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self._sprites[self._fly_count], self.hitbox)
        self._fly_count = (self._fly_count + 1) % len(self._sprites)

    def is_on_screen(self, screen: pygame.Surface) -> bool:
        vertically_on_screen = self._y <= screen.get_height()
        horizontally_on_screen = -Bee.WIDTH <= self._x <= screen.get_width() + Bee.WIDTH
        return vertically_on_screen and horizontally_on_screen

    def _swing(self) -> None:
        self._y += self._swing_speed

        self._swings_count += 1
        if self._swings_count % self._SWING_FLIP_COEF == 0:
            self._swing_speed = -self._swing_speed
    
    _SWING_SPEED = 0.35
    _SWING_FLIP_COEF = config.FRAME_RATE * 2
    WIDTH = 50
    HEIGHT = 50
    _sprites = [
        utils.load_image(sprite_path, width=50, height=50)
        for sprite_path in config.BEE_SPRITES_PATH
    ]
