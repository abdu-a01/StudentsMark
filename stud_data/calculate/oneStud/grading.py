from .utility.validator import checkMark,checkIndex

def giveGrade(result:float) -> tuple:
	result = checkMark(result)
	if result >= 90:
		grade = "A+"
		point = 4.0
	elif result >= 85 and result < 90:
		grade = "A"
		point = 4.0
	elif result >= 80 and result < 85:
		grade = "A-"
		point = 3.75			
	elif result >= 75 and result < 80:
		grade = "B+"
		point = 3.5			
	elif result >= 70 and result < 75:
		grade = "B"
		point = 3.0			
	elif result >= 65 and result < 70:
		grade = "B-"
		point = 2.75			
	elif result >= 60 and result < 65:
		grade = "C+"
		point = 2.5			
	elif result >= 50 and result < 60:
		grade = "C"
		point = 2.0			
	elif result >= 45 and result < 50:
		grade = "C-"
		point = 1.75			
	elif result >= 40 and result < 45:
		grade = "D"
		point = 1.0
	elif result >= 30 and result < 40:
		grade = "Fx"
		point = 0.0
	else:
		grade = "F"
		point = 0.0
	return grade, point
	


def gradeFun(mark:float) -> str:
	return giveGrade(mark)[0]



def pointFun(mark:float) -> float:
	return giveGrade(mark)[1]	


def gpaFun(marks:list,crs:list) -> float:
	checkIndex(marks,crs)
	pMarks = [pointFun(marks[_])*crs[_] for _ in range(len(marks))]
	
	Gpa = sum(pMarks)/sum(crs)
	
	return round(Gpa,2)
	
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
	names = list(data.keys())
	subjects = list(data[names[0]].keys())
	
	marks = [[data[stud][sub] for sub in subjects] for stud in names]
	
	return names,subjects,marks
	
	
def studNames(data):
	return extractor(data)[0]
	
def studMarks(data):
	return extractor(data)[2]
	
def subList(data):
	return extractor(data)[1]
	

	
def max_min(data):
	sub_marks = {sub:[data[stud][sub] for stud in studNames(data)] for sub in subList(data)}
	
	mean_mark = {sub:sum(sub_marks[sub])/len(sub_marks[sub]) for sub in sub_marks}
	
	max_sub = max(mean_mark,key=lambda x:mean_mark[x])
	
	min_sub = min(mean_mark,key=lambda x:mean_mark[x])
	
	return {max_sub:mean_mark[max_sub]},{min_sub:mean_mark[min_sub]}
	

