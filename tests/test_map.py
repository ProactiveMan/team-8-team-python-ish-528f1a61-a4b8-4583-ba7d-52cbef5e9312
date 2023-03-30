from unittest import TestCase
from typing import List
from levelup.map import GameMap
from levelup.position import Position


class TestMap(TestCase):
    def test_init(self):
        testmap = GameMap()
        self.assertEqual(testmap.starting_position, Position(0, 0))
        self.assertEqual(testmap.position_count, 100)
        for pos in testmap.positions:
            self.assertIsInstance(pos, Position)

    def test_get_positions(self):
        testmap = GameMap()
        positions = testmap.get_postions()
        for pos in positions:
            self.assertIsInstance(pos, Position)