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

#use json_import within this function
def extract_food(file_name):
	json_data = json_import(file_name)
	food = []

	for key, value in json_data.items():
		food.append(str(json_data[key]["food"]))

	return food

#use json_import within this function
def reformat_meals(file_name):
	json_data = json_import(file_name)
	reformatted_meals = {}
	reformatted_meals["drink"] = []
	reformatted_meals["food"] = []

	for key, value in json_data.items():
		reformatted_meals["drink"].append(str(json_data[key]["drink"]))
		reformatted_meals["food"].append(str(json_data[key]["food"]))

	return reformatted_meals

#use csv_import within this function
def age_summer(file_name):
	csv_data = csv_import(file_name)
	age_total = 0

	for index, row in csv_data.iterrows():
		age_total += row["age"]

	return age_total

def first_names_starting_with_j(file_name):
	csv_data  = csv_import(file_name)
	j_names = []

	for index, row in csv_data.iterrows():
		if row["first_name"][0] == "J":
			j_names.append(row["first_name"])

	return j_names

