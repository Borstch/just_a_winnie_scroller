import pygame

import config
import utils
from .entity import Entity


class Honey(Entity):
    def __init__(self, x: float, y: float, scrolling_speed: float):
        super(Honey, self).__init__(x, y, self.WIDTH, self.HEIGHT)
        self._speed = scrolling_speed

    def update(self, scrolling_speed: float) -> None:
        self._speed = scrolling_speed
        self._y += self._speed

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self._sprite, self.hitbox)

    WIDTH = 50
    HEIGHT = 55
    _sprite = utils.load_image(config.HONEY_SPRITE_PATH, width=WIDTH, height=HEIGHT)
