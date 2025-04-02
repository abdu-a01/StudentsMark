"""
This module used for validating mark  before calculating gpa grade or points
this module have 3 functions:
        -isfloat(obj):
        -checkMark(mark):
        -checkIndex(arg1,arg2):
"""


def isfloat(obj):
    """Check if the 'obj' can be casted to float or not
    if obj can be casted:
            return True
    else:
            return False
    """
    try:
        float(obj)
    except (ValueError, TypeError):
        return False

    return True


def check_mark(mark):
    """checkMark checks if mark is valid or not!
    mark is valid if it can be casted to float and then it is more than zero
    if mark can be casted to float and more than zero:
            return mark casted to float
    else:
            raise ValueError
    """
    if isfloat(mark):
        if float(mark) < 0:
            raise ValueError(
                "Mark should be greater than zero negative doesn't have grade."
            )

        return float(mark)

    raise ValueError("Mark should be number only")


def check_index(arg1, arg2):
    """checkIndex checks:
            - if arg1 and arg2 are list or tuple
            - if length of arg1 and arg2 is the same
            - if all elements in arg2 are positive integer numbers

    if arg1 and arg2 are not list or tuple :
            raise TypeError
    else if length of mark and length of cr hours are not the same:
            raise ValueError
    else if elements of credit hour are not positive integer numbers:
            raise ValueError
    else:
            return None
    """
    if type(arg1) not in [list, tuple] or type(arg2) not in [list, tuple]:
        raise TypeError("You should give mark and credit hour with list or tuple")

    if len(arg1) != len(arg2):
        raise ValueError("number of mark and their credit hour should be the same")

    if not all(map(lambda x: isinstance(x, int) and x > 0, arg2)):
        raise ValueError("credit hour should be positive integer number only")
