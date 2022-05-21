import random
from typing import List

import config
from entities import Entity, Bee, MovingBee, Honey
from utils import get_screen_center


_SCREEN_WIDTH = config.SCREEN_SIZE[0]
_X_ONE_THIRD = _SCREEN_WIDTH // 3 - Bee.WIDTH * 1.5
_X_TWO_THIRD = 2 * _SCREEN_WIDTH // 3 + Bee.WIDTH // 2
_X_CENTER = get_screen_center()[0] - Bee.WIDTH // 2

_Y = -Honey.HEIGHT

_POSITIONS = (
    ((_X_ONE_THIRD, _Y),),
    ((_X_CENTER, _Y),),
    ((_X_TWO_THIRD, _Y),),
    ((_X_ONE_THIRD, _Y), (_X_CENTER, _Y)),
    ((_X_ONE_THIRD, _Y), (_X_TWO_THIRD, _Y)),
    ((_X_CENTER, _Y), (_X_TWO_THIRD, _Y)),
    ((_X_ONE_THIRD, _Y), (_X_CENTER, _Y), (_X_TWO_THIRD, _Y)),
)


def _should_generate_honey() -> bool:
    return random.randint(0, 101) < (config.HONEY_PROBABILITY * 100)


def get_row(scrolling_speed: float) -> List[Entity]:
    positions = list(random.choice(_POSITIONS))
    entities: List[Entity] = []

    if len(positions) == 1:
        moving_bee_pos = positions.pop()
        direction = random.choice(["LEFT", "RIGHT"])
        entities.append(MovingBee(*moving_bee_pos, scrolling_speed, direction))
    elif len(positions) == 3 or _should_generate_honey():
        honey_pos = random.choice(positions)
        positions.pop(positions.index(honey_pos))
        entities.append(Honey(*honey_pos, scrolling_speed))

    for pos in positions:
        entities.append(Bee(*pos, scrolling_speed))

    return entities
