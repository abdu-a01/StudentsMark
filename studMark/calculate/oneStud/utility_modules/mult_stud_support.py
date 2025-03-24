class MinMarkError(Exception):
	pass

class NotNumberError(Exception):
	pass
	
class NotEqualIndexError(Exception):
	pass


def checkFile(input_data): 
	if type(input_data) == dict:
		return input_data.copy()
	if "." in input_data:
		sep = input_data.split(".")
		if sep[-1] != "json":
			raise ValueError("the function receivs only dictionary or json file")
		json = __import__("json")
		with open(input_data) as file:
			return json.load(file)
		
	raise ValueError("the function receivs only dictionary or json file")
	
 
def checkDictType(file):
	Type = list()
	keys = file.keys()
	
	for key in keys:
		needed = file[key]
		if type(needed) == list:
			Type.append("list")
		elif type(needed) == dict:
			Type.append("dict")

	if len(Type) != len(list(keys)):
		raise ValueError("unsupported format")
	else:
		uType = list(set(Type))
		if len(uType) != 1:
			raise ValueError("All values should be constant type")
		if Type[0] == "list":
			return "list"
		if Type[0] != "dict":
			raise ValueError("unsupported format")
			
		for key in keys:
			needed = file[key]
			for key in needed.keys():
				try:
					float(needed[key])
				except ValueError:
					raise ValueError("unsupported format")
				except TypeError:
					raise ValueError("unsupported format")
		
		return "dict"
		

def mult_gpa_grade(stud_marks,cr_hour,checkMark,checkIndex,gradeFun,gpa):
	stud_marks = [[checkMark(mark) for mark in marks] for marks in stud_marks]
	
	checkIndex(max(stud_marks),cr_hour)
	
	grade_list = [[gradeFun(value) for value in each] for each in stud_marks]
	
	gpa_list = [[gpa(value,cr_hour) for value in each] for each in stud_marks]
	
	
	return grade_list,gpa_list



def list_item_extract(input_data):
	
	stud_data = checkFile(input_data)
	
	if checkDictType(stud_data) != "list":
		raise TypeError("Values must be lists")
		
	
	
	stud_names = [key for key in stud_data]
	
	stud_marks = [value for value in stud_data.values()]
	
	num_sub = len(max(stud_marks))
	
	for each in stud_marks:
		if len(each) < num_sub:
			for _ in range(num_sub - len(each)):
				each.append(0)
	
	return stud_data,stud_names,stud_marks
		
		

def dict_mark_extractor(input_raw):
	input_procced = checkFile(input_raw)
	if checkDictType(input_procced) != "dict":
		raise TypeError("Values must be Dicfionaries")
	
	stud_data = {}
	for key in input_procced.keys():
		stud_data[key] = {}
		for value in input_procced[max(input_procced)]:
			try:
				stud_data[key][value] = input_procced[key][value]
			except KeyError:
				stud_data[key][value] = 0
	stud_names = [key for key in stud_data]
	
	stud_marks = []
	
	for name in stud_names:
		stud = stud_data[name]
			
		temp = [stud[sub] for sub in stud]
		
		stud_marks.append(temp)
	
	return stud_data,stud_names,stud_marks
		