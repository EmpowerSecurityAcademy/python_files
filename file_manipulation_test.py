import unittest
from files import extract_food, reformat_meals

class TestFileManipulation(unittest.TestCase):

	def test_extract_food(self):
		json_file = "data.json"
		extracted_food = extract_food(json_file)

		self.assertIn("sandwich", extracted_food)
		self.assertIn("cereal", extracted_food)
		self.assertIn("lasagna", extracted_food)
		self.assertEqual(len(extracted_food), 3)


	"""
	the data.json object should be reformatted to:
	{
		"drink": ["tea", "lemonade", "wine"],
		"food": ["cereal", "sandwich", "lasagna"]
	}
	"""

	def test_reformat_meals(self):
		json_file = "data.json"
		reformatted = reformat_meals(json_file)


		self.assertIn("sandwich", reformatted["food"])
		self.assertIn("cereal", reformatted["food"])
		self.assertIn("lasagna", reformatted["food"])

		self.assertIn("tea", reformatted["drink"])
		self.assertIn("lemonade", reformatted["drink"])
		self.assertIn("wine", reformatted["drink"])

		self.assertEqual(len(reformatted["drink"]), 3)
		self.assertEqual(len(reformatted["food"]), 3)



if __name__ == '__main__':
	unittest.main(verbosity=2)