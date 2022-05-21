import random
from typing import List

import config
from entities import Entity, Bee, MovingBee, Honey
from utils import get_screen_center


_SCREEN_WIDTH, _SCREEN_HEIGHT = config.SCREEN_SIZE

_X_LEFT = -Bee.WIDTH
_X_RIGHT = _SCREEN_WIDTH
_X_ONE_THIRD = _SCREEN_WIDTH // 3 - Bee.WIDTH * 1.5
_X_TWO_THIRD = 2 * _SCREEN_WIDTH // 3 + Bee.WIDTH // 2
_X_CENTER = get_screen_center()[0] - Bee.WIDTH // 2

_Y_CENTER = get_screen_center()[1]
_Y_TWO_THIRD = _SCREEN_HEIGHT * 2 // 3
_Y = -Honey.HEIGHT


_HONEY_POSITIONS = (
    (_X_ONE_THIRD, _Y), (_X_CENTER, _Y), (_X_TWO_THIRD, _Y)
)

_BEES_POSITIONS = (
    ((_X_ONE_THIRD, _Y),),
    ((_X_CENTER, _Y),),
    ((_X_TWO_THIRD, _Y),),
    ((_X_ONE_THIRD, _Y), (_X_CENTER, _Y)),
    ((_X_ONE_THIRD, _Y), (_X_TWO_THIRD, _Y)),
    ((_X_CENTER, _Y), (_X_TWO_THIRD, _Y)),
)

_MOVING_BEES_POSITIONS = (
    ((_X_LEFT, _Y_CENTER), "RIGHT"),
    ((_X_RIGHT, _Y_CENTER), "LEFT"),
)


def _should_generate_honey() -> bool:
    return random.randint(0, 101) < (config.HONEY_SPAWN_CHANCE * 100)


def _should_generate_moving_bee() -> bool:
    return random.randint(0, 101) < (config.MOVING_BEE_SPAWN_CHANCE * 100)


def get_average_row(scrolling_speed: float) -> List[Entity]:
    entities: List[Entity] = []

    honey_pos = random.choice(_HONEY_POSITIONS) if _should_generate_honey() else None
    bees_positions = [pos for pos in list(random.choice(_BEES_POSITIONS)) if pos != honey_pos]

    if honey_pos is not None:
        entities.append(Honey(*honey_pos, scrolling_speed))

    for bee_pos in bees_positions:
        entities.append(Bee(*bee_pos, scrolling_speed))

    return entities


def get_moving_row(scrolling_speed: float, player_on_left: bool) -> List[Entity]:
    pos, direction = _MOVING_BEES_POSITIONS[1] if player_on_left else _MOVING_BEES_POSITIONS[0]
    return [MovingBee(*pos, scrolling_speed, direction)]


def get_extended_row(scrolling_speed: float, player_on_left: bool) -> List[Entity]:
    if _should_generate_moving_bee():
        return get_moving_row(scrolling_speed, player_on_left)
    return get_average_row(scrolling_speed)
