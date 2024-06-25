import unittest

from dungeon_text_adeventure.classes import Warrior, Mage, Rogue

class TestWarriorClass(unittest.TestCase):

    def setUp(self):
        self.warrior = Warrior("John")

    def test_warrior_init(self):
        self.assertEqual(self.warrior.health, 100)
    
    def test_warrior_string_representation(self):
        self.assertEqual(str(self.warrior), "John the Warrior")

    def test_attack(self):
        self.assertEqual(self.warrior.attack(), 10)

    def test_take_damage(self):
        self.warrior.take_damage(10)
        self.assertEqual(self.warrior.health, 90)

    def test_is_alive_after_non_lethal_damage(self):
        self.warrior.take_damage(99)
        self.assertTrue(self.warrior.is_alive())

    def test_is_alive_after_lethal_damage(self):
        self.warrior.take_damage(100)
        self.assertFalse(self.warrior.is_alive())


class TestMageClass(unittest.TestCase):

    def setUp(self):
        self.mage = Mage("Jane")

    def test_mage_init(self):
        self.assertEqual(self.mage.health, 50)
    
    def test_mage_string_representation(self):
        self.assertEqual(str(self.mage), "Jane the Mage")

    def test_attack(self):
        self.assertEqual(self.mage.attack(), 20)

    def test_take_damage(self):
        self.mage.take_damage(10)
        self.assertEqual(self.mage.health, 40)

    def test_is_alive_after_non_lethal_damage(self):
        self.mage.take_damage(49)
        self.assertTrue(self.mage.is_alive())

    def test_is_alive_after_lethal_damage(self):
        self.mage.take_damage(50)
        self.assertFalse(self.mage.is_alive())


class TestRogueClass(unittest.TestCase):

    def setUp(self):
        self.rogue = Rogue("Jim")

    def test_rogue_init(self):
        self.assertEqual(self.rogue.health, 75)
    
    def test_rogue_string_representation(self):
        self.assertEqual(str(self.rogue), "Jim the Rogue")

    def test_attack(self):
        self.assertEqual(self.rogue.attack(), 15)

    def test_take_damage(self):
        self.rogue.take_damage(10)
        self.assertEqual(self.rogue.health, 65)

    def test_is_alive_after_non_lethal_damage(self):
        self.rogue.take_damage(74)
        self.assertTrue(self.rogue.is_alive())

    def test_is_alive_after_lethal_damage(self):
        self.rogue.take_damage(75)
        self.assertFalse(self.rogue.is_alive())
