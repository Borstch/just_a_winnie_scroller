import random
from typing import List

from entities import Entity, Bee, Honey
from .common_positions import (
    _X_ONE_THIRD, _X_CENTER, _X_TWO_THIRD, _Y
)

_BEES_POSITIONS = (
    ((_X_ONE_THIRD, _Y),),
    ((_X_CENTER, _Y),),
    ((_X_TWO_THIRD, _Y),),
    ((_X_ONE_THIRD, _Y), (_X_CENTER, _Y)),
    ((_X_ONE_THIRD, _Y), (_X_TWO_THIRD, _Y)),
    ((_X_CENTER, _Y), (_X_TWO_THIRD, _Y)),
)

_HONEY_POSITIONS = (
    (_X_ONE_THIRD, _Y), (_X_CENTER, _Y), (_X_TWO_THIRD, _Y)
)


def get_average_row(scrolling_speed: float, generate_honey: bool) -> List[Entity]:
    entities: List[Entity] = []

    honey_pos = random.choice(_HONEY_POSITIONS) if generate_honey else None
    bees_positions = [pos for pos in list(random.choice(_BEES_POSITIONS)) if pos != honey_pos]

    if honey_pos is not None:
        entities.append(Honey(*honey_pos, scrolling_speed))

    for bee_pos in bees_positions:
        entities.append(Bee(*bee_pos, scrolling_speed))

    return entities
