import pytest
from course_grader import convert_to_letter_grade

# TODO-1: Add test_exact_grade_boundaries() function
def test_exact_grade_boundaries():
    print(convert_to_letter_grade(score=0))
    print(convert_to_letter_grade(score=59))
    print(convert_to_letter_grade(score=60))
    print(convert_to_letter_grade(score=69))
    print(convert_to_letter_grade(score=70))
    print(convert_to_letter_grade(score=79))
    print(convert_to_letter_grade(score=80))
    print(convert_to_letter_grade(score=89))
    print(convert_to_letter_grade(score=90))

# TODO-2: Add test_invalid_numerical_score() function
def test_invalid_numerical_score():
    convert_to_letter_grade(score=-1)
    
    convert_to_letter_grade(score=101)

# TODO-3: Add test_non_numeric_input() function
def test_non_numeric_input():
    str = ""
    list = [1, 2, 3]
    n = None

    convert_to_letter_grade(str)

    convert_to_letter_grade(list)

    convert_to_letter_grade(n)

