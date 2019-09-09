import re


class Utils:

    @staticmethod
    def check_roman_numerals(roman_numerals: str):
        if not isinstance(roman_numerals, str) or not roman_numerals:
            return False
        regex_pattern = re.compile(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")
        return regex_pattern.match(roman_numerals)
