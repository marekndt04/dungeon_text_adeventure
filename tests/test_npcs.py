import io
import unittest
from unittest.mock import patch

from dungeon_text_adeventure.npcs import HealerNPC, MysticMerchant


class TestHealerNPCClass(unittest.TestCase):
    def test_string_representation(self):
        self.assertEqual(str(HealerNPC()), "Guen the Healer")

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_interact_print_correct_message(self, mock_stdout):
        npc = HealerNPC()
        npc.interact()
        self.assertEqual(
            mock_stdout.getvalue().strip(), "You've been healed by Guen the Healer.... for 40 HP!"
        )

    def test_interact_return_hp_value(self):
        self.assertEqual(HealerNPC().interact(), 40)


class TestMysticMerchantClass(unittest.TestCase):
    def test_string_representation(self):
        self.assertEqual(str(MysticMerchant()), "Eldric the Mystic Merchant")

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_interact_print_correct_message(self, mock_stdout):
        npc = MysticMerchant()
        npc.interact()
        self.assertEqual(
            mock_stdout.getvalue().strip(),
            "Welcome to my shop, I have many wares for sale. Take this treasue key for free!",
        )

    def test_interact_return_zero(self):
        self.assertEqual(MysticMerchant().interact(), 0)
