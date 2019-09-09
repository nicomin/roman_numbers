from app.galactic_prize_converter import GalacticPrizeConverter
from app.human_prize_converter import HumanPrizeConverter


class ProductManager:
    def __init__(self):
        self.products = {}
        self.galactic_converter = GalacticPrizeConverter()
        self.human_converter = HumanPrizeConverter()

    def add_product(self, item_name: str, unit_human_prize: int = 0, unit_galactic_prize: str = ''):
        product_details = {
            'unit_human_prize': unit_human_prize,
            'unit_galactic_prize': unit_galactic_prize
        }
        self.products.update({item_name: product_details})

        if unit_human_prize and not unit_galactic_prize:
            self._calculate_product_galactic_prize(item_name)
        elif unit_galactic_prize and not unit_human_prize:
            self._calculate_product_human_prize(item_name)

    def get_item(self, item_name: str):
        try:
            return self.products[item_name]
        except KeyError:
            raise Exception('The product "{}" is not registered!'.format(item_name))

    def _calculate_product_human_prize(self, product_name):
        if product_name not in self.products:
            raise KeyError('The product "{}" is not registered'.format(product_name))
        self.products[product_name]['unit_human_prize'] = self.galactic_converter.convert_to_human_prize(
            self.products[product_name]['unit_galactic_prize']
        )

    def _calculate_product_galactic_prize(self, product_name):
        if product_name not in self.products:
            raise KeyError('The product "{}" is not registered'.format(product_name))
        try:
            self.products[product_name]['unit_galactic_prize'] = self.human_converter.convert_to_galactic_prize(
                self.products[product_name]['unit_human_prize']
            )
        except ValueError:
            return
