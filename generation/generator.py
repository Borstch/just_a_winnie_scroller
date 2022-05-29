import random
from typing import Dict, List, Callable

from entities import Entity
from .average_generation import get_average_row
from .extended_generation import get_shifting_row, get_moving_row, get_boomerang_row


GenerationFunction = Callable[[float, bool], List[Entity]]


class Generator:
    def __init__(self):
        self._extended_generators = []
        self._moving_row_spawn_chance = 0.0
        self._honey_spawn_chance = 1.0

    def get_row(self, scrolling_speed: float, player_on_left: bool) -> List[Entity]:
        if self._extended_generators and self._should_generate_moving_bee():
            return random.choice(self._extended_generators)(scrolling_speed, player_on_left)
        return get_average_row(scrolling_speed, self._should_generate_honey())

    def update(self, player_score: int) -> None:
        for threshold in self._THRESHOLDS_GENERATORS.keys():
            if player_score == threshold:
                self._extended_generators.append(
                    self._THRESHOLDS_GENERATORS[threshold]
                )
                self._honey_spawn_chance -= self._HONEY_CHANCE_DECREASE_FACTOR
                self._moving_row_spawn_chance += self._MOVING_ROW_CHANCE_INCREASE_FACTOR
                break

    def _should_generate_moving_bee(self) -> bool:
        return random.randint(0, 101) < (self._moving_row_spawn_chance * 100)

    def _should_generate_honey(self) -> bool:
        return random.randint(0, 101) < (self._honey_spawn_chance * 100)

    _HONEY_CHANCE_DECREASE_FACTOR = 0.05
    _MOVING_ROW_CHANCE_INCREASE_FACTOR = 0.16
    _THRESHOLDS_GENERATORS: Dict[int, GenerationFunction] = {
        10: get_shifting_row,
        20: get_moving_row,
        30: get_boomerang_row,
    }
