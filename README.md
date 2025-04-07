# Students Mark 
**Students Mark** is clear and easy to use for retrieve information about students mark.

```python
>>> import student
>>> stud_data = student.StudMark(data.xlsx)
>>> stud_1 = stud_data.one_stud('stud 1')
>>> stud_1.average()
98
>>> stud_1.grade('english')
A+
>>> stud_data.studData
{'stud 1':{'english':98...}}
```
**Students Mark** used to retrieve information and calculate mark related things with simple stapes. You need only give basic students mark. Then you can calculate and retrieve information about these marks.

## Installing Students Mark and supported version
Students Mark is not available on pypi.
You can install it from GitHub repository 

```console
$ python -m pip install git+https://github.com/abdu-a01/StudentsMark.git
```
or
```console
$ python -m pip install https://github.com/abdu-a01/StudentsMark/archive/refs/heads/master.zip
```
Students Mark supports python 3.8+.

## supported features & Best-practices

**Students Mark** is ready for make easy calculation and searching information about students mark.

- calculate gpa, average and other mark related things for one student or multiple students
- giving rank and id number
- retrieve information about single student 
- retrieve information about single subject
- saving data as json or xlsx file 


