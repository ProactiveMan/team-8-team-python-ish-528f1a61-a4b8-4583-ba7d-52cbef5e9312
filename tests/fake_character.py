from levelup.position import Position
from levelup.character import Character
from fake_map import Direction, FakeMap

class FakeCharacter(Character):
    
    position: Position(0, 0)

    def enter_map(self, game_map: FakeMap):
        return True

    def move(self, direction: Direction):
        return True
    