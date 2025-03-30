"""This package provides Different functions and class used to manipulate students mark in different ways like:
	- calculating gpa 
	- calculating grade and point 
	- calculating average 
	- ranking
	- giving id number
	- retrieving data about single subject or single student.

it has the following class:
	StudMark
and the following functions:
	gradeFun
	pointFun
	gpaFun
	gpa
	average
	
usage:
	with StudMark class:
	
		- declare an object with StudMark class:
			the class recives:
				- dictionary 
				- xlsx file or
				- json file that has students name and mark associated with the subjects
			initialize:
				- students name
				- subjects
				- marks
				- total students number
				- maximum mark and 
				- minimum mark
			do the following things:
				- sort students 
				- calculate grade
				- calculate gpa
				- calculate point
				- calculate average 
				- give rank
				- give id number 
				- information about specific students 
				- information about specific subject
				- save the data with json file 
				- save the data with xlsx file
	with gpaFun and gpa :
		calculate gpa by receiving marks and credit hours
	
	with pointFun:
		calculate point of the single mark
	with gradeFun:
		calculate grade of the single mark
	with average:
		calculate average of the single mark
		

"""
from .calculate.student_mark import StudMark
from .calculate.oneStud.grading import gradeFun,pointFun,gpaFun,gpa,average
