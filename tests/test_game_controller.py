from unittest import TestCase
from unittest.mock import MagicMock, create_autospec
from levelup.controller import GameController, CharacterNotFoundException
from levelup.character import DEFAULT_CHARACTER_NAME, InvalidMoveException, Character
from levelup.position import Position
from fake_character import FakeCharacter
from fake_map import FakeMap, Direction


class TestGameController(TestCase):
    def test_init(self):
        testobj = GameController()
        self.assertEqual(testobj.status.move_count, 0)
        self.assertEqual(
            testobj.status.current_position,
            None,
        )
    
    def test_move(self):
        testobj = GameController()
        testobj.character = FakeCharacter(name="Steve")
        
        self.assertTrue(testobj.move(Direction.SOUTH))
    

    