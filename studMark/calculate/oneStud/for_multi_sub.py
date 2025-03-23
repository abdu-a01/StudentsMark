from for_one_sub import pointFun


def gpa(marks,crs):
	
	pMarks = [pointFun(marks[_])*crs[_] for _ in range(len(marks))]
	
	Gpa = sum(pMarks)/sum(crs)
	
	return round(Gpa,2)



def average(*args):
	
	return sum(args)/len(args)


def ranker(*args):
	
	z = sorted(args)[::-1]
	rank = {x:y for x in range(1,len(args) + 1) for y in z if z.index(y) == x-1}
	
	return rank
	
