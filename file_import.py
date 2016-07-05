import json
import pandas as pd
import xmltodict

def json_import(file_name):
	with open(file_name) as json_file:
		json_data = json.load(json_file)
	return json_data

def csv_import(file_name):
	data_frame = pd.read_csv(file_name)
	return data_frame

def text_import(file_name):
	f = open(file_name)
	lines = []
	for line in f.readlines():
		lines.append(line)
	return lines

def xml_import(file_name):
	with open(file_name) as file:
		doc = xmltodict.parse(file.read())
	return doc


