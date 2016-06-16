import unittest
from files import extract_food

class TestFileManipulation(unittest.TestCase):

	def test_extract_food_into_array(self):
		json_file = "data.json"
		extracted_food = extract_food(json_file)

		self.assertIn("sandwich", extracted_food)
		self.assertIn("cereal", extracted_food)
		self.assertIn("lasagna", extracted_food)
		self.assertEqual(len(extracted_food), 3)

	def reformat_food(self):
		


if __name__ == '__main__':
	unittest.main()