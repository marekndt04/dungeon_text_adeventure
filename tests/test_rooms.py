import unittest

from dungeon_text_adeventure.rooms import MonsterRoom, SimpleRoom, TreasureRoom


class TestSimpleRoom(unittest.TestCase):
    def test_simple_room_string_representation(self):
        self.assertEqual(str(SimpleRoom()), "Modest Chambers")

    def test_simple_room_enter(self):
        expected_message = "You have entered Modest Chambers."
        self.assertEqual(SimpleRoom().enter(), expected_message)


class TestMonsterRoom(unittest.TestCase):
    def test_monster_room_string_representation(self):
        self.assertEqual(str(MonsterRoom()), "Monster Room")

    def test_monster_room_enter(self):
        expected_message = "You have entered Monster Room."
        self.assertEqual(MonsterRoom().enter(), expected_message)


class TestTreasureRoom(unittest.TestCase):
    def test_treasure_room_string_representation(self):
        self.assertEqual(str(TreasureRoom()), "Treasure Room")

    def test_treasure_room_enter(self):
        expected_message = "You have entered Treasure Room."
        self.assertEqual(TreasureRoom().enter(), expected_message)
