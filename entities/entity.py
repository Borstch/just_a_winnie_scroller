from abc import ABCMeta, abstractmethod

import pygame


class Entity(metaclass=ABCMeta):
    def __init__(self, x: float, y: float, width: int, height: int):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def draw(self, screen: pygame.Surface) -> None:
        pass
