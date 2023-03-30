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
        # Create pos array
        x_axis = self.size[0]
        y_axis = self.size[1]

        self.positions = []
        x_positions = [x for x in range(x_axis)]
        y_positions = [y for y in range(y_axis)]
        
        for x in x_positions:
            for y in y_positions:
                self.positions.append(Position(x, y))
        
        self.position_count = len(self.positions)

    def get_postions(self):
        return self.positions
    
    def get_total_positions(self):
        return self.position_count

    def is_valid_position(self, position: Position) -> bool:
        pass

    def calculate_position(
        self, starting_position: Position, direction: Direction
    ) -> Position:
        pass
