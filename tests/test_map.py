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
    
    def test_get_total_positions(self):
        testmap = GameMap()
        total_positions = testmap.get_total_positions()
        self.assertEqual(total_positions, 100)
    
    def test_is_valid_position_good(self):
        # Testing lower limit boundary
        testmap = GameMap()
        pos = Position(0, 0)
        self.assertTrue(testmap.is_valid_position(pos))
    
    def test_is_valid_position_good_2(self):
        # Testing upper limit boundary
        testmap = GameMap()
        pos = Position(testmap.size[0], testmap.size[1])

    def test_is_valid_position_fail_x(self):
        testmap = GameMap()
        # Size exceeds the bound by 1.
        pos = Position(testmap.size[0], 0)
        self.assertFalse(testmap.is_valid_position(pos))
    
    def test_is_valid_position_fail_y(self):
        testmap = GameMap()
        # Size exceeds the bound by 1.
        pos = Position(0, testmap.size[1])
        self.assertFalse(testmap.is_valid_position(pos))
    
    def test_is_valid_position_fail_neg_x(self):
        testmap = GameMap()
        pos = Position(-1, 0)
        self.assertFalse(testmap.is_valid_position(pos))

    def test_is_valid_position_fail_neg_y(self):
        testmap = GameMap()
        pos = Position(0, -1)
        self.assertFalse(testmap.is_valid_position(pos))
    
    def test_calculate_position_valid_1(self):
        pass

    def test_calculate_position_valid_2(self):
        pass

    def test_calculate_position_edge_1(self):
        pass

    def test_calculate_position_edge_2(self):
        pass