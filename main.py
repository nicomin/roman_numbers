import re
import time

from app.product_manager import ProductManager
from app.translation_manager import TranslationManager


class Main:

	def __init__(self):
		self.translator = TranslationManager()
		self.product_manager = ProductManager()
		self.assignment_regex = re.compile(
			r'(?P<word>([a-z]+\s)+)(?P<product>\b[A-Z][a-z]+\b\s)?\bis \b(?P<assigned_value>\w+)\s?(?P<currency_type>\w+)?'
		)
		self.simple_prize_question = re.compile(r'\bhow much is \b(?P<word>([a-z]+\s)+)(?P<product>\b[A-Z][a-z]+\b\s)?\s?\?')
		self.prize_question_with_currency_type_regex = re.compile(
			r'\bhow many \b\s?(?P<currency_type>\w+)\b is \b(?P<word>([a-z]+\s)+)(?P<product>\b[A-Z][a-z]+\b\s)?\s?\?'
		)

	def read_statement(self, statement: str):
		assignment_match = self.assignment_regex.match(statement)
		simple_prize_question_match = self.simple_prize_question.match(statement)
		prize_question_ct_match = self.prize_question_with_currency_type_regex.match(statement)

		try:
			if simple_prize_question_match:
				input_phrase = simple_prize_question_match.groupdict()['word'].strip()
				requested_value = self.translator.translate_prize_phrase(
					input_phrase, self.translator.HUMAN_MONEY_IDENTIFIER
				)
				print('{} is {}'.format(input_phrase, requested_value))
			elif prize_question_ct_match:
				matched_group = prize_question_ct_match.groupdict()
				product = self.product_manager.get_item(matched_group['product'])
				requested_quantity = self.translator.translate_prize_phrase(
					matched_group['word'].strip(), matched_group['currency_type']
				)
				total_amount = product['unit_human_prize'] * requested_quantity
				print('{} {} is {:.0f} {}'.format(
					matched_group['word'], matched_group['product'], total_amount, matched_group['currency_type'])
				)
			elif assignment_match:
				matched_group = assignment_match.groupdict()
				product = matched_group['product']
				if product:
					products_quantity = self.translator.translate_prize_phrase(
						matched_group['word'].strip(), self.translator.HUMAN_MONEY_IDENTIFIER
					)
					products_prize = self.translator.translate_prize_phrase(
						matched_group['assigned_value'], self.translator.HUMAN_MONEY_IDENTIFIER
					)
					unit_human_prize = int(products_prize) / products_quantity
					self.product_manager.add_product(product, unit_human_prize=unit_human_prize)
				else:
					self.translator.add_item(
						matched_group['word'].strip(),
						matched_group['assigned_value'],
						matched_group['currency_type']
					)
			else:
				print('I have no idea what you are talking about')
		except Exception as e:
			print(e.args[0])


if __name__ == '__main__':
	main_exec = Main()
	fname = 'test_entries.txt'
	with open(fname) as f:
		file_lines = f.readlines()
		content = [x.strip() for x in file_lines]
		for statement in content:
			if not statement:
				continue
			main_exec.read_statement(statement)
	time.sleep(10)
