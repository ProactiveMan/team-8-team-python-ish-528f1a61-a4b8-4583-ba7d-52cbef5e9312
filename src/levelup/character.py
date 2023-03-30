from levelup.position import Position
from levelup.map import GameMap, Direction

DEFAULT_CHARACTER_NAME = "Character"


class InvalidMoveException(Exception):
    pass


class Character:
    name: str
    map: GameMap = None
    position: Position = None

    def __init__(self, name: str):
        self.name = name or DEFAULT_CHARACTER_NAME
        
    def get_name(self):
        return self.name

    def get_position(self):
        return self.position
#        print(self.position)

    def enter_map(self, game_map: GameMap):
        self.map = game_map
        self.position = self.map.starting_position
#        print(self.position)
        return self.position

    def move(self, direction: Direction):
        pass
