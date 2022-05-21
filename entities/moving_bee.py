from typing import Union

import pygame

from .bee import Bee


MovementDirection = Union["LEFT", "RIGHT"]


class MovingBee(Bee):
    def __init__(
            self, x: float, y: float, scrolling_speed: float, direction: MovementDirection
    ):
        super(MovingBee, self).__init__(x, y, scrolling_speed)
        self._direction = direction

        if self._should_flip_sprites():
            self._sprites = [pygame.transform.flip(sprite, flip_x=True, flip_y=False) for sprite in self._sprites]

    def update(self, scrolling_speed: float) -> None:
        super(MovingBee, self).update(scrolling_speed)
        self._x += self._culc_movement_direction()

    def _culc_movement_direction(self) -> float:
        if self._direction == "LEFT":
            return -self._scrolling_speed
        elif self._direction == "RIGHT":
            return self._scrolling_speed
        else:
            return 0.0

    def _should_flip_sprites(self) -> bool:
        return self._direction == "RIGHT"
