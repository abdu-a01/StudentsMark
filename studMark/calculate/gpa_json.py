from .oneStud.for_one_sub import gradeFun,gpa
from .oneStud.utility_modules.mult_stud_support import (
	list_item_extract,dict_mark_extractor,mult_gpa_grade
)
from .oneStud.utility_modules.one_stud_support import checkMark,checkIndex

	

	
def list_grade_gpa(input_data,cr_hour):
	
	stud_data,stud_names,stud_marks = list_item_extract(input_data)
	
	grade_list,gpa_list = mult_gpa_grade(stud_marks,cr_hour,checkMark,checkIndex,gradeFun,gpa)
	
	for index,name in enumerate(stud_names):
		stud_data[name] = {
			"marks":stud_marks[index],
			"grade":grade_list[index],
			"gpa":gpa_list[index]
		}
	
	return stud_data

	
def list_gpa(input_data,cr_hour):
	stud_data,stud_names,stud_marks = list_item_extract(input_data)
	
	gpa_list = mult_gpa_grade(stud_marks,cr_hour,checkMark,checkIndex,gradeFun,gpa)[1]
	
	for index,name in enumerate(stud_names):
		stud_data[name] = {
			"marks":stud_marks[index],
			"gpa":gpa_list[index]
		}
	
	return stud_data


def list_grade(input_data):
	
	stud_data,stud_names,stud_marks = list_item_extract(input_data)
	
	grade_list = [gradeFun(each) for each in stud_marks]
	
	for index,name in enumerate(stud_names):
		stud_data[name] = {
			"marks":stud_marks[index],
			"grade":grade_list[index]
		}
	
	return stud_data
	
	
##################################
##################################

def dict_gpa_grade(input_dict,cr_hour):
	
	stud_data,stud_names,stud_marks = dict_mark_extractor(input_dict)

		
	grade_list,gpa_list = mult_gpa_grade(stud_marks,cr_hour,checkMark,checkIndex,gradeFun,gpa)
	
	for i,stud in enumerate(stud_names):

		for j,sub in enumerate(stud_data[stud]):
			stud_data[stud][sub] = {
				"mark": stud_marks[i][j],
				"grade": grade_list[i][j]
			}
		
		stud_data[stud]["gpa"] = gpa_list[i]
		
	return stud_data


def dict_grade(input_dict):
		
	stud_data,stud_names,stud_marks = dict_mark_extractor(input_dict)
		
	grade_list = [gradeFun(each) for each in stud_marks]
	
	for i,stud in enumerate(stud_names):

		for j,sub in enumerate(stud_data[stud]):
			stud_data[stud][sub] = {
				"mark": stud_marks[i][j],
				"grade": grade_list[i][j]
			}
		
		
	return stud_data
		
		
def dict_gpa(input_data,cr_hour):
		
	stud_data,stud_names,stud_marks = dict_mark_extractor(input_data)
		
	gpa_list = mult_gpa_grade(stud_marks,cr_hour,checkMark,checkIndex,gradeFun,gpa)[1]
	
	for i,stud in enumerate(stud_names):
		
		stud_data[stud]["gpa"] = gpa_list[i]
		
	return stud_data


##################################
##################################

def average_mult(input_dict):
	
	stud_data = input_dict.copy()
	
	stud_name = [key for key in stud_data]
	
	stud_mark = [value for value in stud_data.values()]
	
	num_sub = len(max(stud_mark))
	
	average = [sum(each)/num_sub for each in stud_mark]
	
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

