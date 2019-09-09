from enum import Enum
from typing import Tuple


class RomanNumeralEnum(Enum):
	UNDEFINED = 0
	I = 1
	V = 5
	X = 10
	L = 50
	C = 100
	D = 500
	M = 1000

	def _get_next_level_item_name(self):
		value = self.value * 2
		return RomanNumeralEnum(value).name

	@classmethod
	def convert_to_galactic_money(cls, currency_value: int):
		try:
			return cls(currency_value).name
		except ValueError:
			return cls._break_down_human_money_digits(currency_value)

	@classmethod
	def convert_to_human_money(cls, galactical_value: str):
		return cls[galactical_value]

	@classmethod
	def _break_down_human_money_digits(cls, currency_value: int) -> str:
		digits = str(currency_value)
		non_zero_digits = [x for x in digits if not x == '0']
		if len(non_zero_digits) > 1:
			raise ValueError('Unexpected simple digit input: "{}"'.format(digits))
		digits_len = len(digits) - 1
		one_roman_numeral, five_roman_numeral = cls._get_roman_numeral_enum_by_digits_len(digits_len)
		digits_interpreter = {
			1: one_roman_numeral,
			5: five_roman_numeral
		}
		assessed_digit = int(digits[0])
		converted_value = ''
		if assessed_digit == 4:
			return digits_interpreter[1] + digits_interpreter[5]
		elif assessed_digit - 5 == 4:
			return digits_interpreter[1] + cls[digits_interpreter[5]]._get_next_level_item_name()
		elif assessed_digit - 5 > 0:
			assessed_digit -= 5
			converted_value = digits_interpreter[5]
		for _ in range(1, assessed_digit + 1):
			converted_value += digits_interpreter[1]
		return converted_value

	@classmethod
	def _get_roman_numeral_enum_by_digits_len(cls, digits_len: int) -> Tuple:
		return {
			0: (RomanNumeralEnum.I.name, RomanNumeralEnum.V.name),
			1: (RomanNumeralEnum.X.name, RomanNumeralEnum.L.name),
			2: (RomanNumeralEnum.C.name, RomanNumeralEnum.D.name),
			3: (RomanNumeralEnum.M.name, '')
		}[digits_len]
