from unittest import TestCase

from app.product_manager import ProductManager


class TestProductManager(TestCase):
    def setUp(self):
        self.manager = ProductManager()

    def test_calculate_product_human_prize_when_product_name_is_not_registered_then_raise_exception(self):
        with self.assertRaises(KeyError) as cm:
            self.manager._calculate_product_human_prize('sandia')
        self.assertEqual('The product "sandia" is not registered', cm.exception.args[0])

    def test_calculate_product_human_prize_when_product_name_is_already_registered_then_update_human_prize_attr_based_on_galactic_prize(self):
        self.manager.products['limon'] = {
            'unit_galactic_prize': 'XXII'
        }
        self.manager._calculate_product_human_prize('limon')
        self.assertEqual(22, self.manager.products['limon']['unit_human_prize'])

    def test_calculate_product_galactic_prize_when_product_name_is_not_registered_then_raise_exception(self):
        with self.assertRaises(KeyError) as cm:
            self.manager._calculate_product_galactic_prize('mango')
        self.assertEqual('The product "mango" is not registered', cm.exception.args[0])

    def test_calculate_product_galactic_prize_when_product_name_is_already_registered_then_update_galactic_prize_attr_based_on_human_prize(self):
        self.manager.products['durazno'] = {
            'unit_human_prize': 27
        }
        self.manager._calculate_product_galactic_prize('durazno')
        self.assertEqual('XXVII', self.manager.products['durazno']['unit_galactic_prize'])

    def test_add_product_when_input_has_at_least_a_prize_create_in_memory_register_and_calculate_missing_prize_if_neccesary(self):
        self.manager.add_product('melon calameno', unit_human_prize=500)
        self.assertEqual('D', self.manager.products['melon calameno']['unit_galactic_prize'])
        self.manager.add_product('pomelo', unit_galactic_prize='IV')
        self.assertEqual(4, self.manager.products['pomelo']['unit_human_prize'])
        self.manager.add_product('naranja', unit_galactic_prize='IV', unit_human_prize=500)
        self.assertEqual(500, self.manager.products['naranja']['unit_human_prize'])
        self.assertEqual('IV', self.manager.products['naranja']['unit_galactic_prize'])
