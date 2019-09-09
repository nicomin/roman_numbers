from app.galactic_prize_converter import GalacticPrizeConverter
from app.human_prize_converter import HumanPrizeConverter
from app.utils import Utils


class TranslationManager:
    HUMAN_MONEY_IDENTIFIER = 'Credits'
    GALACTIC_MONEY_IDENTIFIER = ''

    def __init__(self):
        self.items = {}
        self.utils = Utils()
        self.human_converter = HumanPrizeConverter()
        self.galatic_converter = GalacticPrizeConverter()

    def add_item(self, word: str, translation: str, currency_type: str = ''):
        item_values = {
            'translation': translation,
            'currency_type': currency_type
        }
        if currency_type == self.GALACTIC_MONEY_IDENTIFIER and not self.utils.check_roman_numerals(translation):
            raise ValueError('The input value "{}" is not a roman numeral'.format(translation))
        self.items.update({word: item_values})

    def translate_prize_phrase(self, foreign_phrase: str, asked_type: str = ''):
        if self._check_if_already_converted(foreign_phrase, asked_type):
            return foreign_phrase
        if foreign_phrase in self.items:
            return self._get_prize_by_asked_type(foreign_phrase, asked_type)
        words = foreign_phrase.split(sep=' ')
        translated_phrase = ''
        for w in words:
            try:
                translated_phrase += self.items[w]['translation']
            except KeyError:
                raise KeyError('The word "{}" is not registered in translator'.format(w))
        return self._translate_word(asked_type, translated_phrase)

    def _get_prize_by_asked_type(self, foreign_phrase: str, asked_type: str = ''):
        if asked_type == self.items[foreign_phrase]['currency_type']:
            return self.items[foreign_phrase]['translation']
        else:
            return self._translate_word(asked_type, self.items[foreign_phrase]['translation'])

    def _translate_word(self, type: str, word: str):
        return {
            'Credits': lambda word: self.galatic_converter.convert_to_human_prize(word),
            '': lambda word: self.human_converter.convert_to_galactic_prize(int(word))
        }[type](word)

    def _check_if_already_converted(self, foreign_phrase: str, asked_type: str = ''):
        return (
            (foreign_phrase.isdigit() and asked_type == self.HUMAN_MONEY_IDENTIFIER)
            or (
              foreign_phrase and not foreign_phrase.isdigit() and asked_type == ''
            )
        )



