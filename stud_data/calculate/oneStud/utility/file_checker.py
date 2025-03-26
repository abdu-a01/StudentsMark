from pathlib import Path

def validate(file):
	
	keys = file.keys()
	
	for key in keys:
		needed = file[key]
		if type(needed) != dict:
			raise ValueError("unsupported format")
			
	for key_up in keys:
		needed = file[key_up]
		for key in needed.keys():
			try:
				float(needed[key])
			except ValueError:
				raise ValueError("unsupported format")
			except TypeError:
				raise ValueError("unsupported format")
		
	return file.copy()


def checkFile(input_data): 
	if type(input_data) == dict:
		return validate(input_data)
		
	file = Path(input_data)
	if not file.is_file():
		raise ValueError("the function receivs only dictionary or json file")
		
	if file.suffix != "json":
		raise ValueError("the function receivs only dictionary or json file")
		
	json = __import__("json")
	with open(input_data) as file:
		data = json.load(file)
		
	return validate(data)

