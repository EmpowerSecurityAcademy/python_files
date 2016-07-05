
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

def extract_i_and_I_from_text(file_name):
	txt_data = text_import(file_name)
	stripped = []

	for sentence in txt_data:
		i_removed = sentence.replace("i", "")
		i_I_removed = i_removed.replace("I", "")
		stripped.append(i_I_removed)

	return stripped




