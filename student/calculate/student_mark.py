"""This module has a class used to retrieve data from a given students data
	has class:
		StudMark
"""


from openpyxl import Workbook
from openpyxl.utils import get_column_letter as gcl
from .oneStud.utility.file_checker import checkFile,dict_xlsx
from .oneStud.grading import (
	gradeFun,
	gpaFun,
	pointFun,
	studNames,
	studMarks,
	subList,
	max_min
)


class StudMark:
	"""This class has all operations that are related to students mark.
	has attributes:
		studData
		students
		subjects
		all_mark
		total
		min_mark
		max_mark
	has methods:
		sort
		sort_update
		grade
		grade_update
		point
		point_update
		gpa
		gpa_update
		average
		average_update
		ranker
		ranker_update
		id_giver
		one_sub
		one_stud
		json
		xlsx
	"""
	
	def __init__(self,file):
		"""initializes the following private attributes for the class:
			studData - the whole students data with dictionary
			students - list of students name 
			subjects - list of subjects
			- all_mark - all marks of students in the form of 2D list
			- total - total number of students
			- max_sub - the subject that has maximum average mark from all students 
			- min_sub - the subject that has minimum average mark from all students 
		"""
		self._studData = checkFile(file)
		self._students = studNames(self._studData)
		self._subjects = subList(self._studData)
		self._all_mark = studMarks(self._studData)
		self._total = len(self._students)
		self._max_sub,self._min_sub = max_min(self._studData)
		
	@property
	def studData(self):
		"""Used to access private _studData from outer scope
		"""
		return self._studData
		
	@property
	def students(self):
		"""Used to access private _students from outer scope
		"""
		return self._students
	
	@property
	def subjects(self):
		"""Used to access private _subjects from outer scope
		"""
		return self._subjects
		
	@property
	def all_mark(self):
		"""Used to access private _all_mark from outer scope
		"""
		return self._all_mark
	
	@property
	def total(self):
		"""Used to access private _total from outer scope
		"""
		return self._total
	
	@property
	def max_sub(self):
		"""Used to access private _max_sub from outer scope
		"""
		return self._max_sub
		
	@property
	def min_sub(self):
		"""Used to access private _min_sub from outer scope
		"""
		return self._min_sub
		
		
	def sort(self,gpa=False):
		"""used to sort the students data, according to:
			- there gpa if gpa is in the dict and gpa parameter is True
			- else by there name
		"""
		data = self._studData.copy()
		
		keys = list(self._studData.keys())
		first = keys[0]
		
		if "gpa" in data[first] and gpa:
			data = {key:data[key] for key in sorted(data,key=lambda y: data[y]["gpa"],reverse=True)}
			
			return data
		
		data = {key:data[key] for key in sorted(data)}
		
		return data
		
		
	def sort_update(self,gpa=False):
		"""The same function as sort but it can update the students data 
		"""
		self._studData = self.sort(gpa=gpa).copy()
		
		
	
	def grade(self):
		"""Used to give grade for each student and for each subject
		"""
		data = self._studData.copy()
		
		subject = self._subjects.copy()
		
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
		"""the same as grade function unless it can update the students data 
		"""
		
		self._studData = self.grade().copy()
		
		
		
	def point(self):
		"""Used to give point for each student and for each subject
		"""
		data = self._studData.copy()
		
		subject = self._subjects.copy()
		
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
		"""the same as point function unless it can update the students data 
		"""
		self._studData = self.point().copy()
		
		
		
	def gpa(self,cr_hours):
		"""Used to calculate gpa by receiving credit hours for each subject and returns a dictionary with students data plus there gpa
		"""
		data = self._studData.copy()
		marks = self._all_mark
		
		gpa_list = [gpaFun(each,cr_hours) for each in marks]
		
		for i,each in enumerate(self._students):
			data[each]["gpa"] = gpa_list[i]
		
		return data
	
	def gpa_update(self,cr_hours):
		"""the same as gpa function unless it can update the students data
		"""
		self._studData = self.gpa(cr_hours).copy()
		
		
	def average(self):
		"""Used to calculate average of students mark and returns students data dictionary plus there average
		"""
		data = self._studData.copy()
		num_sub = len(self._subjects)
		mark_list = self._all_mark
		
		aver = [sum(marks)/num_sub for marks in mark_list]
		for i,each in enumerate(self._students):
			data[each]["average"] = aver[i]
		
		return data
		
	def average_update(self):
		"""The same as average function unless it can update the students data
		"""
		self._studData = self.average().copy()
		
	def ranker(self,gpa=False):
		"""give rank for students by using:
			- gpa if gpa is in dict and gpa is True
			- else average
		"""
		data = self._studData.copy()
		students = list(data.keys())
		
		if gpa and "gpa" in data[students[0]]:
			sorted_data = self.sort(gpa)
			
			stud_names = list(sorted_data.keys())
			
			rank = [(i,each) for i,each in enumerate(stud_names,1)]
			
		else:
			self.average_update()
			
			rank = [(i,each) for i,each in enumerate(sorted(data,key=lambda y:data[y]["average"],reverse=True),1)]
			
			self._studData = data.copy()
			
		
		for i,each in enumerate(rank):
			
			data[each]["rank"] = rank[i]
		
		return data
		
	def ranker_update(self,gpa=False):
		"""The same as ranker unless it can update the students data
		"""
		self._studData = self.ranker(gpa).copy()
			
	
	def id_giver(self,pre="",suf="",sep="/",length=4):
		"""Used to give id for all students from starting 1.
		uses arguments:
			pre - to set prefix 
			suf - to set suffix 
			sep - to set separator between prefix and the id also between id and suffix 
			length - length of id
		"""
		data = self.sort()
		sep = sep if sep in ["-","\\",":"] else "/"
		form = lambda txt:f"{pre}{sep}{txt:}{sep}{suf}"
		
		IDs = [form(f"{i:0{length}d}") for i in range(1,len(data)+1)]
		
		for i,each in enumerate(data):
			data[each]["id_number"] = IDs[i]
		
		self._studData = data.copy()
	
	
	def one_sub(self,subject):
		"""Used to retrieve information about single subject
		recives:
			subject - string of the subject
		returns :
			Subject class to retrieve data about the subject
		"""
		data = self._studData.copy()
		marks = [data[name][subject] for name in data]
		
		class Subject:
			"""Class used to retrieve different informations about the subject
			have the following methods:
				max_mark
				min_mark
				average
				full_mark
			"""
			
			def max_mark(self, target=""):
				"""this method used to get information about the largest mark in the list of all marks.
				recives:
					target - string value must be 'sub' or 'stud' default is ''
				
				if target is 'sub':
					returns maximum mark float type
				else:
					if target is 'stud':
						return list of students that has maximum mark
					else:
						return dict of students and mark with maximum mark
				
				"""
				maximum = max(marks)
				result = {}
				for each in data:
					value = data[each][subject]
					if value == maximum:
						result[each] = value
				
				if target.lower().strip() == "sub":
					return maximum
				elif target.lower().strip() == "stud":
					studs = list(result.keys())
					return studs
				
				return result
				
				
			def min_mark(self, target=""):
				"""this method used to get information about the smallest mark in the list of all marks.
				recives:
					target - string value must be 'sub' or 'stud' default is ''
				
				if target is 'sub':
					returns minimum mark float type
				else:
					if target is 'stud':
						return list of students that has mimimum mark
					else:
						return dict of students and mark with minimum mark
				
				"""
				minimum = min(marks)
				result = {}
				for each in data:
					value = data[each][subject]
					if value == minimum:
						result[each] = value
				
				if target.lower().strip() == "Mark":
					return minimum
				elif target.lower().strip() == "stud":
					studs = list(result.keys())
					return studs
				
				return result
			
			def average(self):
				"""used to calculate average mark of all students.
				"""
				return sum(marks)/len(marks)
				
			def full_mark(self):
				"""used to extract dict with key of students and value of there mark associated with the given subject.
				"""
				result = {name:data[name][subject] for name in data}
				return result
				
		return Subject()
		
		
	def one_stud(self,name):
		"""Used to retrieve information about single student
		recives:
			name - string of the student's name
		returns :
			Student class to retrieve data about the student
		"""
		data = self._studData.copy()
		stud_data = {name:data[name]}
		subjects = self._subjects.copy()
		
		class Student:
			"""Class used to retrieve different informations about the student
				have the following attributes:
					info
					marks
				have the following methods:
					max_mark
					min_mark
					average
					grade
					point
					gpa
			"""
			
			def __init__(self):
				"""Used to initialize 
				attributes for The class
				initializes:
					info - dict with full information about the student
					marks - list of marks the student have
				"""
				self.info = stud_data.copy()
				self.marks = [stud_data[name][sub] for sub in stud_data[name]]
			
			def max_mark(self,target=""):
				"""this method used to get information about the largest mark of the student.
				recives:
					target - string value must be 'sub' or 'mark' default is ''
				
				if target is 'mark':
					returns maximum mark float type
				else:
					if target is 'sub':
						return list of subjects that has maximum mark
					else:
						return dict of subjects and marks with maximum mark
				
				"""
				maximum = max(self.marks)
				result = {}
				for each in stud_data[name]:
					value = data[name][each]
					if value == maximum:
						result[each] = value
				target = target.lower().strip()
				if target == "mark":
					return maximum
				elif target == "sub":
					return list(result.keys())
				return result
				
				
			def min_mark(self,target=""):
				"""this method used to get information about the smallest mark of the student.
				recives:
					target - string value must be 'sub' or 'mark' default is ''
				
				if target is 'mark':
					returns minimum mark float type
				else:
					if target is 'sub':
						return list of subjects that has minimum mark
					else:
						return dict of subjects and marks with minimum mark
				
				"""
				minimum = min(self.marks)
				result = {}
				for each in stud_data[name]:
					value = data[name][each]
					if value == minimum:
						result[each] = value
				target = target.lower().strip()
				if target == "mark":
					return minimum
				elif target == "sub":
					return list(result.keys())
				return result
			
			def average(self):
				"""used to get average mark of the student
				"""
				return sum(self.marks)/len(self.marks)
			
			def grade(self,sub="all"):
				"""used to get grades of the student:
				recives:
					sub - string with possible subjects default is 'all'
				if subject is given:
					return grade of given subject
				else:
					return all grade
				"""
				if sub in subjects:
					Mark = stud_data[name][sub]
					return gradeFun(Mark)
				
				grades = [gradeFun(each) for each in self.marks]
				
				return grades
			
			def point(self,sub="all"):
				"""used to get point of the student:
				recives:
					sub - string with possible subjects default is 'all'
				if subject is given:
					return point of given subject
				else:
					return all point
				"""
				if sub in subjects:
					Mark = stud_data[name][sub]
					return pointFun(Mark)
				
				point = [pointFun(each) for each in self.marks]
				
				return point
				
			def gpa(self,cr_hours):
				"""used to calculate gpa of the student
				recive:
					cr_hours - list or tuple of credit hours 
				
				if cr_hours doesn't given:
					check if a student has gpa in the dict
					if it has:
						return gpa
					else:
						raise TypeError 
				else:
					call gpaFun for calculating gpa and return it
				"""
				try:
					return gpaFun(self.marks,cr_hours)
				except TypeError:
					if "gpa" in stud_data[name]:
						return stud_data[name]["gpa"]
					else:
						raise TypeError("gpa() missing 1 required positional argument: 'cr_hours'")
			
		return Student()
		
	def json(self):
		"""used to convert dictionary data to json file.
		"""
		json = __import__("json")
		with open("student_data.json","w") as file:
			json.dump(self._studData,file,indent=4)
		
		print("student data has been saved")
		
	def xlsx(self):
		"""Used to change dictionary data to xlsx format.
		"""
		data = self._studData
		rows = dict_xlsx(self._studData,self._students,self._subjects)
		wb = Workbook()

		ws = wb.active
		ws.title = "Student_data"
		
		for each in rows:
	
			ws.append(each)
		in_1 = self._students[0]
		
		subs = self._subjects
		
		mg_strt = 2
		for each in data[in_1]:
			each = data[in_1][each]
			if type(each) == dict:
				col_mv = len(each) - 1
				mg_end = mg_strt + len(each) - 1
				mv_strt = mg_strt + 1
				mv_end = mg_strt + len(subs) - 1
				ch1 = f"{gcl(mg_strt)}1"
				ch2 = f"{gcl(mg_end)}1"
				ch3 = f"{gcl(mv_strt)}1"
				ch4 = f"{gcl(mv_end)}1"
									
				ws.move_range(f"{ch3}:{ch4}",cols=col_mv)
				ws.merge_cells(f"{ch1}:{ch2}")
									
				mg_strt += len(each)
				
			
		
		wb.save("student_info.xlsx")
		
			
		