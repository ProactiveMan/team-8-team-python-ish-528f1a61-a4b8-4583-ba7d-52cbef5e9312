import logging
from dataclasses import dataclass
from levelup.character import Character, DEFAULT_CHARACTER_NAME, InvalidMoveException
from levelup.map import Direction, GameMap
from levelup.position import Position


@dataclass
class GameStatus:
    move_count: int = 0
    running: bool = False
    current_position: Position = None

    def __str__(self):
        return f"Moved {self.move_count} times, currently on position {self.current_position}"


class CharacterNotFoundException(Exception):
    pass


class GameController:
    status: GameStatus
    character: Character

    def __init__(self):
        self.status = GameStatus()
        self.character = None
        self.map = GameMap()

    def start_game(self):
        if hasattr(self, "character"):
            self.character.enter_map(self.map)
            self.status.current_position = self.character.position
            self.set_character_position(self.map.starting_position)
        else:
            raise CharacterNotFoundException("Character not found")

    def create_character(self, name: str) -> None:
        if name is not None and name != "":
            self.character = Character(name)
        else:
            self.character = Character(DEFAULT_CHARACTER_NAME)
        self.status.character_name = self.character.name

    def move(self, direction: Direction) -> None:
        self.status.move_count += 1
        resp = self.character.move(direction)
        self.status.current_position = self.character.get_position()
        return resp

    def set_character_position(self, position: Position):
        self.character.position = position

    def get_total_positions(self):
        return self.map.position_count
