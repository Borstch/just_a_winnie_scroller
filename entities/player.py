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
        self._swing_count = 0
        self._frame_count = 0

        self._eat_sound = pygame.mixer.Sound(config.HONEY_PICKING_SOUND_PATH)
        self._die_sound = pygame.mixer.Sound(config.GAME_OVER_SOUND_PATH)

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
            self._sprites = [pygame.transform.flip(sprite, flip_x=True, flip_y=False) for sprite in self._sprites]
            self._flipped = not self._flipped
            self._should_flip = False

        screen.blit(self._sprites[self._swing_count], self.hitbox)

        self._frame_count += 1
        if self._frame_count % self._SWING_SPEED == 0:
            self._swing_count = (self._swing_count + 1) % len(self._sprites)

    def eat(self) -> None:
        self._eat_sound.play(0, 0, 0)

    def die(self) -> None:
        self._die_sound.play(0, 0, 0)

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
    _SWING_SPEED = config.FRAME_RATE * 0.5
    _sprites = [
        utils.load_image(sprite_path, width=80, height=190)
        for sprite_path in config.PLAYER_SPRITES_PATH
    ]
