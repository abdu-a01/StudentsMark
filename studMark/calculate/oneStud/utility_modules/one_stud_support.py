def isfloat(obj):
	try:
		float(obj)
	except ValueError:
		return False
	except TypeError:
		return False		
	else:
		return True
	
def checkMark(mark):
	if isfloat(mark):
		if float(mark) < 0:
			raise ValueError("Mark should be greater than zero negative doesn't have grade.")
		else:
			return float(mark)
	else:
		raise ValueError("Mark should be number only")

		
def checkIndex(arg1,arg2):
	if type(arg1) not in [list,tuple] or type(arg2) not in [list,tuple]:
		raise TypeError("You should give mark and credit hour with list or tuple")
		
	elif len(arg1) != len(arg2):
		raise ValueError("number of mark and their credit hour should be the same")
	
	elif not all(map(lambda x:type(x) == int and x > 0,arg2)):
		raise ValueError("credit hour should be number only")
	
	