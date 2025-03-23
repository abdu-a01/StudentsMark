from .oneStud.for_one_sub import gradeFun
from .oneStud.for_multi_sub import gpa


def mult_gpa_grade(stud_marks,cr_hour):
	num_sub = len(max(stud_marks))
	
	gpa_list = []
	grade_list = []
	
	for each in stud_marks:
		if len(each) < num_sub:
			for _ in range(num_sub - len(each)):
				each.append(0)
			
		temp_grade = [gradeFun(value) for value in each]
		temp_gpa = [gpa(value,cr_hour) for value in each]
	
		
		grade_list.append(temp_grade)
		gpa_list.append(temp_gpa)
	
	return grade_list,gpa_list
	

	
def list_grade_gpa(stud_data,cr_hour):
	stud_names,stud_marks = [],[]
	
	for key,value in stud_data.items():
		stud_names.append(key)
		
		stud_marks.append(value)
	
	grade_list,gpa_list = mult_gpa_grade(stud_marks,cr_hour)
	
	for index,name in enumerate(stud_names):
		stud_data[name] = {
			"marks":stud_marks[index],
			"grade":grade_list[index],
			"gpa":gpa_list[index]
		}
	
	return stud_data

	
def list_gpa(stud_data,cr_hour):
	stud_names,stud_marks = [],[]
	
	for key,value in stud_data.items():
		stud_names.append(key)
		
		stud_marks.append(value)
	
	gpa_list = mult_gpa_grade(stud_marks,cr_hour)[1]
	
	for index,name in enumerate(stud_names):
		stud_data[name] = {
			"marks":stud_marks[index],
			"gpa":gpa_list[index]
		}
	
	return stud_data


def list_grade(stud_data):
	stud_names,stud_marks = [],[]
	
	for key,value in stud_data.items():
		stud_names.append(key)
		
		stud_marks.append(value)
	
	grade_list = [gradeFun(each) for each in stud_marks]
	
	for index,name in enumerate(stud_names):
		stud_data[name] = {
			"marks":stud_marks[index],
			"grade":grade_list[index]
		}
	
	return stud_data
	

def dict_gpa_grade(stud_data,cr_hour):
		
	stud_names = [key for key in stud_data.keys()]
	
	stud_marks = []
	
	for name in stud_names:
		stud = stud_data[name]
			
		temp = [stud[sub] for sub in stud]
		
		stud_marks.append(temp)
		
	grade_list,gpa_list = mult_gpa_grade(stud_marks,cr_hour)
	
	for i,stud in enumerate(stud_names):

		for j,sub in enumerate(stud_data[stud]):
			stud_data[stud][sub] = {
				"mark": stud_marks[i][j],
				"grade": grade_list[i][j]
			}
		
		stud_data[stud]["gpa"] = gpa_list[i]
		
	return stud_data


def dict_grade(stud_data):
		
	stud_names = [key for key in stud_data.keys()]
	
	stud_marks = []
	
	for name in stud_names:
		stud = stud_data[name]
			
		temp = [stud[sub] for sub in stud]
		
		stud_marks.append(temp)
		
	grade_list = [gradeFun(each) for each in stud_marks]
	
	for i,stud in enumerate(stud_names):

		for j,sub in enumerate(stud_data[stud]):
			stud_data[stud][sub] = {
				"mark": stud_marks[i][j],
				"grade": grade_list[i][j]
			}
		
		
	return stud_data
		
		
def dict_gpa(stud_data,cr_hour):
		
	stud_names = [key for key in stud_data.keys()]
	
	stud_marks = []
	
	for name in stud_names:
		stud = stud_data[name]
			
		temp = [stud[sub] for sub in stud]
		
		stud_marks.append(temp)
		
	gpa_list = mult_gpa_grade(stud_marks,cr_hour)[1]
	
	for i,stud in enumerate(stud_names):
		
		stud_data[stud]["gpa"] = gpa_list[i]
		
	return stud_data

def average_mult(stud_data):
	stud_name = [key for key in stud_data]
	
	stud_mark = [value for value in stud_data.values()]
	
	average = [sum(each)/len(each) for each in stud_mark]
	
	for i,name in enumerate(stud_name):
		stud_data[name] = {
			"Marks":stud_mark[i],
			"Average":average[i]
		}
		
	return stud_data
	
def ranker(stud_data):
	
	ranked = sorted(stud_data,key=lambda key:stud_data[key],reverse=True)

	
	final = {rank:{key:stud_data[key]} for rank,key in enumerate(ranked,1)}
	
	return final

