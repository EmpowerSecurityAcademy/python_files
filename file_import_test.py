import unittest
from file_import import json_import, csv_import, text_import

class TestFileImport(unittest.TestCase):

	def test_json_import(self):
		json_file = "./files/data.json"
		data = json_import(json_file)

		self.assertEqual(data["breakfast"]["food"], "cereal")

	#use the pandas library read_csv method for this
	def test_csv_import(self):
		csv_file = "./files/data.csv"
		data = csv_import(csv_file)

		self.assertEqual(data["first_name"][3], "Eduardo")

	def test_text_import(self):
		txt_file = "./files/data.txt"
		data = text_import(txt_file)

		self.assertEqual(data, ['I really enjoy writing code\n', 'I also enjoy learning about cybersecurity'])

	def test_xml_import(self):
		xml_file = "./files/data.xml"
		data = xml_import(xml_file)

		print(data)

if __name__ == '__main__':
	unittest.main(verbosity=2)