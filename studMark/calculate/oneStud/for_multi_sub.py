from for_one_sub import pointFun
from .utility_modules.one_stud_support import (
	checkIndex,NotNumberError,isfloat
)


def gpa(marks,crs):
	checkIndex(marks,crs)
	pMarks = [pointFun(marks[_])*crs[_] for _ in range(len(marks))]
	
	Gpa = sum(pMarks)/sum(crs)
	
	return round(Gpa,2)



def average(*args):
	for arg in args:
		if isfloat(arg):
			continue
		raise NotNumberError(f"{arg} is not number!")
	return sum(args)/len(args)


def ranker(*args):
	for arg in args:
		if isfloat(arg):
			continue
		raise NotNumberError("it gives rank for numbers only!")
	z = sorted(args)[::-1]
	rank = {x:y for x in range(1,len(args) + 1) for y in z if z.index(y) == x-1}
	
	return rank
	

