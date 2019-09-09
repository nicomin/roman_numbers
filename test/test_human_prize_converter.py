from unittest import TestCase
from unittest.mock import MagicMock

from app.human_prize_converter import HumanPrizeConverter
from app.utils import Utils


class TestHumanPrizeConverter(TestCase):
    def setUp(self):
        self.human_mod = HumanPrizeConverter()
        self.utils = MagicMock(Utils)

    def test_check_convertable_value_when_invalid_input_then_raise_exception(self):
        prize = 'a prize'
        self.assertRaises(TypeError, lambda: self.human_mod.convert_to_galactic_prize(prize))

    def test_check_convertable_value_when_value_is_lower_than_1_or_greater_than_3999_then_raise_exception(self):
        prize = 0
        self.assertRaises(ValueError, lambda: self.human_mod.convert_to_galactic_prize(prize))
        prize = 4000
        self.assertRaises(ValueError, lambda: self.human_mod.convert_to_galactic_prize(prize))

    def test_convert_to_galactic_prize_when_value_is_ok_then_break_down_it_in_digits_and_convert_them_one_by_one_unless_its_value_0(self):
        prize = 3648
        self.assertEqual('MMMDCXLVIII', self.human_mod.convert_to_galactic_prize(prize))
        prize = 3333
        self.assertEqual('MMMCCCXXXIII', self.human_mod.convert_to_galactic_prize(prize))
        prize = 2999
        self.assertEqual('MMCMXCIX', self.human_mod.convert_to_galactic_prize(prize))

