from unittest import TestCase
from unittest.mock import MagicMock

from app.galactic_prize_converter import GalacticPrizeConverter
from app.utils import Utils


class TestGalacticPrizeConverter(TestCase):
    def setUp(self):
        self.galactic_mod = GalacticPrizeConverter()
        self.utils = MagicMock(Utils)
        self.galactic_mod.utils = self.utils

    def test_convert_to_human_prize_when_invalid_roman_numeral_then_raise_exception_and_do_not_set_human_prize(self):
        self.utils.check_roman_numerals.return_value = False
        self.assertRaises(ValueError, lambda: self.galactic_mod.convert_to_human_prize('XX'))

    def test_convert_to_human_prize_when_input_has_at_least_one_non_identified_character_then_raise_exception(self):
        galactic_prize = 'XLVB'
        self.assertRaises(KeyError, lambda: self.galactic_mod.convert_to_human_prize(galactic_prize))

    def test_convert_to_human_prize_when_input_char_has_only_len_of_1_then_convert_it_and_return_its_value(self):
        galactic_prize = 'C'
        self.assertEqual(100, self.galactic_mod.convert_to_human_prize(galactic_prize))

    def test_convert_to_human_prize_when_last_saved_char_value_is_lower_than_read_char_value_then_set_human_prize_as_read_char_value_minus_last_saved_char_value(self):
        galactic_prize = 'IX'
        self.assertEqual(9, self.galactic_mod.convert_to_human_prize(galactic_prize))

    def test_convert_to_human_prize_when_input_has_more_than_two_chars_then_recalculate_values_with_same_used_logic(self):
        galactic_prize = 'MMIX'
        self.assertEqual(2009, self.galactic_mod.convert_to_human_prize(galactic_prize))
        galactic_prize = 'MMDCCXLVIII'
        self.assertEqual(2748, self.galactic_mod.convert_to_human_prize(galactic_prize))
