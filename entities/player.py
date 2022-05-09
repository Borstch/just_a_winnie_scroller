from typing import Tuple

import pygame

import config
from .entity import Entity


class Player(Entity):
    def __init__(
            self, x: float,
            y: float,
            width: int,
            height: int,
            movement_speed: float,
            horizontal_boundary: Tuple[int, int],
    ):
        super(Player, self).__init__(x, y, width, height)
        self._horizontal_speed = movement_speed
        self._boundary = horizontal_boundary

    @classmethod
    def from_config(cls) -> "Player":
        screen_width, screen_height = config.SCREEN_SIZE
        boundary = (0, screen_width)

        player_width = 80
        player_height = 125

        player_x = screen_width // 2 - player_width // 2
        player_y = screen_height - player_height * 1.25

        return cls(player_x, player_y, player_width, player_height, config.MOVEMENT_SPEED, boundary)

    def update(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self._move_left()
        elif keys[pygame.K_RIGHT]:
            self._move_right()

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, color=(255, 0, 255), rect=(self._x, self._y, self._width, self._height))

    def _move_left(self) -> None:
        if self._x > self._boundary[0]:
            self._x -= self._horizontal_speed

    def _move_right(self) -> None:
        if (self._x + self._width) <= self._boundary[1]:
            self._x += self._horizontal_speed
