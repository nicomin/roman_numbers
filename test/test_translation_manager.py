from unittest import TestCase
from unittest.mock import MagicMock

from app.translation_manager import TranslationManager


class TestProductManager(TestCase):

    def setUp(self):
        self.manager = TranslationManager()

    def test_add_product_when_product_name_add_new_product_to_products_with_input_prizes_and_calculate_missing_values(self):
        self.manager.add_item('manchana', '3000', 'Credits')
        self.assertEqual('3000', self.manager.items['manchana']['translation'])
        self.manager.add_item('melons', 'CMXC')
        self.assertEqual('CMXC', self.manager.items['melons']['translation'])

    def test_get_prize_by_asked_type_when_asked_type_is_same_than_saved_currency_type_then_return_translated_value(self):
        self.manager.add_item('manchana', '3000', 'Credits')
        self.assertEqual('3000', self.manager._get_prize_by_asked_type('manchana', 'Credits'))

    def test_get_prize_by_asked_type_when_asked_type_is_different_from_saved_currency_type_then_translate_saved_value_to_asked_type_and_return_it(self):
        self.manager.add_item('durazno', '3000', 'Credits')
        self.assertEqual('MMM', self.manager._get_prize_by_asked_type('durazno', ''))
        self.assertEqual('3000', self.manager._get_prize_by_asked_type('durazno', 'Credits'))
        self.manager.add_item('meloncio', 'DCCCXL', '')
        self.assertEqual('DCCCXL', self.manager._get_prize_by_asked_type('meloncio', ''))
        self.assertEqual(840, self.manager._get_prize_by_asked_type('meloncio', 'Credits'))

    def test_translate_prize_phrase_when_foreign_phrase_match_directly_with_saved_items_then_return_get_prize_by_asked_type_fnc_value(self):
        self.manager._get_prize_by_asked_type = MagicMock()
        self.manager._get_prize_by_asked_type.return_value = 'some value'
        self.manager.add_item('frambuesa', '456', 'Credits')
        self.assertEqual('some value', self.manager.translate_prize_phrase('frambuesa', 'Credits'))
        self.manager._get_prize_by_asked_type.assert_called_once_with('frambuesa', 'Credits')

    def test_translate_prize_phrase_when_foreign_phrase_is_already_translated_to_asked_type_then_return_it(self):
        self.manager.add_item('frambuesa', '456', 'Credits')
        self.assertEqual('456', self.manager.translate_prize_phrase('frambuesa', 'Credits'))

    def test_translate_prize_phrase_when_some_foreign_word_is_not_registered_in_translator_then_raise_exception(self):
        self.manager.add_item('coco', '456', 'Credits')
        with self.assertRaises(KeyError) as cm:
            self.manager.translate_prize_phrase('frambuesa frutilla', 'Credits')
        self.assertEqual('The word "frambuesa" is not registered in translator', cm.exception.args[0])

    def test_translate_prize_phrase_when_all_words_match_is_ok_then_translate_entire_phrase_to_requested_type(self):
        self.manager.add_item('tuna', 'I', '')
        self.manager.add_item('aceituna', 'V', '')
        self.manager.add_item('sandia', 'X', '')
        self.assertEqual(26, self.manager.translate_prize_phrase('sandia sandia aceituna tuna', 'Credits'))

    def test_check_if_already_converted_when_arabic_numeral_and_human_money_identifier_then_return_true(self):
        self.assertTrue(self.manager._check_if_already_converted('654', 'Credits'))

    def test_check_if_already_converted_when_there_are_characters_phrase_and_no_money_identifier_then_return_true(self):
        self.assertTrue(self.manager._check_if_already_converted('ksdjfh dsi', ''))

    def test_check_if_already_converted_when_there_are_arabic_numeral_and_no_identifier_then_return_false(self):
        self.assertFalse(self.manager._check_if_already_converted('654', ''))

    def test_check_if_already_converted_when_there_are_not_arabic_number_but_there_is_human_money_identifier_then_return_false(self):
        self.assertFalse(self.manager._check_if_already_converted('some code right there', 'Credits'))

