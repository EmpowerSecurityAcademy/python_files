import unittest
from file_manipulation import extract_food, reformat_meals, age_summer, first_names_starting_with_j, extract_i_and_I_from_text

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

	# def test_reformat_meals(self):
	# 	json_file = "data.json"
	# 	reformatted = reformat_meals(json_file)


	# 	self.assertIn("sandwich", reformatted["food"])
	# 	self.assertIn("cereal", reformatted["food"])
	# 	self.assertIn("lasagna", reformatted["food"])

	# 	self.assertIn("tea", reformatted["drink"])
	# 	self.assertIn("lemonade", reformatted["drink"])
	# 	self.assertIn("wine", reformatted["drink"])

	# 	self.assertEqual(len(reformatted["drink"]), 3)
	# 	self.assertEqual(len(reformatted["food"]), 3)

	# def test_cumulative_age(self):
	# 	csv_file = "data.csv"
	# 	cumulative_age = age_summer(csv_file)

	# 	self.assertEqual(cumulative_age, 294)

	# def test_first_names_starting_with_j(self):
	# 	csv_file = "data.csv"
	# 	j_names = first_names_starting_with_j(csv_file)

	# 	self.assertEqual(j_names, ["Jason", "Jake"])

	# def test_extract_i_and_I_from_text(self):
	# 	txt_file = "data.txt"
	# 	i_I_removed = extract_i_and_I_from_text(txt_file)

	# 	self.assertIn(' really enjoy wrtng code\n', i_I_removed)
	# 	self.assertIn(' also enjoy learnng about cybersecurty', i_I_removed)



if __name__ == '__main__':
	unittest.main(verbosity=2)