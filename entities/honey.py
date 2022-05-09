import pygame

from .entity import Entity


class Honey(Entity):
    def __init__(self, x: float, y: float):
        super(Honey, self).__init__(x, y, self._WIDTH, self._HEIGHT)

    def update(self) -> None:
        pass

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, color=(0, 255, 0), rect=(self._x, self._y, self._width, self._height))

    _WIDTH = 50
    _HEIGHT = 50