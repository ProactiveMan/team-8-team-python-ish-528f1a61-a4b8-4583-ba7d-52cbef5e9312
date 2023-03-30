from levelup.controller import GameController
from levelup.controller import Direction
from levelup.position import Position
from levelup.map import Direction, GameMap


class MoveLibrary:
    start_x: int
    start_y: int

    def initialize_character_xposition_with(self, x_position):
        self.start_x = x_position

    def initialize_character_yposition_with(self, y_position):
        self.start_y = y_position

    def initialize_character_moveCount_with(self, move_count):
        pass

    def move_in_direction(self, direction):
        self.controller = GameController()
        self.controller.set_character_position((self.start_x, self.start_y))

        self.controller.move(Direction[direction])

    def character_xposition_should_be(self, expected):
        raise AssertionError("Not implemented")

    def character_yposition_should_be(self, expected):
        raise AssertionError("Not implemented")

    def character_moveCount_should_be(self, expected):
        raise AssertionError("Not implemented")
