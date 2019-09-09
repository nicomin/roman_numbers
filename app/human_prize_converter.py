from app.roman_numerals_enum import RomanNumeralEnum


class HumanPrizeConverter:
    MIN_ROMAN_NUMERAL = 1
    MAX_ROMAN_NUMERAL = 3999

    def _check_convertible_value(self, prize: int):
        if prize < self.MIN_ROMAN_NUMERAL or prize > self.MAX_ROMAN_NUMERAL:
            raise ValueError('The number "{}" cannot be converted to roman numeral'.format(prize))

    def convert_to_galactic_prize(self, prize):
        self._check_convertible_value(prize)
        prize_str = str(int(prize))
        number_of_digits = len(prize_str)
        galactic_prize = ''
        for index, char in enumerate(prize_str, 1):
            digit = int(char)
            if not digit:
                continue
            pos = number_of_digits - index
            to_convert = digit * 10**pos
            galactic_prize += RomanNumeralEnum.convert_to_galactic_money(to_convert)
        return galactic_prize


