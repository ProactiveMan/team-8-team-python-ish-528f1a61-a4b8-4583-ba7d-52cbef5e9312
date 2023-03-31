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
         self.assertEqual(FakeCharacter.get_name(), "Shoresy") 

    def test_get_name_Shorsey(self):
         FakeCharacter = Character(name="Shorsey")
         self.assertEqual(FakeCharacter.get_name(), "Shorsey")

    def test_enter_map(self):
        FakeCharacter = Character(name="Shorsey")
        FakeMap = GameMap()
        FakeCharacter.enter_map(FakeMap)
        pos = FakeCharacter.get_position()
        #Should be born on 0,0
        self.assertEqual(Position(0,0), pos)

    def test_get_position(self):
        FakeCharacter = Character(name="Shorsey")
        FakeMap = GameMap()
        FakeCharacter.enter_map(FakeMap)
        pos = FakeCharacter.get_position()
        self.assertIsInstance(pos,Position)
    
    def test_move_valid_destination(self):   
        FakeCharacter = Character(name="Shorsey")
        FakeMap = GameMap()
        NewPos = FakeMap.calculate_position(Position(0,0),Direction.SOUTH)
        self.assertIsInstance(NewPos,Position)
