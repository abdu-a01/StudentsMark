"""This module is for testing all functions and the class."""

from pathlib import Path
import pytest
from .student import StudMark, point_fun, gpa_fun, grade_fun, gpa, average


test_data = {
    "abdu": {"English": 87, "Maths": 92, "OOP": 97},
    "selam": {"English": 83, "Maths": 97, "OOP": 91},
}

def test_xlsx_input():
	"""Testing the class with xlsx input 
	"""
	stud_data = StudMark("student_info.xlsx")
	
	assert stud_data.stud_data == test_data
	
def test_json_input():
	"""Testing the class with json input 
	"""
	stud_data = StudMark("student_data.json")
	
	assert stud_data.stud_data == test_data

# testing the class
class TestStudMark:
    """class for testing StudMark class"""

    def setup_method(self, method):
        """declaring object for the class"""

        self.test_mark = StudMark(test_data)
        return self.test_mark

    def teardown_method(self, method):
        """deleting the object after usage"""

        del self.test_mark

    def test_attributes(self):
        """testing all attributes"""

        assert self.test_mark.stud_data == test_data
        assert self.test_mark.students == ["abdu", "selam"]
        assert self.test_mark.all_mark == [[87, 92, 97], [83, 97, 91]]
        assert self.test_mark.subjects == ["English", "Maths", "OOP"]
        assert self.test_mark.total == 2
        assert self.test_mark.max_sub == {"Maths": 94.5}
        assert self.test_mark.min_sub == {"English": 85}

    def test_sort(self):
        """testing sort method"""
        assert self.test_mark.sort() == test_data

    def test_grade(self):
        """testing grade method"""
        grade = {
            "abdu": {
                "English": {"mark": 87, "grade": "A"},
                "Maths": {"mark": 92, "grade": "A+"},
                "OOP": {"mark": 97, "grade": "A+"},
            },
            "selam": {
                "English": {"mark": 83, "grade": "A-"},
                "Maths": {"mark": 97, "grade": "A+"},
                "OOP": {"mark": 91, "grade": "A+"},
            },
        }
        
        not_update = self.test_mark.grade()
        assert (
        	not_update == grade and
        	self.test_mark.stud_data != grade
        )
        
        self.test_mark.grade(update=True)
        
        assert self.test_mark.stud_data == grade

    def test_point(self):
        """testing point method"""
        point = {
            "abdu": {
                "English": {"mark": 87, "point": 4.0},
                "Maths": {"mark": 92, "point": 4.0},
                "OOP": {"mark": 97, "point": 4.0},
            },
            "selam": {
                "English": {"mark": 83, "point": 3.75},
                "Maths": {"mark": 97, "point": 4.0},
                "OOP": {"mark": 91, "point": 4.0},
            },
        }
        
        not_update = self.test_mark.point()
        assert (
        	not_update == point and
        	self.test_mark.stud_data != point
        )
        
        self.test_mark.point(update=True)
        
        assert self.test_mark.stud_data == point


    def test_gpa(self):
        """testing gpa method"""
        gpa_var = {
            "abdu": {"English": 87, "Maths": 92, "OOP": 97, "gpa": 4.0},
            "selam": {"English": 83, "Maths": 97, "OOP": 91, "gpa": 3.92},
        }
        
        not_update = self.test_mark.gpa((3, 3, 3))

        assert (
        	not_update == gpa_var and
        	self.test_mark.stud_data != gpa_var
        )
        
        self.test_mark.gpa((3, 3, 3),update=True)
        
        assert self.test_mark.stud_data == gpa_var

    def test_average(self):
        """testing average method"""
        aver = {
            "abdu": {"English": 87, "Maths": 92, "OOP": 97, "average": 92.0},
            "selam": {"English": 83, "Maths": 97, "OOP": 91, "average": 90.33},
        }
        
        not_update = self.test_mark.average()
        
        assert (
        	not_update == aver and
        	self.test_mark.stud_data != aver
        )
        
        self.test_mark.average(update=True)
        
        assert self.test_mark.stud_data == aver


    def test_ranker(self):
        """testing ranker method"""
        rank = {
            "abdu": {"English": 87, "Maths": 92, "OOP": 97, "rank": 1},
            "selam": {"English": 83, "Maths": 97, "OOP": 91, "rank": 2},
        }


        
        not_update = self.test_mark.ranker()
        
        assert (
        	not_update == rank and
        	self.test_mark.stud_data != rank
        )
        
        self.test_mark.ranker(update=True)
        
        assert self.test_mark.stud_data == rank




    def test_id_giver(self):
        """testing id_giver method"""
        id_gived = {
            "abdu": {"English": 87, "Maths": 92, "OOP": 97, "id_number": "0001"},
            "selam": {"English": 83, "Maths": 97, "OOP": 91, "id_number": "0002"},
        }

        self.test_mark.id_giver()

        assert self.test_mark.stud_data == id_gived

    def test_one_sub(self):
        """testing one_sub method"""

        @pytest.fixture
        def class_subject():
            return self.test_mark.one_sub("English")

        def test_max_mark(class_subject):

            assert class_subject.max_mark() == {"abdu": 87}

        def test_min_mark(class_subject):

            assert class_subject.max_mark() == {"selam": 83}

        def test_average(class_subject):

            assert class_subject.average() == 85.0

        def test_full_data(class_subject):

            assert class_subject.full_mark() == {"abdu": 87, "selam": 83}

    def test_one_stud(self):
        """testing one_stud method"""

        @pytest.fixture
        def class_student():
            return self.test_mark.one_stud("abdu")

        def test_attributes(class_student):

            assert class_student.info == {
                "abdu": {"English": 87, "Maths": 92, "OOP": 97}
            }
            assert class_student.marks == [87, 92, 97]

        def test_max_mark(class_student):

            assert class_student.max_mark() == {"OOP": 97}

        def test_min_mark(class_student):

            assert class_student.min_mark() == {"English": 87}

        def test_average(class_student):

            assert class_student.average() == 92.0

        def test_grade(class_student):

            assert class_student.grade() == ["A", "A+", "A+"]

        def test_point(class_student):

            assert class_student.point() == [4.0, 4.0, 4.0]

        def test_gpa(class_student):

            assert class_student.gpa((3, 3, 3)) == 4.0

    def test_json(self):
        """testing json method"""
        self.test_mark.json()
        file = Path("student_data.json")
        assert file.is_file() is True

    def test_xlsx(self):
        """testing xlsx method"""
        self.test_mark.xlsx()
        file = Path("student_info.xlsx")
        assert file.is_file() is True


# testing functions
def test_grade_fun():
    """testing grade_fun function"""
    assert grade_fun(91) == "A+"


def test_point_fun():
    """testing point_fun function"""
    assert point_fun(91) == 4.0


def test_gpa_fun():
    """testing gpa_fun function"""
    assert gpa_fun((98, 97, 87), (3, 3, 3)) == 4.0


def test_gpa():
    """testing gpa function"""
    assert gpa((98, 3), (89, 2), (97, 3)) == 4.0


def test_average():
    """testing average function"""
    assert average(98, 96, 97) == 97.0
