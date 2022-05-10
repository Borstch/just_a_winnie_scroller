from random import randrange
from typing import Tuple, Generator
from pathlib import Path

import pygame

import utils
from ambient import Background
from entities import Entity, Player, Bee, Honey
from events import INSTANTIATE_ROW
from generation import get_row


class Game:
    def __init__(
            self,
            title: str,
            icon_path: Path,
            background_path: Path,
            screen_size: Tuple[int, int],
            scrolling_speed: float,
            frame_rate: int,
    ):
        self._init_pygame_and_events()

        self._frame_rate = frame_rate
        self._scrolling_speed = scrolling_speed

        self._screen = utils.init_screen(title, icon_path, screen_size)
        self._clock = pygame.time.Clock()
        self._bg = Background(background_path, *screen_size, int(scrolling_speed))

        self._player = Player.from_config()
        self._entities = []

        self._running = True

    def main_loop(self) -> None:
        while self._running:
            self._update()
            self._draw()

            self._clock.tick(self._frame_rate)

    def _update(self) -> None:
        self._bg.update()
        self._player.update()

        for entity in self._get_entities():
            entity.update()
            if self._player.is_collide(entity):
                self._process_collision(entity)

        self._remove_entities_off_the_screen()
        self._dispatch_events()

    def _draw(self) -> None:
        self._bg.draw(self._screen)
        self._player.draw(self._screen)
        for entity in self._get_entities():
            entity.draw(self._screen)

        pygame.display.update()

    def _dispatch_events(self) -> None:
        for event in pygame.event.get():
            if event.type == INSTANTIATE_ROW:
                self._entities.extend(get_row(self._scrolling_speed))
            elif event.type == pygame.QUIT:
                self._running = False

    def _process_collision(self, entity: Entity) -> None:
        if isinstance(entity, Bee):
            self._running = False
            print("[DEBUG] Player hit bee")
        elif isinstance(entity, Honey):
            self._player.score += 1
            print(f"[DEBUG] Player score is now {self._player.score}")

        self._remove_entity(entity)

    def _get_entities(self) -> Generator[Entity, None, None]:
        for entity in self._entities:
            yield entity

    def _remove_entities_off_the_screen(self) -> None:
        entities_to_remove = [entity for entity in self._entities if not entity.is_on_screen(self._screen)]
        for entity in entities_to_remove:
            self._remove_entity(entity)

    def _remove_entity(self, entity: Entity) -> None:
        self._entities.pop(self._entities.index(entity))

    @staticmethod
    def exit() -> None:
        utils.exit_game()

    @staticmethod
    def _init_pygame_and_events() -> None:
        pygame.init()
        pygame.time.set_timer(INSTANTIATE_ROW, randrange(4000, 5000))
