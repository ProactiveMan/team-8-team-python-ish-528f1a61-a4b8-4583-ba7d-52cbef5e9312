from unittest import TestCase
from levelup.character import Character, InvalidMoveException
from levelup.map import GameMap, Direction
from levelup.position import Position


class TestCharacter(TestCase):
    def test_init(self):
        expected_name = "arbitrary"
        testobj = Character(expected_name)
        self.assertEqual(testobj.name, expected_name)
        expected_position = None
        self.assertEqual(testobj.position, expected_position)

    def test_get_name_default(self):
         FakeCharacter = Character(name=None)
         self.assertEqual(FakeCharacter.get_name(), "Character") 

    def test_get_name_Shorsey(self):
         FakeCharacter = Character(name="Shorsey")
         self.assertEqual(FakeCharacter.get_name(), "Shorsey")

    def test_enter_map(self):
        FakeCharacter = Character(name="Shorsey")
        FakeMap = GameMap()
        FakeCharacter.enter_map(FakeMap)
        pos = FakeCharacter.get_position()
        print(pos)
        #Should be born on 0,0
        self.assertEqual(Position(0,0), pos)
    
