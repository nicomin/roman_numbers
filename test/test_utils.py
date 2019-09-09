from unittest import TestCase

from app.utils import Utils


class TestUtils(TestCase):
    def setUp(self):
        self.utils = Utils

    def test_check_roman_numerals_when_input_is_not_a_str_then_return_false(self):
        self.assertFalse(self.utils.check_roman_numerals(9999))

    def test_check_roman_numerals_when_empty_input_then_return_false(self):
        self.assertFalse(self.utils.check_roman_numerals(''))

    def test_check_roman_numerals_when_input_is_not_a_roman_numeral_then_return_false(self):
        self.assertFalse(self.utils.check_roman_numerals('no soy un número romano'))
        self.assertFalse(self.utils.check_roman_numerals('XICI'))
        self.assertFalse(self.utils.check_roman_numerals('XXXXV'))
        self.assertFalse(self.utils.check_roman_numerals('VC'))
        self.assertFalse(self.utils.check_roman_numerals('MMMM'))
        self.assertFalse(self.utils.check_roman_numerals('LL'))
        self.assertFalse(self.utils.check_roman_numerals('MMMXM'))

    def test_check_roman_numerals_when_input_is_a_roman_numeral_then_return_true(self):
        self.assertTrue(self.utils.check_roman_numerals('MMXVIII'))
        self.assertTrue(self.utils.check_roman_numerals('XXXIX'))
