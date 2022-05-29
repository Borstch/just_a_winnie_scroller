import random

import config


def _should_generate_honey() -> bool:
    return random.randint(0, 101) < (config.HONEY_SPAWN_CHANCE * 100)


def _should_generate_moving_bee() -> bool:
    return random.randint(0, 101) < (config.MOVING_BEE_SPAWN_CHANCE * 100)
