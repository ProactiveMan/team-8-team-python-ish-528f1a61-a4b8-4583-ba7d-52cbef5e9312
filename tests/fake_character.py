from levelup.position import Position
from levelup.character import Character
from levelup.map import Direction

class FakeCharacter(Character):
    
    position: Position(0, 0)

    def move(self, direction: Direction):
        self.position = Position(0, 1)
    