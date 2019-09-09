from typing import Tuple

from app.roman_numerals_enum import RomanNumeralEnum
from app.utils import Utils


class GalacticPrizeConverter:
	"""Save and process galactical prizes"""
	def __init__(self):
		self.utils = Utils

	def convert_to_human_prize(self, galactic_prize: str):
		if not self.utils.check_roman_numerals(galactic_prize):
			raise ValueError('The galactic prize "{}" is not a roman numeral'.format(galactic_prize))
		chars = list(galactic_prize)
		last_galactic_prize_value = RomanNumeralEnum.UNDEFINED
		human_prize = 0
		for char in chars:
			gotten_prize, last_galactic_prize_value = self._get_roman_numeral(last_galactic_prize_value, char)
			human_prize += gotten_prize
		if last_galactic_prize_value:
			human_prize += last_galactic_prize_value.value
		return human_prize

	def _get_roman_numeral(self, last_galactic_prize_value: RomanNumeralEnum, content: str) -> Tuple[int, int]:
		human_prize = 0
		try:
			char_prize = RomanNumeralEnum.convert_to_human_money(content)
			if last_galactic_prize_value is RomanNumeralEnum.UNDEFINED:
				last_galactic_prize_value = char_prize
			elif last_galactic_prize_value.value < char_prize.value:
				human_prize = (char_prize.value - last_galactic_prize_value.value)
				last_galactic_prize_value = RomanNumeralEnum.UNDEFINED
			else:
				human_prize = last_galactic_prize_value.value
				last_galactic_prize_value = char_prize
		except KeyError:
			raise
		else:
			return human_prize, last_galactic_prize_value
