import random
from typing import List

from entities import Entity, MovingBee, BoomerangBee, ShiftingBee
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


def get_moving_row(scrolling_speed: float, player_on_left: bool) -> List[Entity]:
    pos, direction = _MOVING_BEES_POSITIONS[1] if player_on_left else _MOVING_BEES_POSITIONS[0]
    return [MovingBee(*pos, scrolling_speed, direction)]


def get_boomerang_row(scrolling_speed: float, _: bool) -> List[Entity]:
    pos = random.choice(_BOOMERANG_BEES_POSITIONS)
    return [BoomerangBee(*pos, scrolling_speed)]


def get_shifting_row(scrolling_speed, _: bool) -> List[Entity]:
    pos, radius = random.choice(_SHIFTING_BEES_POSITIONS)
    direction = random.choice(("LEFT", "RIGHT"))
    return [ShiftingBee(*pos, scrolling_speed, direction, radius)]
