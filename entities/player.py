from typing import Tuple

import pygame

import config
import utils
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

        self._flipped = False
        self._should_flip = False

        self.score = 0

    @classmethod
    def from_config(cls) -> "Player":
        screen_width, screen_height = config.SCREEN_SIZE
        boundary = (0, screen_width)

        player_x = screen_width // 2 - cls._WIDTH // 2
        player_y = screen_height - cls._HEIGHT * 1.25

        return cls(player_x, player_y, cls._WIDTH, cls._HEIGHT, config.MOVEMENT_SPEED, boundary)

    def update(self, scrolling_speed: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self._move_left()
        elif keys[pygame.K_RIGHT]:
            self._move_right()

    def draw(self, screen: pygame.Surface) -> None:
        if self._should_flip:
            self._sprite = pygame.transform.flip(self._sprite, flip_x=True, flip_y=False)
            self._flipped = not self._flipped
            self._should_flip = False

        screen.blit(self._sprite, self.hitbox)

    def _move_left(self) -> None:
        if not self._flipped:
            self._should_flip = True

        if self._x > self._boundary[0]:
            self._x -= self._horizontal_speed

    def _move_right(self) -> None:
        if self._flipped:
            self._should_flip = True

        if (self._x + self._width) <= self._boundary[1]:
            self._x += self._horizontal_speed

    _WIDTH = 80
    _HEIGHT = 190
    _sprite = utils.load_image(config.PLAYER_SPRITE_PATH, width=_WIDTH, height=_HEIGHT)
