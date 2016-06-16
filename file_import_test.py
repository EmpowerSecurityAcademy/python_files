import unittest
from files import json_import, csv_import, text_import

class TestFileImport(unittest.TestCase):

	def test_json_import(self):
		json_file = "data.json"
		data = json_import(json_file)

		self.assertEqual(data["breakfast"]["food"], "cereal")

	def test_csv_import(self):
		csv_file = "data.csv"
		data = csv_import(csv_file)

		self.assertEqual(data["first_name"][3], "Eduardo")

	def test_text_import(self):
		txt_file = "data.txt"
		data = text_import(txt_file)

		self.assertEqual(data, ['I really enjoy writing code\n', 'I also enjoy learning about cybersecurity'])

if __name__ == '__main__':
	unittest.main()