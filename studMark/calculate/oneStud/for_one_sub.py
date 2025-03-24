from .utility_modules.one_stud_support import checkMark,checkIndex

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


def gpa(marks:list,crs:list) -> float:
	checkIndex(marks,crs)
	pMarks = [pointFun(marks[_])*crs[_] for _ in range(len(marks))]
	
	Gpa = sum(pMarks)/sum(crs)
	
	return round(Gpa,2)