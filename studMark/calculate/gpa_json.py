from .oneStud.for_one_sub import (
	gradeFun,
	gpaFun,
	pointFun,
	studNames,
	studMarks,
	subList,
	max_min,
	fileChecker
)



class StudMark:
	
	def __init__(self,file):
		self.studData = fileChecker(file)
		self.students = studNames(self.studData)
		self.subjects = subList(self.studData)
		self.all_mark = studMarks(self.studData)
		self.total = len(self.students)
		self.max_sub,self.min_sub = max_min(self.studData)
		
		
	def sort(self,gpa=False):
		data = self.studData.copy()
		
		keys = list(self.studData.keys())
		first = keys[0]
		
		if "gpa" in data[first] and gpa:
			data = {key:data[key] for key in sorted(data,key=lambda y: data[y]["gpa"],reverse=True)}
			
			return data
		
		data = {key:data[key] for key in sorted(data)}
		
		return data
		
		
	def sort_update(self,gpa=False):
		
		self.studData = self.sort(gpa=gpa).copy()
		
		
	
	def grade(self):
		data = self.studData.copy()
		
		subject = self.subjects.copy()
		
		for each in data:
			stud = data[each]
			for sub in subject:
				if "mark" not in stud[sub]:
					mark = stud[sub]
					grade_sub = gradeFun(mark)
				
					data[each][sub] = {
						"mark":mark,
						"grade":grade_sub
					}
					continue
				mark = stud[sub]["mark"]
				data[each][sub]["grade"] = gradeFun(mark)
		
		return data
	
	def grade_update(self):
		
		self.studData = self.grade().copy()
		
		
		
	def point(self):
		data = self.studData.copy()
		
		subject = self.subjects.copy()
		
		for each in data:
			stud = data[each]
			for sub in subject:
				if "mark" not in stud[sub]:
					mark = stud[sub]
					point_sub = pointFun(mark)
				
					data[each][sub] = {
						"mark":mark,
						"point":point_sub
					}
					continue
				mark = stud[sub]["mark"]
				data[each][sub]["point"] = pointFun(mark)
		
		return data
	
	
	def point_update(self):
		
		self.studData = self.point().copy()
		
		
		
	def gpa(self,cr_hours):
		data = self.studData.copy()
		marks = self.all_mark
		
		gpa_list = [gpaFun(each,cr_hours) for each in marks]
		
		for i,each in enumerate(self.students):
			data[each]["gpa"] = gpa_list[i]
		
		return data
	
	def gpa_update(self,cr_hours):
		self.studData = self.gpa(cr_hours).copy()
		
		
	def average(self):
		data = self.studData.copy()
		num_sub = len(self.subjects)
		mark_list = self.all_mark
		
		aver = [sum(marks)/num_sub for marks in mark_list]
		for i,each in enumerate(self.students):
			data[each]["average"] = aver[i]
		
		return data
		
	def average_update(self):
		self.studData = self.average().copy()
		
	def ranker(self,gpa=False):
		data = self.studData.copy()
		students = list(data.keys())
		
		if gpa and "gpa" in data[students[0]]:
			sorted_data = self.sort(gpa)
			
			stud_names = list(sorted_data.keys())
			
			rank = [(i,each) for i,each in enumerate(stud_names,1)]
			
		else:
			self.average_update()
			
			rank = [(i,each) for i,each in enumerate(sorted(data,key=lambda y:data[y]["average"],reverse=True),1)]
			
			self.studData = data.copy()
			
		
		for i,each in enumerate(rank):
			
			data[each]["rank"] = rank[i]
		
		return data
		
	def ranker_update(self,gpa=False):
		self.studData = self.ranker(gpa).copy()
			
	
	