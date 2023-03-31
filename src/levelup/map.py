from enum import Enum
from typing import Tuple, List
from levelup.position import Position


class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    EAST = "e"
    WEST = "w"


class GameMap:
    starting_position: Position = Position(0, 0)
    size: Tuple[int, int] = (10, 10)
    position_count: int
    positions: List[Position]

    def __init__(self):
        self.create_positions()

    def create_positions(self) -> None:
        self.positions = []
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                self.positions.append(Position(x, y))
        
        self.position_count = len(self.positions)

    def get_postions(self):
        return self.positions
    
    def get_total_positions(self):
        return self.position_count

    def is_valid_position(self, position: Position) -> bool:
        x, y = position.coordinates
        if x in range(self.size[0]) and y in range(self.size[1]):
            return True
        else:
            return False

    def calculate_position(
        self, starting_position: Position, direction: Direction
    ) -> Position:
        x, y = starting_position.coordinates
        if direction is Direction.NORTH:
            y -= 1
        elif direction is Direction.SOUTH:
            y += 1
        elif direction is Direction.EAST:
            x += 1
        elif direction is Direction.WEST:
            x -= 1
        
        new_position = Position(x, y)
        if self.is_valid_position(new_position):
            return new_position
        else:
            return starting_position