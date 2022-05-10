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
            game_sound_path: Path,
            screen_size: Tuple[int, int],
            scrolling_speed: float,
            scrolling_coef: float,
            max_scrolling_speed: float,
            frame_rate: int,
    ):
        self._init_pygame_and_events()

        self._bg_sound = pygame.mixer.Sound(game_sound_path)
        self._bg_sound.set_volume(0.25)

        self._initial_scrolling_speed = scrolling_speed
        self._scrolling_speed = scrolling_speed
        self._max_speed = max_scrolling_speed
        self._speed_coef = scrolling_coef

        self._font = pygame.font.SysFont("Impact", 38)
        self._screen = utils.init_screen(title, icon_path, screen_size)
        self._clock = pygame.time.Clock()
        self._bg = Background(background_path, *screen_size, int(scrolling_speed))

        self._player = Player.from_config()
        self._entities = get_row(self._initial_scrolling_speed)

        self._frame_rate = frame_rate
        self._running = True

    @property
    def screen(self) -> pygame.Surface:
        return self._screen

    def main_loop(self) -> int:
        self._bg_sound.play()

        while self._running:
            self._update()
            self._draw()

            self._clock.tick(self._frame_rate)

        self._bg_sound.stop()
        score = self._player.score
        self.reset()
        return score

    def reset(self) -> None:
        self._running = True
        self._scrolling_speed = self._initial_scrolling_speed
        self._bg.update(self._scrolling_speed)
        self._player = Player.from_config()
        self._entities.clear()

    @staticmethod
    def exit() -> None:
        utils.exit_game()

    @property
    def _text(self) -> pygame.Surface:
        return self._font.render(str(self._player.score), False, (176, 91, 24))

    def _update(self) -> None:
        self._bg.update(self._scrolling_speed)
        self._player.update(self._scrolling_speed)

        for entity in self._get_entities():
            entity.update(self._scrolling_speed)
            if self._player.is_collide(entity):
                self._process_collision(entity)

        self._remove_entities_off_the_screen()
        self._dispatch_events()

    def _draw(self) -> None:
        self._bg.draw(self._screen)
        self._player.draw(self._screen)
        for entity in self._get_entities():
            entity.draw(self._screen)

        self._screen.blit(self._text, (10, 5))

        pygame.display.update()

    def _dispatch_events(self) -> None:
        for event in pygame.event.get():
            if event.type == INSTANTIATE_ROW:
                self._entities.extend(get_row(self._scrolling_speed))
            elif event.type == pygame.QUIT:
                self._running = False

    def _process_collision(self, entity: Entity) -> None:
        if isinstance(entity, Bee):
            self._player.die()
            self._running = False
        elif isinstance(entity, Honey):
            self._player.eat()
            self._player.score += 1
            self._update_scrolling_speed()
            self._update_spawn_timer()

        self._remove_entity(entity)

    def _update_scrolling_speed(self) -> None:
        self._scrolling_speed = min(self._scrolling_speed * self._speed_coef, self._max_speed)

    def _update_spawn_timer(self) -> None:
        increase_coef = self._initial_scrolling_speed / self._scrolling_speed
        pygame.time.set_timer(INSTANTIATE_ROW, int(self._SPAWN_RATE * increase_coef))

    def _get_entities(self) -> Generator[Entity, None, None]:
        for entity in self._entities:
            yield entity

    def _remove_entities_off_the_screen(self) -> None:
        entities_to_remove = [entity for entity in self._entities if not entity.is_on_screen(self._screen)]
        for entity in entities_to_remove:
            self._remove_entity(entity)

    def _remove_entity(self, entity: Entity) -> None:
        self._entities.pop(self._entities.index(entity))

    @classmethod
    def _init_pygame_and_events(cls) -> None:
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        pygame.time.set_timer(INSTANTIATE_ROW, cls._SPAWN_RATE)

    _SPAWN_RATE = 5500
