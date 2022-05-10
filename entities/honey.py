import pygame

from .entity import Entity


class Honey(Entity):
    def __init__(self, x: float, y: float, scrolling_speed: float):
        super(Honey, self).__init__(x, y, self.WIDTH, self.HEIGHT)
        self._speed = scrolling_speed

    def update(self, scrolling_speed: float) -> None:
        self._speed = scrolling_speed
        self._y += self._speed

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, color=(0, 255, 0), rect=(self._x, self._y, self._width, self._height))

    WIDTH = 50
    HEIGHT = 50
