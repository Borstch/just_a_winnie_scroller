import config
import utils
from .bee import Bee


class BoomerangBee(Bee):
    def __init__(self, x: float, y: float, scrolling_speed: float):
        super(BoomerangBee, self).__init__(x, y, scrolling_speed)
        self._sprites = [
            utils.load_image(sprite_path, width=self.WIDTH, height=self.HEIGHT)
            for sprite_path in config.ANGRY_BEE_SPRITES_PATH
        ]
        self._going_back = False
        self._remaining_turns = 2

    def update(self, scrolling_speed: float) -> None:
        if self._should_turn_around():
            self._turn_around()

        if self._going_back:
            scrolling_speed = -scrolling_speed
        super(BoomerangBee, self).update(scrolling_speed)

    def _should_turn_around(self) -> bool:
        if self._remaining_turns < 1:
            return False

        if self._going_back:
            return self._y < (config.SCREEN_SIZE[1] - 2 * self.HEIGHT)
        return self._y > (config.SCREEN_SIZE[1] - self.HEIGHT // 2)

    def _turn_around(self) -> None:
        self._going_back = not self._going_back
        self._remaining_turns -= 1
