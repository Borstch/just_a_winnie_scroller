import pygame

from .entity import Entity


class Bee(Entity):
    def __init__(self, x: float, y: float):
        super(Bee, self).__init__(x, y, self._WIDTH, self._HEIGHT)

        self._speed = self._SWING_SPEED
        self._lower_swing_bound = self._y - self._SWING_BOUNDARY_COEF
        self._upper_swing_bound = self._y + self._SWING_BOUNDARY_COEF

    def update(self) -> None:
        self._swing()

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, color=(255, 0, 0), rect=(self._x, self._y, self._width, self._height))

    def _swing(self) -> None:
        self._y += self._speed
        if not (self._lower_swing_bound <= self._y <= self._upper_swing_bound):
            self._speed = -self._speed
    
    _SWING_SPEED = 0.15
    _SWING_BOUNDARY_COEF = 3
    _WIDTH = 50
    _HEIGHT = 50
