from .moving_bee import MovingBee, MovementDirection


class ShiftingBee(MovingBee):
    def __init__(
            self, x: float, y: float, scrolling_speed: float, direction: MovementDirection, shifting_radius: int
    ):
        super(ShiftingBee, self).__init__(x, y, scrolling_speed, direction)
        self._shifting_center = x
        self._shifting_radius = shifting_radius

    def update(self, scrolling_speed: float) -> None:
        if self._should_change_direction():
            self._change_direction()
        super(ShiftingBee, self).update(scrolling_speed)

    def _culc_movement_direction(self) -> float:
        speed = super(ShiftingBee, self)._culc_movement_direction()
        return self._HORIZONTAL_MOVEMENT_SCALE * speed

    def _should_change_direction(self) -> bool:
        if self._direction == "LEFT":
            return self._x < (self._shifting_center - self._shifting_radius)
        if self._direction == "RIGHT":
            return self._x > (self._shifting_center + self._shifting_radius)
        return False

    def _change_direction(self) -> None:
        if self._direction == "LEFT":
            self._direction = "RIGHT"
        elif self._direction == "RIGHT":
            self._direction = "LEFT"
        else:
            raise ValueError(
                f"Direction expected to be a string literal 'LEFT' or 'RIGHT' but got {self._direction}"
            )

        self._flip_sprites()

    _HORIZONTAL_MOVEMENT_SCALE = 0.4
