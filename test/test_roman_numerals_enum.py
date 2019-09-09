from unittest import TestCase

from app.roman_numerals_enum import RomanNumeralEnum


class TestRomanNumeralsEnum(TestCase):
	def setUp(self):
		self.enum = RomanNumeralEnum

	def test_convert_to_galactic_money_when_invalid_input_then_raise_exception(self):
		input = 'G'
		self.assertRaises(ValueError, lambda: self.enum.convert_to_galactic_money(input))

	def test_convert_to_galactic_money_when_input_has_more_than_1_non_zero_digit_then_raise_exception(self):
		input = 15
		self.assertRaises(ValueError, lambda: self.enum.convert_to_galactic_money(input))

	def test_convert_to_galactic_money_when_valid_input_then_return_roman_number_str_value(self):
		self.assertEqual('V', self.enum.convert_to_galactic_money(5))

	def test_convert_to_galactic_money_when_valid_input_it_is_not_registered_as_simple_roman_numeral_then_return_compound_roman_numeral(self):
		self.assertEqual('VII', self.enum.convert_to_galactic_money(7))
		self.assertEqual('IX', self.enum.convert_to_galactic_money(9))
		self.assertEqual('XC', self.enum.convert_to_galactic_money(90))
		self.assertEqual('XL', self.enum.convert_to_galactic_money(40))
		self.assertEqual('XXX', self.enum.convert_to_galactic_money(30))
		self.assertEqual('LX', self.enum.convert_to_galactic_money(60))
		self.assertEqual('DCCC', self.enum.convert_to_galactic_money(800))
		self.assertEqual('CD', self.enum.convert_to_galactic_money(400))
		self.assertEqual('MMM', self.enum.convert_to_galactic_money(3000))

	def test_convert_to_human_money_when_invalid_input_then_raise_exception(self):
		input = 'G'
		self.assertRaises(KeyError, lambda: self.enum.convert_to_human_money(input))

	def test_convert_to_human_money_when_valid_input_then_return_human_prize_value(self):
		self.assertEqual(self.enum.V, self.enum.convert_to_human_money('V'))

	def test_get_roman_numeral_enum_by_digits_len_when_input_has_more_than_3_zero_digits_then_raise_exception(self):
		to_convert_number = 50000
		zeros_quantity = len(str(to_convert_number)) - 1
		self.assertRaises(KeyError, lambda: self.enum._get_roman_numeral_enum_by_digits_len(zeros_quantity))

	def test_get_roman_numeral_enum_by_digits_len_is_lower_than_4_then_return_roman_numeral_position_range(self):
		to_convert_number = 600
		zeros_quantity = len(str(to_convert_number)) - 1
		position_range = self.enum._get_roman_numeral_enum_by_digits_len(zeros_quantity)
		self.assertEqual('C', position_range[0])
		self.assertEqual('D', position_range[1])



