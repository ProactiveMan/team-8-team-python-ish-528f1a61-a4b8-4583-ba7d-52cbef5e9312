from levelup.map import GameMap
from levelup.position import Position

class FakeMap(GameMap):

    def calculate_position(self, starting_position: Position, direction: Direction
    ) -> Position:
        return Position(0, 0)