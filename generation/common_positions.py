import config
from entities import Bee, Honey
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
