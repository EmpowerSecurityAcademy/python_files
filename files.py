import json
import pandas as pd

def json_import(file_name):
	with open(file_name) as json_file:
		json_data = json.load(json_file)
	return json_data

def csv_import(file_name):
	df = pd.read_csv(file_name)
	return df


def text_import(file_name):
	f = open(file_name)
	lines = []
	for line in f.readlines():
		lines.append(line)
	return lines

def extract_food(file_name):
	json_data = json_import(file_name)
	food = []

	for key, value in json_data.items():
		food.append(str(json_data[key]["food"]))

	return food

def reformat_food(file_name)