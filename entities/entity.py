from abc import ABCMeta, abstractmethod

import pygame


class Entity(metaclass=ABCMeta):
    def __init__(self, x: float, y: float, width: int, height: int):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    @property
    def hitbox(self) -> pygame.Rect:
        return pygame.Rect(self._x, self._y, self._width, self._height)

    @abstractmethod
    def update(self, scrolling_speed: float) -> None:
        pass

    @abstractmethod
    def draw(self, screen: pygame.Surface) -> None:
        pass

    def is_collide(self, other: "Entity") -> bool:
        return self.hitbox.colliderect(other.hitbox)

    def is_on_screen(self, screen: pygame.Surface) -> bool:
        vertically_on_screen = 0 <= self._y <= screen.get_height()
        horizontally_on_screen = 0 <= self._x <= screen.get_width()
        return vertically_on_screen and horizontally_on_screen
