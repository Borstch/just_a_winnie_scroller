import random
from typing import List

from entities import Entity, MovingBee, BoomerangBee, ShiftingBee
from .average_generation import get_average_row
from .generation_conditions import _should_generate_moving_bee
from .common_positions import (
    _X_ONE_THIRD,
    _X_CENTER,
    _X_TWO_THIRD,
    _X_LEFT,
    _X_RIGHT,
    _Y,
    _Y_CENTER,
)


_MOVING_BEES_POSITIONS = (
    ((_X_LEFT, _Y_CENTER), "RIGHT"),
    ((_X_RIGHT, _Y_CENTER), "LEFT"),
)

_BOOMERANG_BEES_POSITIONS = (
    (_X_ONE_THIRD, _Y), (_X_CENTER, _Y), (_X_TWO_THIRD, _Y)
)

_SHIFTING_BEES_POSITIONS = (
    ((_X_ONE_THIRD, _Y), ShiftingBee.WIDTH),
    ((_X_CENTER, _Y), 3 * ShiftingBee.WIDTH),
    ((_X_TWO_THIRD, _Y), ShiftingBee.WIDTH),
)


def _get_moving_row(scrolling_speed: float, player_on_left: bool) -> List[Entity]:
    pos, direction = _MOVING_BEES_POSITIONS[1] if player_on_left else _MOVING_BEES_POSITIONS[0]
    return [MovingBee(*pos, scrolling_speed, direction)]


def _get_boomerang_row(scrolling_speed: float, _: bool) -> List[Entity]:
    pos = random.choice(_BOOMERANG_BEES_POSITIONS)
    return [BoomerangBee(*pos, scrolling_speed)]


def _get_shifting_row(scrolling_speed, _: bool) -> List[Entity]:
    pos, radius = random.choice(_SHIFTING_BEES_POSITIONS)
    direction = random.choice(("LEFT", "RIGHT"))
    return [ShiftingBee(*pos, scrolling_speed, direction, radius)]


_EXTENDED_GENERATORS = (
    _get_moving_row,
    _get_boomerang_row,
    _get_shifting_row,
)


def get_extended_row(scrolling_speed: float, player_on_left: bool) -> List[Entity]:
    if _should_generate_moving_bee():
        generator = random.choice(_EXTENDED_GENERATORS)
        return generator(scrolling_speed, player_on_left)
    return get_average_row(scrolling_speed)
