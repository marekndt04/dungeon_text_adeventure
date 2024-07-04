import io
import unittest
from unittest.mock import patch

from dungeon_text_adeventure.hostile_npcs import Dragon, LesserDemon, Troll


class TestDragonClass(unittest.TestCase):
    def test_dragon_init(self):
        dragon = Dragon()
        self.assertEqual(dragon.health, 25)

    def test_dragon_attack(self):
        self.assertEqual(Dragon().attack(), 20)

    def test_dragon_take_damage(self):
        dragon = Dragon()
        dragon.take_damage(10)
        self.assertEqual(dragon.health, 15)

    def test_dragon_is_alive_after_non_lethal_damage(self):
        dragon = Dragon()
        dragon.take_damage(19)
        self.assertTrue(dragon.is_alive())

    def test_dragon_is_alive_after_lethal_damage(self):
        dragon = Dragon()
        dragon.take_damage(30)
        self.assertFalse(dragon.is_alive())

    def test_string_representation(self):
        self.assertEqual(str(Dragon()), "The Dragon, eater of worlds")


class TestTrollClass(unittest.TestCase):
    def test_troll_init(self):
        troll = Troll()
        self.assertEqual(troll.health, 20)

    def test_troll_attack(self):
        self.assertEqual(Troll().attack(), 10)

    def test_troll_take_damage(self):
        troll = Troll()
        troll.take_damage(10)
        self.assertEqual(troll.health, 10)

    def test_troll_is_alive_after_non_lethal_damage(self):
        troll = Troll()
        troll.take_damage(19)
        self.assertTrue(troll.is_alive())

    def test_troll_is_alive_after_lethal_damage(self):
        troll = Troll()
        troll.take_damage(20)
        self.assertFalse(troll.is_alive())

    def test_string_representation(self):
        self.assertEqual(str(Troll()), "The Troll, destroyer of dreams")


class TestLesserDemonClass(unittest.TestCase):
    def test_lesser_demon_init(self):
        lesser_demon = LesserDemon()
        self.assertEqual(lesser_demon.health, 15)

    def test_lesser_demon_attack(self):
        self.assertEqual(LesserDemon().attack(), 10)

    def test_lesser_demon_take_damage(self):
        lesser_demon = LesserDemon()
        lesser_demon.take_damage(10)
        self.assertEqual(lesser_demon.health, 5)

    def test_lesser_demon_is_alive_after_non_lethal_damage(self):
        lesser_demon = LesserDemon()
        lesser_demon.take_damage(9)
        self.assertTrue(lesser_demon.is_alive())

    def test_lesser_demon_is_alive_after_lethal_damage(self):
        lesser_demon = LesserDemon()
        lesser_demon.take_damage(20)
        self.assertFalse(lesser_demon.is_alive())

    def test_string_representation(self):
        self.assertEqual(str(LesserDemon()), "The Lesser Demon, a harbinger of chaos")
