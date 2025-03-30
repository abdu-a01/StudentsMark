"""This module provides functions that are used to calculate grade, point,gpa and to extract students name, subjects, and marks.
it has the following functions:
	-giveGrade
	-gpaFun
	-gpa
	-extractor
	-max_min
"""


from .utility.validator import checkMark,checkIndex

def giveGrade(result:float) -> tuple:
	"""This function used to calculate grade and point using result as an input
	- first check if an argument is valid or not
	- then checks its grade and point 
	then returns tuple with grade and point 
	"""
	result = checkMark(result)
	if result >= 90:
		grade = "A+"
		point = 4.0
	elif result >= 85:
		grade = "A"
		point = 4.0
	elif result >= 80:
		grade = "A-"
		point = 3.75			
	elif result >= 75:
		grade = "B+"
		point = 3.5			
	elif result >= 70:
		grade = "B"
		point = 3.0			
	elif result >= 65:
		grade = "B-"
		point = 2.75			
	elif result >= 60:
		grade = "C+"
		point = 2.5			
	elif result >= 50:
		grade = "C"
		point = 2.0			
	elif result >= 45:
		grade = "C-"
		point = 1.75			
	elif result >= 40:
		grade = "D"
		point = 1.0
	elif result >= 30:
		grade = "Fx"
		point = 0.0
	else:
		grade = "F"
		point = 0.0
	return grade, point
	

def gradeFun(mark):
	"""used to calculate grade for one subject mark
	recives: mark - non negative float number 
	return : the first element that returned from giveGrade
	"""
	return giveGrade(mark)[0]

def pointFun(mark):
	"""used to calculate point for one subject mark
	recives: mark - non negative float number 
	return : the second element that returned from giveGrade
	"""
	return giveGrade(mark)[1]


def gpaFun(marks:list,crs:list) -> float:
	"""This function calculate gpa from given marks and crs
	first check if marks and crs is valid or not
	then calculate Gpa 
	"""
	checkIndex(marks,crs)
	pMarks = [pointFun(marks[_])*crs[_] for _ in range(len(marks))]
	
	Gpa = sum(pMarks)/sum(crs)
	
	return round(Gpa,2)
	
def average(*args):
	"""used to calculate average:
	recive: args - marks each mark is float
	return: sum of marks devided by number of args
	"""
	for each in args:
		checkMark(each)
	return sum(args)/len(args)
	
def gpa(*args):
	for each in args:
		if type(each) != tuple:
			raise TypeError("Invalid argument")
		if len(each) != 2:
			raise ValueError("each value must have both mark and credit hours")
	marks = [each[0] for each in args]
	cr_hours = [each[1] for each in args]
	
	return gpaFun(marks,cr_hours)


	
def extractor(data):
	"""This function recives dictionary of students data,
	return (
		students name,
		subjects and 
		marks 
	)
	"""
	names = list(data.keys())
	subjects = list(data[names[0]].keys())
	
	marks = [[data[stud][sub] for sub in subjects] for stud in names]
	
	return names,subjects,marks
	

	
studNames = lambda data: extractor(data)[0]

studMarks = lambda data: extractor(data)[2]

subList = lambda data: extractor(data)[1]	

	
def max_min(data):
	"""This function recives dictionary of students data then
	returns max mark and min mark subjects.
	"""
	sub_marks = {sub:[data[stud][sub] for stud in studNames(data)] for sub in subList(data)}
	
	mean_mark = {sub:sum(sub_marks[sub])/len(sub_marks[sub]) for sub in sub_marks}
	
	max_sub = max(mean_mark,key=lambda x:mean_mark[x])
	
	min_sub = min(mean_mark,key=lambda x:mean_mark[x])
	
	return {max_sub:mean_mark[max_sub]},{min_sub:mean_mark[min_sub]}
	

